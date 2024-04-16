import logging
from time import sleep
from multiprocessing import Process, Queue, Value
from base64 import b64encode
from cv2 import imencode
from .Rpcer import Rpcer
from .FeatureExtractor import FeatureExtractor
from .SignalProcessor import SignalProcessor as sp
from .protos.Validation_pb2 import ReportTimeout, InvalidStartFrame
from .Utilities import Utility as util


class MeasurerProcess(Process):
    def __init__(self, **kwargs):
        super().__init__()
        logging_config = kwargs.get('logging_config')
        if logging_config:
            logging.basicConfig(**logging_config)

        self.__queue: Queue = kwargs['queue']
        self.__start_frame = kwargs['start_frame']
        self.__measuring_flag: Value = kwargs['measuring_flag']
        self.__accomplish = kwargs['accomplish']
        self.__handle_error = kwargs['handle_error']
        self.__rpc = None

        try:
            self.__rpc = Rpcer(**kwargs)
            self.__extractor = FeatureExtractor(**kwargs)
        except ValueError as error:
            interrupted, config, addition = util.validate_error(error)
            self.stop(interrupted, error, config, **addition)
            if interrupted:
                return
        except Exception as ex:
            self.stop(exception=ex)
            return

    def run(self):
        self.__creat_measurement()
        self.__process_frames()
        self.__wait_report()

    @property
    def measurement_id(self):
        return self.__rpc.measurement_id

    def __creat_measurement(self):
        """
        创建测量
        """
        encoded_image = None
        try:
            success, encoded_image = imencode('.jpg', self.__start_frame)
            if not success:
                util.generate_error(InvalidStartFrame)
            sp.validate(*sp.detect(self.__start_frame))
        except ValueError as error:
            interrupted, config, addition = util.validate_error(error)
            self.stop(interrupted, error, config, **addition)
            if interrupted:
                return
        except Exception as ex:
            return self.stop(exception=ex)

        self.__rpc.start(b64encode(encoded_image).decode('utf-8'))

    def __process_frames(self):
        """
        处理视频帧
        """
        frame_order = 0
        format_message = lambda suffix: {
            'message': f"measurement_id:{self.measurement_id} frame_order:{frame_order}{' ' + suffix if suffix else suffix} {{}}"}
        try:
            while util.get_shared_value(self.__measuring_flag):
                # 检出视频帧
                if self.__queue.empty() or not self.measurement_id:
                    sleep(0.1)
                    continue

                frame_obj = self.__queue.get()
                frame = frame_obj['frame']
                frame_features = None

                # 校验视频帧
                try:
                    frame_features = sp.detect(frame)
                    position = sp.validate(*frame_features)
                    self.__extractor.validate(frame_features[0], *position)
                except ValueError as error:
                    interrupted, config, addition = util.validate_error(error)
                    self.stop(interrupted, error, config, **addition, **format_message(''))
                    if interrupted:
                        return
                except Exception as ex:
                    return self.stop(exception=ex, **format_message(ex))

                frame_order = frame_obj['order']
                frame_timestamp = frame_obj['timestamp']
                logging.debug(format_message(f'start to process frame {frame_timestamp}')['message'])
                status = self.__extractor.process_frame(frame, frame_timestamp, *frame_features)

                match status:
                    case 0:  # 无chunk
                        continue
                    case 1:  # 阶段性chunk
                        chunk_no, chunk = self.__extractor.chunk
                        self.__rpc.push_physiology_chunk(util.serialize_message(chunk))
                        logging.debug(f'measurement_id:{self.measurement_id} packaged chunk {chunk_no}')
                    case 2:  # 完整chunk
                        self.__rpc.push_physiology_chunk(util.serialize_message(self.__extractor.physiology_chunk))
                        self.__rpc.push_emotion_chunk(util.serialize_message(self.__extractor.emotion_chunk))
                        logging.debug(f'measurement_id:{self.measurement_id} finished packaging all chunks')
                        break
                    case _:
                        return self.stop(**format_message('invalid extraction status'))
        except Exception as ex:
            # 异常中断测量
            self.stop(exception=ex, **format_message(ex.args[0]))

    def __wait_report(self):
        """
        等待健康报告
        """
        waited_time, interval = 0, 0.2
        while util.get_shared_value(self.__measuring_flag):
            sleep(interval)
            waited_time += interval

            timeout = util.get_validation(ReportTimeout)['timeout']
            if waited_time < timeout:
                continue
            return self.stop(
                error=util.generate_error(ReportTimeout, False,
                                          message=f'measurement_id:{self.measurement_id} {{}} {timeout}'))

        self.__accomplish()

    def stop(self, interrupted=True, error=None, exception_config=None, **kwargs):
        if interrupted and self.__rpc:
            self.__rpc.stop()
        if error is not None or kwargs:
            self.__handle_error(error, exception_config, **kwargs)

import datetime
import typing
from enum import Enum


class Worker:
    worker_id: str
    gpu_type: typing.Optional[str]
    region: str
    started_at: datetime.datetime
    last_service_time: datetime.datetime
    number_of_successes: int
    number_of_failures: int
    # if number_of_successes great than zero, this worker cloud not be scale down
    number_of_sessions: int
    average_response_time: int


class QueueReason(Enum):
    #
    NotDispatch = "NotDispatch"
    # all worker is busy
    QueueDueBusy = 'QueueDueBusy'
    # session worker is busy
    QueueDueSession = 'QueueDueSession'


class Request:
    # time of enter the queue
    queue_time: datetime.datetime
    # queue reason
    queue_reason: QueueReason


class Queue:
    requests: list[Request]


class Factors:
    def __init__(self):
        # 10 -> queue information at 10 seconds ago
        # 30 -> queue information at 30 seconds ago
        # 60 -> queue information at 60 seconds ago
        queue_histories: dict[int, Queue]

        queue: Queue

        workers: list[Worker]

import datetime
import typing
from enum import Enum


class WorkerStatus(Enum):
    # The worker be started, and not working yet
    Inflight = "Inflight"
    # The worker is free
    Free = 'Free'
    # The worker is busy now
    Busy = 'Busy'


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
    status: WorkerStatus


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
    # 10 -> queue information at 10 seconds ago
    # 30 -> queue information at 30 seconds ago
    # 60 -> queue information at 60 seconds ago
    queue_histories: dict[int, Queue]

    queue: Queue

    workers: list[Worker]

    def __init__(
            self,
            queue_histories: dict[int, Queue] = None,
            queue: Queue = None,
            workers: list[Worker] = None,
    ):
        self.queue_histories = queue_histories
        self.queue = queue
        self.workers = workers

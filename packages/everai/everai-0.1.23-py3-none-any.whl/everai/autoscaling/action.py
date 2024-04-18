import typing


class ScaleUpAction:
    count: int

    def __init__(self, count: int) -> None:
        self.count = count


class ScaleDownAction:
    worker_id: str

    def __init__(self, worker_id: str) -> None:
        self.worker_id = worker_id


Action = typing.Union[ScaleUpAction, ScaleDownAction]
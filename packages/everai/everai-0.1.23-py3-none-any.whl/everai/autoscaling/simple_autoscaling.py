from everai.autoscaling.action import Action, ScaleUpAction, ScaleDownAction
from everai.autoscaling.autoscaling_policy import AutoScalingPolicy
from everai.autoscaling.factors import Factors

class SimpleAutoScalingPolicy(AutoScalingPolicy):
    # The minimum number of worker, even all of those are idle
    min_workers: int
    # The maximum number of worker, even there are some request in queue
    max_workers: int
    # The max_queue_size let scheduler know it's time to scale up
    max_queue_size: int
    # The max_idle_time in seconds let scheduler witch worker should be scale down
    max_idle_time: int

    def __init__(self, min_workers: int, max_workers: int, max_queue_size: int, max_idle_time: int):
        self.min_workers = min_workers
        self.max_workers = max_workers
        self.max_queue_size = max_queue_size
        self.max_idle_time = max_idle_time

    def should_scale_up(self, factors: Factors) -> bool:
        ...

    def decide(self, factors: Factors) -> list[Action]:
        if len(factors.workers) < self.min_workers:
            return [ScaleUpAction(self.min_workers - len(factors.workers))]


        return [ScaleUpAction(3), ScaleDownAction('12')]

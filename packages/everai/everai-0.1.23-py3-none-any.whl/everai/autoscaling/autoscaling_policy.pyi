from everai.autoscaling.action import Action
from everai.autoscaling.factors import Factors

class AutoScalingPolicy:
    def decide(self, factors: Factors) -> list[Action]: ...

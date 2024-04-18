from abc import ABC, abstractmethod
from everai.autoscaling.factors import Factors
from everai.autoscaling.action import Action


class AutoScalingPolicy(ABC):
    @abstractmethod
    def decide(self, factors: Factors) -> list[Action]: ...

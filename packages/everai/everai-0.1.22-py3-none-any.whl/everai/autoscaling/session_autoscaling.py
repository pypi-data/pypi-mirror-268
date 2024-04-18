from everai.autoscaling import SimpleAutoScalingPolicy
from everai.autoscaling.action import Action


class SessionAutoScalingPolicy(SimpleAutoScalingPolicy):
    # The maximum sessions that one worker could hold
    max_sessions_per_worker: int

    # The maximum idle time for a session, If a session does not receive any requests for more than this period of time,
    # the session will be removed.
    session_living_period: int

    def __init__(self, max_sessions_per_worker: int, session_living_period: int, *args, **kwargs):
        self.max_sessions_per_worker = max_sessions_per_worker
        self.session_living_period = session_living_period
        super().__init__(*args, **kwargs)

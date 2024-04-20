import cooptools.geometry_utils.vector_utils as vec
from cooptools.physics.movement import Velocity, Acceleration
from cooptools.transform import Transform, Translation
import logging
from typing import Optional, Tuple, Iterable, List
from cooptools.physics.kinematic import GoalSeeker
from cooptools.physics.waypoint import Waypoint

logger = logging.getLogger(__name__)

class WaypointFollower(GoalSeeker):
    def __init__(self,
                 name: str,
                 initial_transform: Transform,
                 max_acceleration: float,
                 initial_velocity: Velocity = None,
                 initial_acceleration: Acceleration = None,
                 initial_goal: vec.FloatVec = None,
                 history_len: int = None
                 ):
        GoalSeeker.__init__(self,
                            name=name,
                            initial_transform=initial_transform,
                            max_acceleration=max_acceleration,
                            initial_velocity=initial_velocity,
                            initial_acceleration=initial_acceleration,
                            initial_goal=initial_goal,
                            history_len=history_len)
        self.waypoints: List[Waypoint] = []

    def add_waypoints(self, waypoints: Iterable[Waypoint], index: int = -1):
        if index < 0 or index > len(self.waypoints):
            self.waypoints += waypoints
            logger.debug(f"Appending waypoints to agent {self.Name}: {waypoints}")
        else:
            self.waypoints[index:index] = waypoints
            logger.debug(f"Adding waypoints to agent {self.Name} at index [{index}]: {waypoints}")

    def get_next_waypoint(self) -> Waypoint:
        if len(self.waypoints) > 1:
            segment = self.waypoints[1]
            return segment
        else:
            return None

    def get_next_destination(self) -> Waypoint:
        if len(self.waypoints) > 1:
            destination = next(x for x in self.waypoints if x.is_destination)
            return destination
        else:
            return None

    def get_segments_to_next_destination(self):
        segments = []
        if len(self.waypoints) > 0:
            for x in self.waypoints:
                segments.append(x)
                if x.is_destination:
                    break

            return segments
        else:
            return None

    def length_remaining_for_agent(self):
        current_segment = self.waypoints[1]
        length_of_remaining_segments = vec.vector_len(vec.vector_between(self.Position.Vector, current_segment.end_pos))

        last = current_segment
        for ii in range(2, len(self.waypoints)):
            next = self.waypoints[ii]
            length = vec.vector_len(vec.vector_between(last.end_pos, next.end_pos))
            length_of_remaining_segments += length

        return length_of_remaining_segments

    def agent_last_pos(self):
        return self.waypoints[-1].end_pos if len(self.waypoints) > 0 else self.Position

if __name__ == "__main__":
    from cooptools.timedDecay import TimeTracker
    import logging
    from cooptools.loggingHelpers import BASE_LOG_FORMAT
    logging.basicConfig(level=logging.INFO, format=BASE_LOG_FORMAT)
    import random as rnd

    def test_1():
        wf = WaypointFollower(
            name='Coop',
            initial_transform=Transform(
                translation=(0, 0)),
            max_acceleration=5
        )

        tt = TimeTracker()
        goal = (0, 100)
        rnd.seed(0)
        while True:
            reached = wf.update(delta_time_ms=tt.Delta_MS, goal_pos=goal)
            logger.info(f"{wf.Position} -- {wf.Velocity} -- {wf.Acceleration}")
            # tt.update(delta_ms=1)
            tt.update()
            if reached:
                goal = (rnd.randint(0, 100), rnd.randint(0, 100))

    test_1()
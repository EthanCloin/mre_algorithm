class RangeChecker:
    """this class keeps track of the status of the connection
    off all the bots and station"""
    def __init__(self, robots, base_station, settings):
        self.robots = robots
        self.base_station = base_station
        self.settings = settings

        self.status = None

    def check_config(self, pos):
        # check whether pos is in range of base station

        # check whether pos is in range of another robot

        # for pos in range of another robot
            # check if other robot is in range of any other robots
            # check
        pass


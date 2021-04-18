import pygame as pg
import math


class Settings:
    """This class defines settings and constants as needed
    for each of the classes used in this program."""

    def __init__(self):
        """Initialize settings"""
        # Screen Settings
        self.screen_width = 600
        self.screen_height = 600
        self.bg_color = pg.Color('gray87')

        # Node Settings
        self.unexplored_color = pg.Color('grey100')
        self.visited_color = pg.Color('green3')
        self.obstacle_color = pg.Color('grey0')
        self.frontier_color = pg.Color('yellow1')
        self.robot_color = pg.Color('orangered1')
        self.base_station_color = pg.Color('orchid')
        self.node_width = 20

        # Grid Settings
        self.grid_width = 600
        self.grid_height = 600
        self.grid_rows = 50
        self.grid_color = pg.Color('gray87')

        # Robot Settings
        self.robot_range = 5
        self.robot_pack_size = 5

        # Base Station Settings
        self.base_station_range = 15

        # Algorithm Settings
        self.search_max = 25
        self.pop_max = 50

"""
Manhattan distance data: 1 node = 12px distance
                         1 node diag = 24px distance
"""
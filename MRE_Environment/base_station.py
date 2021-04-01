from node import Node
import pygame as pg


class BaseStation:

    def __init__(self, node, settings):
        self.node = node
        self.range = settings.base_station_range
        self.position = node.get_position()
        self.x = node.x
        self.y = node.y
        self.color = settings.base_station_color
        self.center = self.position[0] + node.width / 2, self.position[1] + node.width / 2

    def display_range(self, screen):
        """draw a circle representing the range of base_station"""
        pg.draw.circle(screen, self.color, self.center, self.range, 2)

    def draw(self, screen):
        """Represent BaseStation as pygame rect on given pygame Surface"""
        pg.draw.rect(screen, self.color, (self.node.x, self.node.y,
                                          self.node.width, self.node.width))

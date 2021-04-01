import pygame as pg
from node import Node
import random


class Robot:
    """This class defines behaviors of robotic agents in
    the exploration simulation"""
    pack_size = 3

    def __init__(self, node, settings):
        """Creates a Robot object given a node"""
        self.node = node
        self.row = node.row
        self.col = node.col
        self.x = node.x
        self.y = node.y
        self.width = node.width
        self.neighbors = node.neighbors
        #self.nearest_frontier = None
        self.pack_size = settings.robot_pack_size
        self.range = settings.robot_range # in px distance
        self.color = settings.robot_color
        self.settings = settings
        self.center = self.x + node.width / 2, self.y + node.width / 2

    def display_range(self, screen):
        """draw a circle representing the range of robot"""
        pg.draw.circle(screen, self.color, self.center, self.range * 12, 2)

    def get_frontier_distance(self, frontiers):
        """Returns manhattan distance to nearest frontier node"""
        pass

    def get_base_distance(self, base_station):
        """Returns manhattan distance to base_station"""
        pass

    def draw(self, screen):
        """Represent Robot as pygame rect on given pygame Surface"""
        pg.draw.rect(screen, self.color, (self.x, self.y,
                                          self.width, self.width))
        self.display_range(screen)

    def move_north(self, grid):
        """relocate robot one tile south. Returns "dne" if nonexistent"""
        # check for legal northern neighbor
        north_neighbor = self.node.get_north_neighbor(grid)
        if north_neighbor is None:
            return "dne"

        # set current node to green
        grid[self.row][self.col].set_visited()

        # update node neighbors
        north_neighbor.neighbors = north_neighbor.get_neighbors(grid)

        # update node to northern neighbor
        self.node = north_neighbor

        # update robot to match node attributes
        self.update_to_node()

    def move_south(self, grid):
        """relocate robot one tile south. Returns "dne" if nonexistent"""
        # check for legal southern neighbor
        south_neighbor = self.node.get_south_neighbor(grid)
        if south_neighbor is None:
            return "dne"

        # set current node to green
        grid[self.row][self.col].set_visited()

        # update node neighbors
        south_neighbor.neighbors = south_neighbor.get_neighbors(grid)

        # update node to southern neighbor
        self.node = south_neighbor

        # update robot to match node attributes
        self.update_to_node()

    def move_east(self, grid):
        """relocate robot one tile East. Returns "dne" if nonexistent"""
        # check for legal eastern neighbor
        east_neighbor = self.node.get_east_neighbor(grid)
        if east_neighbor is None:
            return "dne"

        # set current node to green
        grid[self.row][self.col].set_visited()

        # update node neighbors
        east_neighbor.neighbors = east_neighbor.get_neighbors(grid)

        # update node to eastern neighbor
        self.node = east_neighbor

        # update robot to match node attributes
        self.update_to_node()

    def move_west(self, grid):
        """relocate robot one tile west. Returns "dne" if nonexistent"""
        # check for legal western neighbor
        west_neighbor = self.node.get_west_neighbor(grid)
        if west_neighbor is None:
            return "dne"

        # set current node to green
        grid[self.row][self.col].set_visited()

        # update node neighbors
        west_neighbor.neighbors = west_neighbor.get_neighbors(grid)

        # update node to western neighbor
        self.node = west_neighbor

        # update robot to match node attributes
        self.update_to_node()

    def move_northwest(self, grid):
        # check for legal northwestern neighbor
        northwest_neighbor = self.node.get_northwest_neighbor(grid)
        if northwest_neighbor is None:
            return "dne"

        # set current node to green
        grid[self.row][self.col].set_visited()

        # update node neighbors
        northwest_neighbor.neighbors = northwest_neighbor.get_neighbors(grid)

        # update node to northwestern neighbor
        self.node = northwest_neighbor

        # update robot to match node attributes
        self.update_to_node()

    def move_southwest(self, grid):
        """relocate robot one tile southwest"""
        # check for legal southwestern neighbor
        southwest_neighbor = self.node.get_southwest_neighbor(grid)
        if southwest_neighbor is None:
            return "dne"

        # set current node to green
        grid[self.row][self.col].set_visited()

        # update node neighbors
        southwest_neighbor.neighbors = southwest_neighbor.get_neighbors(grid)

        # update node to southwestern neighbor
        self.node = southwest_neighbor

        # update robot to match node attributes
        self.update_to_node()

    def move_northeast(self, grid):
        """relocate robot one tile northeast"""
        # check for legal northeastern neighbor
        northeast_neighbor = self.node.get_northeast_neighbor(grid)
        if northeast_neighbor is None:
            return "dne"

        # set current node to green
        grid[self.row][self.col].set_visited()

        # update node neighbors
        northeast_neighbor.neighbors = northeast_neighbor.get_neighbors(grid)

        # update node to northeastern neighbor
        self.node = northeast_neighbor

        # update robot to match node attributes
        self.update_to_node()

    def move_southeast(self, grid):
        """relocate robot one tile southeast"""
        # check for legal southeastern neighbor
        southeast_neighbor = self.node.get_southeast_neighbor(grid)
        if southeast_neighbor is None:
            return "dne"

        # set current node to green
        grid[self.row][self.col].set_visited()

        # update node neighbors
        southeast_neighbor.neighbors = southeast_neighbor.get_neighbors(grid)

        # update node to southeastern neighbor
        self.node = southeast_neighbor

        # update robot to match node attributes
        self.update_to_node()
        self.node.set_robot()

    def to_string(self):
        string = f'row: {self.row} col: {self.col}\n' \
                 f'x: {self.x} y: {self.y} color: {self.color}'

        return string

    def get_neighbors(self):
        self.neighbors = self.node.get_neighbors()

    def update_to_node(self):
        """Updates all robot attributes to match its node"""
        self.x = self.node.x
        self.y = self.node.y
        self.row = self.node.row
        self.col = self.node.col
        self.neighbors = self.node.neighbors
        self.center = self.node.center
        self.node.set_robot()

    def print_neighbors(self):
        """call to_string for all nodes stored in neighbors"""
        print("robot call")
        print("neighbors: ", self.neighbors)
        for neighbor in self.neighbors:
            print(neighbor.to_string())

    def random_move(self, grid):
        directions = ["n", "s", "e", "w", "nw", "ne", "sw", "se", "stay"]
        choice = random.randint(0, 7)

        if directions[choice] == "n":
            self.move_north(grid)
        elif directions[choice] == 's':
            self.move_south(grid)
        elif directions[choice] == 'e':
            self.move_east(grid)
        elif directions[choice] == 'w':
            self.move_west(grid)
        elif directions[choice] == 'nw':
            self.move_northwest(grid)
        elif directions[choice] == 'ne':
            self.move_northeast(grid)
        elif directions[choice] == 'sw':
            self.move_southwest(grid)
        elif directions[choice] == 'se':
            self.move_southeast(grid)

        return "FAILED"

    def move_to(self, environment, target_node):
        """relocate robot to provided node"""
        # set current node to green
        current = environment.grid[self.row][self.col]
        current.set_visited()

        # update node neighbors
        target_node.neighbors = target_node.get_neighbors(environment.grid)

        # update node to southeastern neighbor
        self.node = target_node
        environment.visited.append(target_node)

        # update robot to match node attributes
        self.update_to_node()

    def get_random_neighbor(self, grid):
        """randomly picks between valid neighbor or staying"""
        # list to hold neighbors + self aka stay
        options = self.node.get_neighbors(grid)
        options.append(self.node)

        # select a random
        rand_index = random.randint(0, len(options) - 1)
        random_node = options[rand_index]
        return random_node

    def get_nearest_frontier(self, frontier):
        """This function searches the environment frontier and checks for the
        closest frontier node to the given robot"""

        # calculate all distances
        nearest = (99999, None)
        for f in frontier:
            dist = self.node.manhattan_distance(f)
            if dist < nearest[0]:
                # store distance and Node reference
                nearest = (dist, f)

        print(nearest[0])
        print(nearest[1].to_string())
        return nearest[1]
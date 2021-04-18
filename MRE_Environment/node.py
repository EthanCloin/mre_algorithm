import pygame as pg
import random
import math
from robot import Robot


class Node:
    """This class defines a Node object. Their color will
    update to represent exploration of the robots displayed
    on the Environment"""
    def __init__(self, row, col, width, total_rows, settings):
        """Initialize a Node as unexplored square"""
        self.row = row
        self.col = col
        self.width = width
        self.color = settings.unexplored_color
        self.settings = settings
        self.x = row * width
        self.y = col * width
        self.neighbors = []
        self.center = self.x + self.width / 2, self.y + self.width / 2

        # Status Functions
        self.base_flag = False

    def is_obstacle(self):
        """returns True if color matches obstacle"""
        return self.color == self.settings.obstacle_color

    def is_unexplored(self):
        """returns True if color matches unexplored"""
        return self.color == self.settings.unexplored_color

    def is_frontier(self):
        """returns True if color matches frontier"""
        return self.color == self.settings.frontier_color

    def is_visited(self):
        """returns True if color matches visited"""
        return self.color == self.settings.visited_color

    def is_robot(self):
        """returns True if color matches Robot"""
        return self.color == self.settings.robot_color

    def is_base_station(self):
        """returns True if color matches base_station"""
        return self.color == self.settings.base_station_color

    # Getter Functions
    def get_position(self):
        """returns the x,y position"""
        return self.x, self.y

# Setter Functions
    def set_obstacle(self):
        """changes Node to obstacle"""
        self.color = self.settings.obstacle_color

    def set_unexplored(self):
        """changes Node to unexplored"""
        self.color = self.settings.unexplored_color

    def set_frontier(self):
        """changes Node to frontier"""
        self.color = self.settings.frontier_color

    def set_visited(self):
        """changes Node to visited"""
        self.color = self.settings.visited_color

    def set_robot(self):
        """changes Node to Robot color"""
        self.color = self.settings.robot_color

    def set_base_station(self):
        """changes Node to BaseStation color"""
        self.color = self.settings.base_station_color

    def draw(self, screen):
        """Represent Node as pygame rect on given pygame Surface"""
        pg.draw.rect(screen, self.color, (self.x, self.y, self.width, self.width))

    def get_north_neighbor(self, grid):
        """Returns a node one unit North"""
        # if it won't go out of bounds
        if self.col > 0:
            north_node = grid[self.row][self.col - 1]
            return north_node
        return None

    def get_south_neighbor(self, grid):
        """Returns a node one unit South or None if dne"""
        # if it won't go out of bounds
        if self.col < self.settings.grid_rows - 1:
            south_node = grid[self.row][self.col + 1]
            return south_node
        return None

    def get_east_neighbor(self, grid):
        """Returns a node one unit East or None if dne"""
        # if it won't go out of bounds
        if self.row < self.settings.grid_rows - 1:
            east_node = grid[self.row + 1][self.col]
            return east_node
        return None

    def get_west_neighbor(self, grid):
        """Returns a node one unit West or None if dne"""
        # if it won't go out of bounds
        if self.row > 0:
            west_node = grid[self.row - 1][self.col]
            return west_node
        return None

    def get_northeast_neighbor(self, grid):
        """Returns a node one unit Northeast"""
        if self.row < self.settings.grid_rows - 1 and self.col > 0:
            northeast_node = grid[self.row + 1][self.col - 1]
            return northeast_node
        return None

    def get_northwest_neighbor(self, grid):
        """Returns a copied node one unit Northwest"""
        if self.row > 0 and self.col > 0:
            northwest_node = grid[self.row - 1][self.col - 1]
            return northwest_node
        return None

    def get_southeast_neighbor(self, grid):
        """Returns a copied node one unit Southeast"""
        if self.col < self.settings.grid_rows - 1 and self.row < self.settings.grid_rows - 1:
            southeast_node = grid[self.row + 1][self.col + 1]
            return southeast_node
        return None

    def get_southwest_neighbor(self, grid):
        """Returns a copied node one unit Northeast"""
        if self.col < self.settings.grid_rows - 1 and self.row > 0:
            southwest_node = grid[self.row - 1][self.col + 1]
            return southwest_node
        return None

    def get_neighbors(self, grid):
        """get neighbor nodes from all compass directions and add
        valid movement options to neighbor attribute"""

        neighbors = []
        n = self.get_north_neighbor(grid)
        # if n is not None:
            # print("North: " + n.to_string())
        neighbors.append(n)

        s = self.get_south_neighbor(grid)
        # if s is not None:
            # print("South: " + s.to_string())
        neighbors.append(s)

        e = self.get_east_neighbor(grid)
        # if e is not None:
            # print("East: " + e.to_string())
        neighbors.append(e)

        w = self.get_west_neighbor(grid)
        # if w is not None:
            # print("West: " + w.to_string())
        neighbors.append(w)

        nw = self.get_northwest_neighbor(grid)
        # print("Northwest: " + nw.to_string())
        neighbors.append(nw)
        #
        ne = self.get_northeast_neighbor(grid)
        # print("Northeast: " + ne.to_string())
        neighbors.append(ne)
        #
        sw = self.get_southwest_neighbor(grid)
        # print("Southwest: " + sw.to_string())
        neighbors.append(sw)
        #
        se = self.get_southeast_neighbor(grid)
        # print("Southeast: " + se.to_string())
        neighbors.append(se)

        for neighbor in neighbors:
            # check if valid
            if neighbor is None:
                neighbors.remove(neighbor)
                # print("Removed: none boi")
            elif neighbor.is_robot():
                neighbors.remove(neighbor)
                # print("Removed for robot: " + neighbor.to_string())
            elif neighbor.is_base_station():
                neighbors.remove(neighbor)
                # print("Removed for base station: " + neighbor.to_string())
            elif neighbor.is_obstacle():
                neighbors.remove(neighbor)
                # print("Removed for obstacle: " + neighbor.to_string())

        return neighbors

    def to_string(self):
        string = f'row: {self.row} col: {self.col}\n' \
                 f'x: {self.x} y: {self.y} color: {self.color}'

        return string

    def update_to_robot(self, robot):
        """use the attributes of given robot to update values of node"""
        self.row = robot.row
        self.col = robot.col
        self.x = robot.x
        self.y = robot.y
        self.set_visited()

    def print_neighbors(self):
        """call to_string for all nodes stored in neighbors"""
        print("called")
        for neighbor in self.neighbors:
            print(neighbor.to_string())

    def get_random_neighbor(self, grid):
        """randomly picks between valid neighbor or staying"""
        options = self.get_neighbors(grid)
        options.append(self.node)
        random_node = options[random.randint(0, len(options) - 1)]
        print(random_node.to_string())
        return random_node

    def manhattan_distance(self, node_2):
        return (abs(self.x - node_2.x) + abs(self.y - node_2.y)) / 12

    def find_nearest_frontier(self, environment):
        """searches within a 2 node radius and returns the nearest frontier node"""

        """
        Update this to search all frontiers for all robots
        
        """

        # define four corners
        nodes_in_radius = []
        corners = [self.get_northwest_neighbor(environment.grid),
                   self.get_northeast_neighbor(environment.grid),
                   self.get_southwest_neighbor(environment.grid),
                   self.get_southeast_neighbor(environment.grid)]

        # get neighbors for each corner
        for corner in corners:
            if corner is not None:
                nodes_in_radius.append(corner)
                neighbors = corner.get_neighbors(environment.grid)
                for neighbor in neighbors:
                    if neighbor is not None:
                        nodes_in_radius.append(neighbor)

        shortest_distance = 99999
        best_frontier = None
        distances = []

        # get least manhattan distance
        for node in nodes_in_radius:
            if node is not None:
                if node.is_frontier():
                    distance = node.manhattan_distance(self)
                    distances.append((distance, node))

                    if distance < shortest_distance:
                        shortest_distance = distance

        # check for multiple best options
        dupes = []
        for distance in distances:
            if distance[0] == shortest_distance:
                dupes.append(distance)
        print(dupes)

        if len(dupes) >= 1:
            # randomly pick among best options
            best_option = dupes[random.randint(0, len(dupes) - 1)]
            best_frontier = best_option[1]

            return best_frontier

        best_tuple = dupes[0]
        return best_tuple[1]

    def crows_distance(self, node_2):
        """Returns straight line distance ignoring obstacles"""
        return (math.sqrt( (node_2.x - self.x) ** 2 + (node_2.y - self.y) ** 2 )) / 12

    def get_nearest_frontier(self, frontier):
        """This function searches the environment frontier and checks for the
        closest frontier node to the given Node. Returns a tuple of form (distance, Node)"""

        # calculate all distances
        nearest = (99999, None)
        for f in frontier:
            dist = self.manhattan_distance(f)
            if dist < nearest[0]:
                # store distance and Node reference
                nearest = (dist, f)
        return nearest

    def can_communicate(self, robots, base_station):
        """Check whether the node is within communication range with
        at least one robot or the base station. Returns True if given
        node is within communication range of any robot/station. Currently
        forces all robots to remain within range of base station

        Should be replaced by graphstream but unclear how to implement that
        """
        results = []  # boolean list
        distances = []
        # Robot check
        for robot in robots:
            distance = robot.node.crows_distance(self)
            # how to ignore own robot?
            # trying ignore min distance
            distances.append(distance)


        # sort ascending and remove first
        distances.sort()
        distances.remove(distances[0])

        for distance in distances:
            if distance - robot.range <= robot.range:
                results.append(True)
            else:
                results.append(False)

        distance = base_station.node.crows_distance(self)
        if distance - robot.range <= base_station.range:
            results.append(True)
        else:
            # results.append(False)
            return False

        if True in results:
            return True

        return False

    def comms_check(self, environment):
        robots = environment.robots
        base_station = environment.base_station

        results = []
        distances = []

        # check whether the pos in range of base station
        distance_to_base = self.crows_distance(base_station.node)
        if distance_to_base <= base_station.range:
            self.base_flag = True
            return True

        # check whether the robots are in range of pos
        for robot in robots:
            robot.check_base_comms()
            distance_to_robot = self.crows_distance(robot.node)
            distances.append((distance_to_robot, robot))
        # sort ascending and remove first
        distances.sort()
        print("Removed: ", distances[0])
        distances.remove(distances[0])

        for distance in distances:
            if distance[0] <= environment.settings.robot_range:
                return True
            # check whether

    def config_can_communicate(self, config, environment):
        """translate config into list of robot objects and check their
        range overlaps. Return True if comms are maintained"""

        # translate config into list of robots
        robots = []
        for node in config:
            if node is None:
                return False
            my_robot = Robot(node, environment.settings)
            robots.append(my_robot)

        for my_robot in robots:
            # clear linked
            my_robot.linked.clear()
            # flag if within base
            if my_robot.node.crows_distance(environment.base_station.node) <= \
                    environment.base_station.range + my_robot.range:
                my_robot.base_flag = True

            # check what other bots are in range
            for other in robots:
                # ignore self
                if other == my_robot:
                    continue
                # add robot buddies in range to 'linked' list
                if other.node.manhattan_distance(my_robot.node) <= 2 * my_robot.range:
                    my_robot.linked.append(other)

            # check all buddies and if any connected to base, then flag this one as connected
            for buddy in my_robot.linked:
                if buddy.base_flag:
                    my_robot.base_flag = True

        # after updating all 3, check whether any of the robots are out of comms range
        for my_robot in robots:
            if not my_robot.base_flag:
                return False

        return True

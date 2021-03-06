import pygame as pg
from multi_robot_exploration.base_station import BaseStation
from multi_robot_exploration.node import Node
from multi_robot_exploration.robot import Robot


class Environment:
    """This class represents the visualization of the MRE
    Algorithm. It includes an "ad_hoc_map" with complete information
    and an "exploration_map" that is built by the Robots as the
    algorithm executes"""

    def __init__(self, settings):
        """initialize Environment"""
        self.screen = self.build_screen(settings)
        self.settings = settings
        self.grid = self.build_grid(settings.grid_rows, settings.grid_width)
        self.robots = []
        self.base_station = None

        self.visited = []
        self.frontier = (
            []
        )  # use this list to allow all robots to search for nearest to them
        self.obstacles = []

    def build_screen(self, settings):
        """builds the primary surface for display"""
        screen = pg.display.set_mode((settings.screen_width, settings.screen_height))
        pg.display.set_caption("Multi-Robot Exploration")
        screen.fill(settings.bg_color)
        return screen

    def show_instructions_popup(self, settings):
        self.screen.fill(settings.unexplored_color)
        font = pg.font.Font(None, 20)
        textbox = pg.Rect(25, 50, 140, 32)

        text_surface = font.render(
            "Press 'R' to spawn robots, 'Space' to set them exploring, "
            "and 'Enter' to dismiss this message!",
            True,
            settings.obstacle_color,
        )
        self.screen.blit(text_surface, (10, self.screen.get_height() / 2))
        pg.draw.rect(self.screen, settings.unexplored_color, textbox, 2)
        pg.display.flip()

    def load_ad_hoc(self):
        # import the data defining the environment
        # should be composed of a grid of Nodes that
        # are appropriately colored to represent obstacles
        pass

    def build_grid(self, rows, width):
        """Construct a grid of nodes with dimensions
        defined by the settings module"""
        grid = []
        gap = width // rows
        for i in range(rows):
            grid.append([])
            for j in range(rows):
                node = Node(i, j, gap, rows, self.settings)
                grid[i].append(node)

        return grid

    def draw_gridlines(self, screen, rows, width):
        """draws a visual representation of gridlines between nodes"""
        gap = width // rows
        for i in range(rows):
            pg.draw.line(
                screen, self.settings.grid_color, (0, i * gap), (width, i * gap)
            )
            for j in range(rows):
                pg.draw.line(
                    screen, self.settings.grid_color, (j * gap, 0), (j * gap, width)
                )

    def draw_env(self, screen, rows, width):
        """draws the environment with all its attributes"""
        # Draw grid
        for row in self.grid:
            for node in row:
                node.draw(self.screen)

        # Draw frontier
        for each in self.frontier:
            each.set_frontier()
            each.draw(self.screen)

        # Draw obstacles
        for obstacle in self.obstacles:
            obstacle.draw(self.screen)

        # Draw visited nodes
        for each in self.visited:
            each.set_visited()
            each.draw(self.screen)

        # Draw robots
        for robot in self.robots:
            robot.node.set_robot()
            robot.draw(self.screen)

        # If initialized, draw base_station and radius
        if self.base_station is not None:
            self.base_station.draw(self.screen)
            self.base_station.display_range(self.screen)

        self.draw_gridlines(screen, rows, width)

    def get_clicked_grid(self, pos, rows, width):
        """returns the node located at the position clicked"""
        gap = width // rows
        y, x = pos
        row = y // gap
        col = x // gap
        return row, col

    def add_robot(self, node, grid):
        """creates a Robot at given Node and adds to environment"""
        if len(self.robots) < self.settings.robot_pack_size:
            robot = Robot(node, self.settings)
            self.visited.append(node)
            self.robots.append(robot)
            for neighbor in node.get_neighbors(grid):
                if neighbor is not None:
                    neighbor.set_frontier()
                    self.frontier.append(neighbor)

    def add_base_station(self, node):
        """creates a BaseStation at given Node and adds to environment"""
        base_station = BaseStation(node, self.settings)
        self.visited.append(node)
        for neighbor in node.get_neighbors(self.grid):
            neighbor.set_frontier()
            self.frontier.append(neighbor)
        self.base_station = base_station

    def add_obstacle(self, node):
        """Add obstacle to list of obstacle nodes"""
        print("obstacle added")
        self.obstacles.append(node)
        self.grid[node.row][node.col].set_obstacle()

    def update_frontier(self, grid):
        """scans the grid and updates appropriate visited nodes
        to be frontier"""

        for current in self.visited:
            # make sure frontier doesn't hold any nodes that have already been visited
            if current in self.frontier:
                self.frontier.remove(current)
            neighbors = current.get_neighbors(grid)
            for neighbor in neighbors:
                if neighbor is not None:
                    if neighbor.is_unexplored():
                        current.set_frontier()
                        self.frontier.append(neighbor)

    def check_comm_status(self):
        """Update status of all robots"""
        for robot in self.robots:
            # clear linked
            robot.linked.clear()
            # flag if within base
            if (
                robot.node.crows_distance(self.base_station.node)
                <= self.base_station.range
            ):
                robot.base_flag = True

            # check what other bots are in range
            for other in self.robots:
                # ignore self
                if other == robot:
                    continue
                # add robot buddies in range to 'linked' list
                if other.node.crows_distance(robot.node) <= 2 * robot.range:
                    robot.linked.append(other)

            # check all buddies and if any connected to base, then flag this one as connected
            for buddy in robot.linked:
                if buddy.base_flag:
                    robot.base_flag = True

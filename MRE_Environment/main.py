import sys
import pygame as pg

import algorithm
from MRE_Environment import settings
from environment import Environment
from settings import Settings
import random

"""
The number of robots: 3,4, and 5.
Two types of obstacle patterns of choice (something similar to Assignment 2).
random start locations.
"""


def spawn_three(environment):
    """This function determines behavior for spawning three
    robots and a base station."""
    settings.robot_pack_size = 3
    environment.add_base_station(environment.grid[24][24])
    environment.add_robot(environment.grid[24][25], environment.grid)
    environment.add_robot(environment.grid[23][24], environment.grid)
    environment.add_robot(environment.grid[25][24], environment.grid)
    return True


def spawn_four(environment):
    """This function determines behavior for spawning four
    robots and a base station."""
    settings.robot_pack_size = 4
    environment.add_base_station(environment.grid[24][24])
    environment.add_robot(environment.grid[24][25], environment.grid)
    environment.add_robot(environment.grid[23][24], environment.grid)
    environment.add_robot(environment.grid[25][24], environment.grid)
    environment.add_robot(environment.grid[24][23], environment.grid)
    return True


def spawn_five(environment):
    """This function determines  behavior for spawning five
    robots and a base station."""
    settings.robot_pack_size = 5
    environment.add_base_station(environment.grid[24][24])
    environment.add_robot(environment.grid[24][20], environment.grid)
    environment.add_robot(environment.grid[22][22], environment.grid)
    environment.add_robot(environment.grid[26][22], environment.grid)
    environment.add_robot(environment.grid[22][26], environment.grid)
    environment.add_robot(environment.grid[26][26], environment.grid)
    return True


def spawn_random(environment):
    """This function determines random behavior for spawning
    robots and base station."""
    robot_count = random.randint(3, 5)
    settings.robot_pack_size = robot_count
    environment.add_base_station(environment.grid[24][24])
    banned = [(24, 24)]
    spawned_count = 0

    # try random locations in a 10 tile radius of base station
    while spawned_count <= robot_count:
        x = random.randint(14, 34)
        y = random.randint(14, 34)
        if (x, y) not in banned:
            banned.append((x, y))
            environment.add_robot(environment.grid[x][y], environment.grid)
            spawned_count += 1
    return True


def live_update_search(environment, algorithm, settings):
    """This function calls the provided search algorithm and provides live
    updates to visualization on each iteration"""
    for i in range(settings.search_max):
        algorithm.generate_population(environment, settings)
        environment.update_frontier(environment.grid)
        environment.draw_env(environment.screen, settings.grid_rows, settings.grid_width)
        pg.display.update()


def main():
    """Contains the primary loop for visualization"""
    my_settings = Settings()
    environment = Environment(my_settings)
    grid = environment.grid
    spawned = False

    # primary game loop
    while True:
        environment.draw_env(environment.screen, my_settings.grid_rows, my_settings.grid_width)

        # define exit behavior
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

            # Keyboard events
            elif event.type == pg.KEYDOWN:

                # Define spacebar behavior
                if event.key == pg.K_SPACE:
                    if not spawned:
                        # default spawn
                        spawned = spawn_three(environment)

                    # run algorithm and update display
                    else:
                        live_update_search(environment, algorithm, my_settings)
                elif event.key == pg.K_3:
                    spawned = spawn_three(environment)
                elif event.key == pg.K_4:
                    spawned = spawn_four(environment)
                elif event.key == pg.K_5:
                    spawned = spawn_five(environment)
                elif event.key == pg.K_r:
                    spawned = spawn_random(environment)

            # Mouse presses
            if pg.mouse.get_pressed()[0]: # mouse1
                pos = pg.mouse.get_pos()
                row, col = environment.get_clicked_grid(pos, my_settings.grid_rows, my_settings.grid_width)
                clicked = grid[row][col]

                # change to base station and add to environment
                if environment.base_station is None:
                    environment.add_base_station(clicked)
                    spawned = True

                # attempt to place robot
                elif len(environment.robots) < my_settings.robot_pack_size and\
                        (clicked.is_unexplored() or clicked.is_frontier()):
                    # add new robot to environment
                    environment.add_robot(clicked, grid)

                # else make obstacle
                elif clicked.is_unexplored() or clicked.is_frontier():
                    environment.add_obstacle(clicked)
                    if clicked in environment.frontier:
                        environment.frontier.remove(clicked)

            elif pg.mouse.get_pressed()[2]:  # mouse2
                pos = pg.mouse.get_pos()
                row, col = environment.get_clicked_grid(pos, my_settings.grid_rows, my_settings.grid_width)
                clicked = grid[row][col]

                # reset node
                clicked.set_unexplored()
        # constantly update screen
        pg.display.update()


if __name__ == '__main__':
    pg.init()
    main()



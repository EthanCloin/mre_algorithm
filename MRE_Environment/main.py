import sys
import pygame as pg

import algorithm
from environment import Environment
from settings import Settings
from node import Node
from robot import Robot
import random


def default_spawn(environment):
    """This function determines default behavior for spawning
    robots and base station."""
    environment.add_base_station(environment.grid[24][24])
    environment.add_robot(environment.grid[24][25], environment.grid)
    environment.add_robot(environment.grid[23][24], environment.grid)
    environment.add_robot(environment.grid[25][24], environment.grid)
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
    settings = Settings()
    environment = Environment(settings)
    grid = environment.grid
    spawned = False

    # primary game loop
    while True:
        environment.draw_env(environment.screen, settings.grid_rows, settings.grid_width)

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
                        spawned = default_spawn(environment)

                    # run algorithm and update display
                    else:
                        live_update_search(environment, algorithm, settings)
                elif event.key == pg.K_7:
                    environment.check_comm_status()

            # Mouse presses
            if pg.mouse.get_pressed()[0]: # mouse1
                pos = pg.mouse.get_pos()
                row, col = environment.get_clicked_grid(pos, settings.grid_rows, settings.grid_width)
                clicked = grid[row][col]

                # change to base station and add to environment
                if environment.base_station is None:
                    environment.add_base_station(clicked)
                    spawned = True

                # attempt to place robot
                elif len(environment.robots) < settings.robot_pack_size and\
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
                row, col = environment.get_clicked_grid(pos, settings.grid_rows, settings.grid_width)
                clicked = grid[row][col]

                # reset node
                clicked.set_unexplored()
        # constantly update screen
        pg.display.update()


if __name__ == '__main__':
    pg.init()
    main()



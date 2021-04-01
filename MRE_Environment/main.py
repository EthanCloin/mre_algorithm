import sys
import pygame as pg

import algorithm
from environment import Environment
from settings import Settings
from node import Node
from robot import Robot


def main():
    settings = Settings()
    environment = Environment(settings)
    grid = environment.grid

    # primary game loop
    running = True
    while running:
        environment.draw_env(environment.screen, settings.grid_rows, settings.grid_width)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                pg.quit()
                sys.exit()

            # Keyboard events
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_w:
                    environment.robots[0].move_north(grid)
                elif event.key == pg.K_s:
                    environment.robots[0].move_south(grid)
                elif event.key == pg.K_d:
                    environment.robots[0].move_east(grid)
                elif event.key == pg.K_a:
                    environment.robots[0].move_west(grid)
                elif event.key == pg.K_q:
                    environment.robots[0].move_northwest(grid)
                elif event.key == pg.K_e:
                    environment.robots[0].move_northeast(grid)
                elif event.key == pg.K_z:
                    environment.robots[0].move_southwest(grid)
                elif event.key == pg.K_c:
                    environment.robots[0].move_southeast(grid)
                elif event.key == pg.K_o:
                    environment.robots[0].move_to(grid, grid[0][0])
                elif event.key == pg.K_r:
                    rando = environment.robots[0].get_random_neighbor(grid)
                    environment.robots[0].move_to(environment, rando)
                # execute algorithm
                elif event.key == pg.K_SPACE:
                    algorithm.generate_population(environment, environment.settings)
                # test methods
                elif event.key == pg.K_7:
                    test_comms = [
                        environment.robots[0].node,
                        environment.robots[1].node,
                        environment.robots[2].node,
                    ]
                    for test in test_comms:
                        print(test.can_communicate(environment.robots, environment.base_station))
                # see robot node status
                elif event.key == pg.K_8:
                    print(environment.robots[0].node.to_string())
                    print(environment.robots[1].node.to_string())
                    print(environment.robots[2].node.to_string())
                # test crows distance
                elif event.key == pg.K_9:
                    print(environment.robots[0].node.crows_distance(environment.base_station.node))
                environment.update_frontier(grid)

            # Mouse presses
            if pg.mouse.get_pressed()[0]: # mouse1
                pos = pg.mouse.get_pos()
                row, col = environment.get_clicked_grid(pos, settings.grid_rows, settings.grid_width)
                clicked = grid[row][col]

                # change to base station and add to environment
                if environment.base_station is None:
                    clicked.set_visited()
                    clicked.set_base_station()
                    environment.add_base_station(clicked)

                # check if all robots are placed
                elif len(environment.robots) < Robot.pack_size and (clicked.is_unexplored() or clicked.is_frontier()):
                    # add new robot to environment
                    environment.add_robot(clicked, grid)

                # else make obstacle
                elif clicked.is_unexplored() or clicked.is_frontier():
                    clicked.set_obstacle()
                    environment.add_obstacle(clicked)
                    if clicked in environment.frontier:
                        environment.frontier.remove(clicked)

            elif pg.mouse.get_pressed()[2]: # mouse2
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

"""
Next to develop
Add checks on leaving radius of base station
Add checks on leaving radius of communication with pack
Add checks on robots occupying same node  
"""

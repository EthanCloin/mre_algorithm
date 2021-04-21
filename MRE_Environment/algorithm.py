import node
import time
import pygame as pg


def generate_population(environment, settings):
    """This function executes a number of searches to generate a number of populations
    and (for now) moves robots to the generated configurations within the population
    Calls the utility function to decide which moves to make"""
    time.sleep(.01)
    population = []
    for pop in range(settings.pop_max):
        config = []
        for robot in environment.robots:
            # randomly choose a valid direction to move
            config.append(robot.get_random_neighbor(environment.grid))

        # add configuration to population
        population.append(config)

    # select most fit configuration
    best = get_fittest(environment, population)

    index = 0
    for robot in environment.robots:
        environment.robots[index].move_to(environment, best[index])
        index += 1

    return "success"


def get_fittest(environment, population):
    """Returns the fittest population (3 nodes in list)"""
    # prepare best_values
    best_utility = -999999
    best_config = None

    for config in population:

        utility = calculate_utility(config, environment)

        # for robot_pos in config:
        #     if robot_pos is not None:
        #         # add distances to nearest frontier in each config to utility value
        #         nearest_frontier = robot_pos.find_nearest_frontier(environment)
        #         utility = calculate_utility(robot_pos, environment)

        if utility > best_utility:
            best_utility = utility
            best_config = config
    return best_config


def calculate_utility(configuration, environment):
    """Given a configuration, calculate the utility, based on
         impossiblity (obstacle/shared node/boundary), loss of
         communication (maintain overlapping radii), and distance
         to nearest frontier node"""

    utility = 0

    can_communicate = False
    impossible = False
    comm_check_count = 0

    for pos in configuration:
        if pos is None:
            return -999999*3
        # check whether position in config would be impossible
        if pos.is_obstacle():
            utility -= 99999
            impossible = True
        elif pos.is_robot():
            utility -= 99999
            impossible = True
        elif pos.is_base_station():
            utility -= 99999
            impossible = True

        # check whether communication is lost (once)
        if comm_check_count == 0:
            dummy_node = pos
            can_communicate = dummy_node.config_can_communicate(configuration, environment)
            comm_check_count += 1

        if not can_communicate:
            utility -= 99999

        # if not pos.can_communicate(environment.robots, environment.base_station):
        #     utility -= 99999
        #     comm_loss = False
        # else:
        #     comm_loss = True

        if not impossible and can_communicate:
            # check distance to nearest frontier node
            nearest = pos.get_nearest_frontier(environment.frontier)
            utility -= nearest[0]

    return utility


# def calculate_utility(configuration, environment):
#     """Given a configuration, calculate the utility, based on
#         impossiblity (obstacle/shared node/boundary), loss of
#         communication (maintain overlapping radii), and distance
#         to nearest frontier node"""
#
#     """
#     Instead of -3, use largest negative value instead.
#     """
#     # note: manhattan distance / 12 =~ nodes to travel
#     utility = 0
#     for position in configuration:
#         # check for impossibility
#         impossible = False
#         comm_loss = False
#         if position.is_obstacle() or position.is_robot() or position.is_base_station():
#             impossible = True
#
#         # check distances to robots
#         distances =[]
#         for robot in environment.robots:
#             distances.append(position.manhattan_distance(robot.node) )
#         """
#         library "graphstream" use fxn "connected component"
#         create temporary graph with cur_locations as nodes
#         two nodes will share an edge if in communication
#
#         using function, check whether that graph is connected
#         if number of connected components in graph >> 1, then not connected
#         use that to decide
#
#
#         """
#
#         # check distance to base
#         distances.append(position.manhattan_distance(environment.base_station.node))
#
#         # sort ascending
#         distances = sorted(distances)
#         closest = distances[1]  # ignoring closest, since that is itself
#         distance_to_range = closest - environment.settings.robot_range
#         if distance_to_range - environment.settings.robot_range > environment.settings.robot_range:
#             comm_loss = True
#
#         print("IMPOSSIBLE?: ", impossible)
#         print("COMMS FAIL?: ", comm_loss)
#
#         if impossible:
#             utility -= 36
#         if comm_loss:
#             utility -= 36
#         if not impossible and not comm_loss:
#             utility -= position.manhattan_distance(position.find_nearest_frontier(environment))
#             print(position.manhattan_distance(position.find_nearest_frontier(environment)))
#     print("UTILITY: ", utility)
#     return utility

"""
Currently this somewhat functions but it is unpredictable at boundaries
I would like to see where I am miscalculating to have such a margin of error, it seems like a 
2 node discrepancy at least

For now, move on to using this as the utility, since it should still provide decent results
... it did not work out, consider restart/redesign 
"""






            # check distance from each frontier cell to current location

            # add the least distance to population total

            # pick the population with lowest total


    #





import time


def generate_population(environment, settings):
    """This function executes a number of searches to generate a number of populations
    and (for now) moves robots to the generated configurations within the population
    Calls the utility function to decide which moves to make"""
    time.sleep(settings.wait_time)
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
            return -999999 * 3
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
            can_communicate = dummy_node.config_can_communicate(
                configuration, environment
            )
            comm_check_count += 1

        if not can_communicate:
            utility -= 99999

        if not impossible and can_communicate:
            # check distance to nearest frontier node
            nearest = pos.get_nearest_frontier(environment.frontier)
            utility -= nearest[0]

    return utility

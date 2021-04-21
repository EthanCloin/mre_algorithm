# mre_algorithm
Implementation of a Multi Robot Exploration algorithm

## Demo Instructions:

This visualization can be controlled using simpley keyboard and mouse
inputs to run the requested variations of the MRE search. Upon compilation
a pygame window containing a 50x50 grid appears. User can interact with this
grid in the following ways:

### Spawning the Robots
#### Spawn Three Robots:
Press the '3' key on your keyboard (not numpad) to spawn 3 robots and a base
station. These robots have a pre-defined position near the base station. 
Pressing the spacebar also defaults to spawning 3 robots.

#### Spawn Four Robots:
Press the '4' key on your keyboard (not numpad) to spawn 4 robots and a base
station. These robots have a pre-defined position near the base station.

#### Spawn Five Robots:
Press the '5' key on your keyboard (not numpad) to spawn 5 robots and a base
station. These robots have a pre-defined position near the base station.

#### Spawn Random Robots:
Press the 'r' key on your keyboard to spawn 3-5 robots and a base
station. These robots will spawn in random locations within a 10 tile 
radius of the base station.

### Placing Obstacles
Use the mouse to click and drag the nodes that you wish to become obstacles.
Right click on any obstacle you wish to reset as an unexplored node. Beware
that the robots can move diagonally, and may surprise you by moving past a 
single-layered diagonal wall.

### Executing the Search
Press the spacebar to execute the searching algorithm. Currently, the algorithm
is set to run for 500 iterations with a .01s sleep between each. These values can be
adjusted by changing the "search_max" or "wait_time" variables in settings.py, respectively.

## Purpose
Implement a searching algorithm with multiple agents maintaining communication with a base station. Agents each have a max communication range, and they can use each other to stay in contact with the base. Final project for Introduction to Artificial Intelligence course. 

## Example
<img src="https://drive.google.com/uc?export=view&id=1BpVijoJPtmE_ZM4Z0azj_ES0mHNoPCSz" 
width="600" height="600"/>

## Setup Instructions:
Clone this repo and run `pip install pygame` or `pip install -r requirements.txt`

You can run the simulation by executing `main.py`

Follow the below instructions to draw obstacles, spawn robots, and watch them explore
their environment, while maintaining communication distance!

## Demo Instructions:

This visualization can be controlled using simply keyboard and mouse
inputs to run the requested variations of the MRE search. Upon compilation
a pygame window containing a 50x50 grid appears. User can interact with this
grid in the following ways:

### Placing Obstacles
  Use the mouse to click and drag the nodes that you wish to become obstacles.
  Right click on any obstacle you wish to reset as an unexplored node. Beware
  that the robots can move diagonally, and may surprise you by moving past a 
  single-layered diagonal wall.

### Spawning the Robots
#### Spawn Specific Robot Count:
  Press '3', '4', or '5' on your keyboard to spawn the respective number of robots. These will 
    always spawn in the same position surrounding the base station.

#### Spawn Random Robots:
  Press the 'r' key on your keyboard to spawn 3-5 robots and a base
  station. These robots will spawn in random locations within a 10 tile 
  radius of the base station.

- ### Executing the Search
  Press the spacebar to execute the searching algorithm. Currently, the algorithm
  is set to run for 500 iterations with a .01s sleep between each. These values can be
  adjusted by changing the *"search_max"* or *"wait_time"* variables in settings.py, respectively.

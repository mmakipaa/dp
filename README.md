
# Basic Dynamic Programming Algorithms

This repository contains Jupyter notebooks illustrating basic Dynamic Programming (DP) algorithms using a simple maze or grid-world as an environment.


## Value Iteration

A notebook illustrating Value Iteration algorithm. In addition. the notebook also covers some background of dynamic programming, briefly discussing for example Markov Decision Processes, policies and value functions.

[maze_value_iteration.ipynb](https://github.com/mmakipaa/dp/blob/main/notebooks/maze_value_iteration.ipynb)

## Policy Iteration

A notebook illustrating Policy Iteration

[maze_policy_iteration.ipynb](https://github.com/mmakipaa/dp/blob/main/notebooks/maze_policy_iteration.ipynb)

## Basic Maze

A notebook containing the implementation for a basic maze, as well as utility functions for visualizing the maze. The implementation is imported by the notebooks above

[maze_basis.ipynb](https://github.com/mmakipaa/dp/blob/main/notebooks/maze_basis.ipynb)

In addition to Jupyter notebooks, html versions of the notebooks rendered using [nbconvert](https://github.com/jupyter/nbconvert) can be found in [html](html) folder. These pre-rendered versions use a slightly larger font and fix an issue when applying styling span elements within markdown cells. Also deep linking between notebooks works when html files are located in same directory. Unfortunately, nbconvert adds almost 14000 lines of style defintions and Github 'can’t show files that are this big right now'.
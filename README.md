
# Basic Dynamic Programming Algorithms

This repository contains Jupyter notebooks illustrating basic Dynamic Programming (DP) algorithms using a simple maze or grid-world as an environment.

## Value Iteration

A notebook illustrating value iteration algorithm. In addition. the notebook also covers some background of dynamic programming, briefly discussing for example Markov Decision Processes, policies and value functions.

[maze_value_iteration.ipynb](notebooks/maze_value_iteration.ipynb)

## Policy Iteration

A notebook illustrating policy iteration algorithm

[maze_policy_iteration.ipynb](notebooks/maze_policy_iteration.ipynb)

## Basic Maze

A notebook implementing a basic maze, as well as utility functions for visualizing the maze. The implementation is imported by the above notebooks.

[maze_basis.ipynb](notebooks/maze_basis.ipynb)

## HTML versions

In addition to Jupyter notebooks in _.ipynb_ format, HTML versions of the notebooks generated using [nbconvert](https://github.com/jupyter/nbconvert) can be found in [html](html) folder. These pre-rendered versions use a slightly larger font and fix an issue when using styling \<span\> elements within markdown cells. Also deep linking between notebooks works. 

GitHub does not currently support rendering of HTML files. So, to view the pre-rendered notebooks, navigate to [Github pages](https://mmakipaa.github.io/dp/) side of this project and follow the links there.

Alternatively, the notebooks can be viewed in <notebooks> folder using the renderer provided by GitHub, with above limitations by using the links above.
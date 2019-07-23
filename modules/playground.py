#! /usr/bin/env python3
# coding: utf-8

"""
Amelie game playground
"""

from modules.mazes import *
from settings import *

from random import sample, choice


class Playground:
    """ Class for extracting and storing the abscissa coordinates
     of each motionless element whether by structure or randomly. """

    def __init__(self):
        # Pick a maze in mazes file
        self.maze_on = choice(maze_list)
        self.paths = []     # Initialize the container for the paths x values
        # Create list of randomized obj img to be loaded
        self.obj_img = sample(obj, G)
        # Initialize the container for the obj x-axis coordinates
        self.obj_x = []

        for line in self.maze_on:
            i = 0
            paths_x = []
            for col in line:
                if col == START:
                    self.start = i  # Store the start x-axis coordinate
                # Store the paths x-axis coordinates individually
                if col == PATH:
                    paths_x.append(i)
                i += 1
            # Store the coordinates in lists, one for each line
            self.paths.append(paths_x)

    def random_obj(self):
        """ Method for randomizing and storing
        the x-axis coordinates of the objects. """
        for i in range(N):
            # Pick a value for each list in the paths list and store it
            self.obj_x.append(choice(self.paths[i]))

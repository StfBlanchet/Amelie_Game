#! /usr/bin/env python3
# coding: utf-8

"""
Amelie game player methods
"""

from modules.playground import *


class Player:
    """ Manage the player's positions, movements and results. """

    def __init__(self, coord):
        self.coord = coord  # Declare attribute for callable maze
        self.maze = coord.maze_on  # Call the maze for searchable strings
        # Call the start x value extracted by playground method
        self.x = coord.start
        self.y = 0  # Set the start y value
        self.pos_x = self.x * CELL  # Convert the player's position to pixels
        self.pos_y = self.y * CELL
        self.hits = []  # Initialize the container for the player's hits

    def move_right(self):
        """ Method for moving right. """
        # Going right involves moving forward on the abscissa axis
        right = self.x + 1
        # Stay inside the screen by limiting the maximum value of x to n cells
        if right < N:
            # Check that the new position does not match a wall
            if self.maze[self.y][right] != WALL:
                self.x = right  # Update the player x-axis coordinate
                self.pos_x += CELL   # Move one cell

    def move_left(self):
        """ Method for moving left. """
        # Going left involves moving backward on the abscissa axis
        left = self.x - 1
        if left >= 0:  # Stay inside the screen by banning any negative x value
            if self.maze[self.y][left] != WALL:
                self.x = left
                self.pos_x -= CELL

    def move_up(self):
        """ Method for moving up. """
        # Going up involves moving backward on the ordinate axis
        up = self.y - 1
        if up >= 0:
            if self.maze[up][self.x] != WALL:
                self.y = up
                self.pos_y -= CELL

    def move_down(self):
        """ Method for moving down. """
        # Going down involves moving forward on the ordinate axis
        down = self.y + 1
        if down < N:
            if self.maze[down][self.x] != WALL:
                self.y = down
                self.pos_y += CELL

    def hit(self):
        """ Method for incrementing the hit counter
        each time the player moves over an object
         and repositioning the object grabbed. """
        # Query the object x-axis values according to the player y-axis value
        if self.x == self.coord.obj_x[self.y]:
            # Add 1 each time the player's position matches an object
            self.hits.append(1)
            # Place the object grabbed in the counter bar, to the 16th col
            self.coord.obj_x[self.y] = 15

    def results(self):
        """ Method for defining each possible outcome. """
        # The player has not grabbed all the objects
        if len(self.hits) < G and self.maze[self.y][self.x] != ARRIVAL:
            # and has not reached the arrival point
            return 0
        if len(self.hits) < G and self.maze[self.y][self.x] == ARRIVAL:
            # but has reached the arrival point
            return 1
        # The player has grabbed all the objects
        if len(self.hits) == G and self.maze[self.y][self.x] != ARRIVAL:
            # but has not reached the arrival point
            return 2
        if len(self.hits) == G and self.maze[self.y][self.x] == ARRIVAL:
            # and has reached the arrival point
            return 3

#! /usr/bin/env python3
# coding: utf-8

"""
The Amelie's trip game
released under MIT License
by Stephanie BLANCHET stephanie.blanchet.it@gmail.com

In this version of the game, the player has to grab random items
in a labyrinth and reach the finish point in a limited time.

Python 3.7 script
files: mazes.py, playground.py, player.py, settings.py, materials
"""

from sys import exit

import pygame
from pygame.locals import *

from modules.player import *
from modules.playground import *

pygame.init()


def main():

    # Window elements
    win = pygame.display.set_mode(((matrix + side_bar), matrix))
    counter_bar = pygame.Rect((matrix, 0), (CELL, matrix))
    icon = pygame.image.load(icon_img).convert_alpha()
    pygame.display.set_icon(icon)
    pygame.display.set_caption(title)

    # Font elements
    font_small = pygame.font.Font(font_family, small)
    font_medium = pygame.font.Font(font_family, medium)
    font_large = pygame.font.Font(font_family, large)

    # Welcome elements
    welcome = pygame.image.load(welcome_img).convert_alpha()
    intro = font_large.render(intro_msg, 1, font_color)
    instruction_1 = font_small.render(instruction1, 1, font_color)
    instruction_2 = font_small.render(instruction2, 1, font_color)

    # Mobile element
    player = pygame.image.load(player_img).convert_alpha()

    # Motionless elements
    arrival = pygame.image.load(arrival_img).convert_alpha()
    wall = pygame.image.load(wall_img).convert_alpha()

    # Outcome event elements
    won = pygame.image.load(won_img).convert_alpha()
    big_lover = pygame.image.load(lover_img).convert_alpha()
    lost = pygame.image.load(lost_img).convert_alpha()
    fatal = pygame.image.load(fatal_img).convert_alpha()
    happy = font_large.render(happy_text, 1, font_color)
    sad = font_medium.render(sad_text, 1, font_color)
    pity = font_medium.render(pity_text, 1, font_color)
    over = font_large.render(fatal_text, 1, font_color)

    # Class instances
    play = Playground()
    amelie = Player(play)

    def build():
        """ Function to build the playground
        i.e. display each motionless element,
        according to the structure of the maze. """
        j = 0
        for line in play.maze_on:
            i = 0
            for sprite in line:
                # Convert wall positions to pixels
                x = i * CELL
                y = j * CELL
                # for random obj, y values = i
                # x values are given according to i
                # PAD adds a slight padding for obj vertical centering
                w = (i * CELL) + PAD    # y
                z = (play.obj_x[i] * CELL) + PAD    # x
                if sprite == PATH:
                    # Load the given objects in the object list following y (i)
                    objects = \
                        pygame.image.load(play.obj_img[i]).convert_alpha()
                    win.blit(objects, (z, w))
                elif sprite == WALL:
                    win.blit(wall, (x, y))
                elif sprite == ARRIVAL:
                    win.blit(arrival, (x, y))
                i += 1
            j += 1

    def countdown():
        """ Function to generate and display the countdown
        as a decreasing sidebar. """
        time_left = time_limit - (pygame.time.get_ticks() - start_time)
        timer_height = int(time_left / (time_limit / matrix))
        if time_left >= 0:
            pygame.draw.rect(win, timer_color,
                             ((matrix + CELL), 0, timer_width, timer_height))
            pygame.display.update()

        return time_left

    def outcome():
        """ Function for generating the outcome displays
        according to time, arrival and hit variables. """
        timer = countdown()
        # In case the player has not reached the point of arrival on time
        if timer < 0:
            # and has not grab all the objects
            if amelie.results() == 0:
                win.fill(bg)
                win.blit(fatal, (155, 100))
                win.blit(over, (320, 600))
            # but has grabbed all the objects
            if amelie.results() == 2:
                win.fill(bg)
                win.blit(lost, (210, 150))
                win.blit(pity, (240, 550))
        # In case the player has reached the point of arrival on time
        elif timer > 0:
            # but has not grabbed all the objects
            if amelie.results() == 1:
                win.fill(bg)
                win.blit(lost, (210, 150))
                win.blit(sad, (160, 550))
            # and has grabbed all the objects
            elif amelie.results() == 3:
                win.fill(bg)
                win.blit(won, (0, 0))
                win.blit(icon, (170, 470))
                win.blit(big_lover, (240, 452))
                win.blit(happy, (285, 590))

    # Main loop
    run = True
    while run:
        welcome_on = True
        game_on = False

        # Display the welcome screen elements
        win.fill(bg)
        win.blit(welcome, (50, 0))
        win.blit(intro, (120, 610))
        win.blit(instruction_1, (120, 660))
        win.blit(instruction_2, (120, 685))
        pygame.display.flip()

        # Define actions in welcome loop
        while welcome_on:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                elif event.type == KEYDOWN:
                    if event.key == K_SPACE:
                        welcome_on = False
                        # Launch screen game
                        game_on = True
                        # Launch start time and countdown
                        start_time = pygame.time.get_ticks()
                        countdown()

        # Game loop
        while game_on:

            # Set the loop speed limitation
            pygame.time.Clock().tick(60)

            # Display the playground screen elements
            win.fill(bg)
            win.fill(counter_color, counter_bar)
            play.random_obj()
            build()
            win.blit(player, (amelie.pos_x, amelie.pos_y))
            amelie.hit()
            outcome()
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                elif event.type == KEYDOWN:
                    if event.key == K_SPACE:
                        game_on = False
                        main()
                    if event.key == K_DOWN:
                        amelie.move_down()
                    if event.key == K_UP:
                        amelie.move_up()
                    if event.key == K_RIGHT:
                        amelie.move_right()
                    if event.key == K_LEFT:
                        amelie.move_left()


if __name__ == "__main__":
    main()

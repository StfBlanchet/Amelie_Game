#! /usr/bin/env python3
# coding: utf-8

"""
Amelie game settings
"""

# Shared screen settings
N = 15      # number of cells
CELL = 50   # cell size consistent with wall and player img dimensions = 48*48
ELT_SIZE = 48
matrix = N * CELL
side_bar = CELL + (CELL // 2)
icon_img = 'materials/Amelie_75x75.png'
bg = (31, 97, 141)  # window background color
title = 'Help Amelie to grab all the objects and join her lover!'

# font
font_color = (234, 236, 238)
font_family = 'materials/avenir.otf'
x_small = 14
small = 18
medium = 26
large = 36

# Welcome screen
welcome_img = 'materials/Amelie_640x640.png'
intro_msg = "Welcome to Amelie's trip!"
instruction1 = \
    'Help Amelie to grab all the objects and join her lover in 45 seconds.'
instruction2 = 'Ready? Press the SPACE KEY to start.'

# Game screen
counter_color = (234, 236, 238)  # counter bar background color

player_img = 'materials/Amelie_48x48.png'
wall_img = 'materials/arch.png'
arrival_img = 'materials/TheLover_48x48.png'

# Time limit in milliseconds
time_limit = 46000
timer_color = (180, 0, 0)
timer_width = CELL / 2

# Outcome events
won_img = 'materials/win.png'
lost_img = 'materials/lost.png'
lover_img = 'materials/TheLover_96x96.png'
fatal_img = 'materials/fatal.png'
happy_text = 'Congratulations!'
sad_text = 'Too bad, Amelie did not grab all the objects.'
pity_text = 'Pity! Amelie was almost there...'
fatal_text = 'Time over!'

# Loop for generating the object images list
# Of note: objects dimensions = 32*32
# Icons provided by https://www.icons8.com under free license.
OBJ_SIZE = 32
PAD = (ELT_SIZE - OBJ_SIZE) / 2
G = 15  # number of objects
obj = []
img = 'materials/obj'
for i in range(G):
    obj.append(img + str(i) + '.png')

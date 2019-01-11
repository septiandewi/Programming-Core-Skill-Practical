# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 18:14:15 2019

@author: pprt
"""
import numpy as np
import matplotlib
#==============================================================================
# Define the Matrix for making the city map
#==============================================================================
# define the size of the array
drunk_plan = np.zeros([300, 300])
#define size each bulidings
size = range(0, 20)
#define location and build up the pubs (there are  3 pubs)
for i in size:
    for j in size:
        drunk_plan[269+i, 39+j] = 260
        drunk_plan[269+i, 139+j] = 260
        drunk_plan[269+i, 239+j] = 260
#define location and build up the houses (there are  25 houses) with different numbers    
for i in size:
    for j in size:
        drunk_plan[23+i, 39+j] = 250
        drunk_plan[23+i, 79+j] = 240
        drunk_plan[23+i, 119+j] = 230
        drunk_plan[23+i, 159+j] = 220
        drunk_plan[23+i, 199+j] = 210
        drunk_plan[23+i, 239+j] = 200
        drunk_plan[63+i, 59+j] = 190
        drunk_plan[63+i, 99+j] = 180
        drunk_plan[63+i, 139+j] = 170
        drunk_plan[63+i, 179+j] = 160
        drunk_plan[63+i, 219+j] = 150
        drunk_plan[103+i, 39+j] = 140
        drunk_plan[103+i, 79+j] = 130
        drunk_plan[103+i, 119+j] = 120
        drunk_plan[103+i, 159+j] = 110
        drunk_plan[103+i, 199+j] = 100
        drunk_plan[103+i, 239+j] = 90
        drunk_plan[143+i, 59+j] = 80
        drunk_plan[143+i, 99+j] = 70
        drunk_plan[143+i, 139+j] = 60
        drunk_plan[143+i, 179+j] = 50
        drunk_plan[143+i, 219+j] = 40
        drunk_plan[183+i, 39+j] = 30
        drunk_plan[183+i, 139+j] = 20
        drunk_plan[183+i, 239+j] = 10
       
#for checking result of the map
matplotlib.pyplot.imshow(drunk_plan)
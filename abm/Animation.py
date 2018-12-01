# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 00:25:33 2018

@author: Septian Dewi Cahyani

_Version_ 1.0.0
"""
#==================================
#Import Function
#==================================
import csv
import matplotlib
import agentframework
import matplotlib.animation

#==================================
#Define the Environment
#==================================

#Import file contain environment
f = open("in.txt")
data = []
for line in f:
    parsed_line = str.split(line,",")
    data_line = []
    for word in parsed_line:
        data_line.append(float(word))
    data.append(data_line)
#print(data)
f.close()

fig = matplotlib.pyplot.figure(figsize=(7, 7)) #define the window size of animation

#Make container for environment
environment = []   


#open csv data (raster) using csv.reader
f = open('in.txt', newline='') 
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
for row in reader:	# A list of rows
    rowlist = []
    environment.append(rowlist)
    for value in row:	# A list of value
        #print(value) # Floats
        rowlist.append(value)
#f.close() # Don't close until you are done with the reader;
        # the data is read on request.

#plot the environment(for checking)
matplotlib.pyplot.imshow(environment)
matplotlib.pyplot.show()   

#=======================================================================
#Making the agents, connect it with environment and make their activity
#=======================================================================
num_of_agents = 10 #number of agents will be created
num_of_iterations = 10 #number of agent's interation
neighbourhood = 20 #number of limitation distance to each agent to reach another agent
agents = [] #make container for agents
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment,agents))#put agents in evironment
    
def update(frame_number): #make definition of frame number in animation
    
    fig.clear()   
    
    for i in range(num_of_agents):
        agents[i].move() #load code from agentframework that makes agent move
        agents[i].eat() ##load code from agentframework that makes agent eat
        agents[i].share_with_neighbours(neighbourhood) #load code from agentframework that  share food with neighbour

#=================================================
#Making agent's activity animation
#=================================================     
   
    matplotlib.pyplot.xlim(00, 299)
    matplotlib.pyplot.ylim(299, 00)
    matplotlib.pyplot.imshow(environment)
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
        
animation = matplotlib.animation.FuncAnimation(fig, update, interval=10)#making animation with unlimited movement    

matplotlib.pyplot.show()

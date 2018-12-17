# agentframework.py
# -*- coding: utf-8 -*-
"""
Last Edited on Tue Dec 11 18:31:53 2018

@author: Septian Dewi Cahyani
"""
import random
class Agent():
#create agents and setting up the environment. it defined the zero position and zero condition 
    def __init__ (self, environment,agents, y, x):
         if (x == None):
           self.x = random.randint(0,100)
         else:
           self.x = x
    
         if (y == None):
           self.y = random.randint(0,100)
         else:
           self.y = y
           
         self.environment = environment
         self.agents = agents
         self.store = 0 # We'll come to this in a second.
#make the agents eat
    def eat(self): # can you make it eat what is left?
        if self.environment[self.y][self.x] > 10: 
            self.environment[self.y][self.x] -= 10
            self.store += 10 #number of each agent food 
#make the agents move 
    def move(self):        
        if random.random() < 0.5:
            self.y = (self.y + 1) % 100
        else:
            self.y = (self.y - 1) % 100
        if random.random() < 0.5:
            self.x = (self.x + 1) % 100
        else:
            self.x = (self.x - 1) % 100
#interact with neighbors.
    def share_with_neighbours(self, neighbourhood):
        for agent in self.agents:
            dist = self.distance_between(agent) 
            if dist <= neighbourhood:
                total = self.store + agent.store
                ave = total /2 #food between two agents that interact divided by two
                self.store = ave
                agent.store = ave
                #print("sharing " + str(dist) + " " + str(ave))

    def distance_between(self, agent):
        return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5




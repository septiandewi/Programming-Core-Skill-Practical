# agentframework.py

import random
class Agent():
#create agents and setting up the environment. it defined the zero position and zero condition (model 20 november)
    def __init__ (self, environment,agents, y, x):
         if (x == None):
           self.x = random.randint(0,100)
         else:
           self.x = x
    
         if (y == None):
           self.y = random.randint(0,100)
         else:
           self.y = x
           
         self.environment = environment
         self.agents = agents
         self.store = 0 # We'll come to this in a second.
#make the agents eat (model 20 november)
    def eat(self): # can you make it eat what is left?
        if self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10       
#make the agents move 
    def move(self):        
        if random.random() < 0.5:
            self.y = (self.y + 1) % 300
        else:
            self.y = (self.y - 1) % 300
        if random.random() < 0.5:
            self.x = (self.x + 1) % 300
        else:
            self.x = (self.x - 1) % 300
#interact with neighbors(model 23 nov)
    def share_with_neighbours(self, neighbourhood):
        for agent in self.agents:
            dist = self.distance_between(agent) 
            if dist <= neighbourhood:
                total = self.store + agent.store
                ave = total /2
                self.store = ave
                agent.store = ave
                print("sharing " + str(dist) + " " + str(ave))

    def distance_between(self, agent):
        return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5



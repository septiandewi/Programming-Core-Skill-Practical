

import csv
import matplotlib
import agentframework
import matplotlib.animation


f = open("in.txt")
data = []
for line in f:
    parsed_line = str.split(line,",")
    data_line = []
    for word in parsed_line:
        data_line.append(float(word))
    data.append(data_line)
print(data)
f.close()

fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])

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

#plot the environment
matplotlib.pyplot.imshow(environment)
matplotlib.pyplot.show()   


#making the agents and connect it into the environment
num_of_agents = 10
num_of_iterations = 10
neighbourhood = 20
agents = []
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment,agents))
    
def update(frame_number):
    
    fig.clear()   
#make the agents move-eat-share 
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood)
    #plot the move and eat agents with the environment
    matplotlib.pyplot.xlim(00, 299)
    matplotlib.pyplot.ylim(299, 00)
    #plot the environment
    matplotlib.pyplot.imshow(environment)
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i].x,agents[i].y)

'''
def gen_function(b = [0]):
    a = 0
    global carry_on #Not actually needed as we're not assigning, but clearer
    while (a < 1000) & (carry_on) :
        yield a			# Returns control and waits next call.
        a = a + 1
'''
     
#animation = matplotlib.animation.FuncAnimation(fig, update, interval=1)
#animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
#animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False, interval=3000)
animation = matplotlib.animation.FuncAnimation(fig, update, repeat=False)
#animation = matplotlib.animation.FuncAnimation(fig, update, repeat=False)




'''
def update(frame_number):
    
    fig.clear()   

    for i in range(num_of_agents):
            if random.random() < 0.5:
                agents[i][0]  = (agents[i][0] + 1) % 99 
            else:
                agents[i][0]  = (agents[i][0] - 1) % 99
            
            if random.random() < 0.5:
                agents[i][1]  = (agents[i][1] + 1) % 99 
            else:
                agents[i][1]  = (agents[i][1] - 1) % 99 
        
   
    
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i][0],agents[i][1])
        #print(agents[i][0],agents[i][1])
    print(frame_number)
'''
matplotlib.pyplot.show()
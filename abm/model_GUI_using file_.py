# -*- coding: utf-8 -*-
"""
Last Edited on Tue Dec 11 18:31:53 2018

@author: Septian Dewi Cahyani
"""
import csv
import matplotlib
import agentframework_GUI_file
import matplotlib.animation
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.backends.backend_tkagg
import tkinter
import random
import requests
import bs4

#set the size of the box to use in GUI
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])
#Set the shape for the Environment
environment = []   

#==============================================================================
# open Data For Environment and Agent's Positions
#==============================================================================

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


#open the file that contain agent's Positions from web
r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html') #directory for get the data
content = r.text
soup = bs4.BeautifulSoup(content, 'html.parser')
td_ys = soup.find_all(attrs={"class" : "y"})
td_xs = soup.find_all(attrs={"class" : "x"})
print(td_ys)
print(td_xs)
print(len(td_ys))#print the lenght of the data from data

#==============================================================================
# Define The agents and connect them into the environment
#==============================================================================
#making the agents and connect it into the environment
#num_of_agents = 10 #it can be use when you want call the exact numbers of the 
num_of_agents =len(td_ys) #use all of the agents in the data
num_of_iterations = 10
neighbourhood = 20
agents = []

for i in range(num_of_agents):
     y = int(td_ys[i].text)
     x = int(td_xs[i].text)
     agents.append(agentframework_GUI_file.Agent(environment, agents, y, x))
    
    
carry_on = True

#==============================================================================
# Make the animation that show agent's activity.
#==============================================================================

#define the animation
def update(frame_number):
    global carry_on
    fig.clear()   
    
    #set the axes
    matplotlib.pyplot.xlim(00, 100)
    matplotlib.pyplot.ylim(100, 00)


    #set the condition for the process stop
    if random.random() < 0.01:
        carry_on = False
        print("stopping condition")
        
    #plot the environment to the environment to each mivement
    matplotlib.pyplot.imshow(environment)
        
    #make the agents move-eat-share (define agent's activities)
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood)
    

    # plot the agents
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i].x,agents[i].y)

#set the condition for the animation stop
def gen_function(b = [0]):
    a = 0
    global carry_on #Not actually needed as we're not assigning, but clearer
    while (a < 10) & (carry_on) :
        yield a			# Returns control and waits next call.
        a = a + 1

#define the animation function
def run():
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
    canvas.show()
 
#==============================================================================
# Build the GUI for the model
#==============================================================================
    
    
#build the GUI
root = tkinter.Tk() 
root.wm_title("Model") #set the title for the GUI's model
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
menu_bar = tkinter.Menu(root) #make the menu bar
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)  #define the name of sub-menu
model_menu.add_command(label="Run model", command=run) #define the action of sub-menu

tkinter.mainloop()	# Wait for interactions.



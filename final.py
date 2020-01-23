# -*- coding: utf-8 -*-#

import matplotlib
import matplotlib.pyplot
import agentframework
import csv



#number of agents
num_of_agents = 5000
agents = []

#settings of figure
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])

#the bomb position
startx=starty=75
#height of the building
height=75

# get enviroment
#the map
bacterialmap = []#2D map
with open('./windraster.txt', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')#read file
    for row in spamreader:
        rowlist = []
        for value in row:
            rowlist.append(int(value))
        bacterialmap.append(rowlist)#add one row
#find the start position
for row in range(len(bacterialmap)):
    for column in range(len(bacterialmap[0])):
        if(bacterialmap[row][column]==255):
            bacterialmap[row][column]=0
            startx=column#start x
            starty=row#start y


#inital all agents
for i in range(num_of_agents):
    agents.append(agentframework.Agent(bacterialmap, agents, starty, startx,75))

def run():

    #run 5000
    for i in range(num_of_agents):
        while agents[i].height!=0:#When not reaching the ground
            agents[i].move()
        bacterialmap[agents[i].y][agents[i].x]+=1#reaching the ground
    with open('./result.txt', 'w') as f:#write the map to txt file
        for row in bacterialmap:
            s = str(row).replace('[','').replace(']','')#replace [ and ]
            s = s.replace("'",'') +'\n'  #replace '
            f.write(s)

run()
#draw image
matplotlib.pyplot.imshow(bacterialmap)
matplotlib.pyplot.show()



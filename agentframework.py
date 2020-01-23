# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# File  : agentframework.py
# Author:
# Date  : 2019-11-21 08:27
# Desc  : 
# -------------------------------------------------------------------------------

import random


class Agent:
    def __init__(self, environment, agents,y,x,h):
        self.environment = environment
        self.store = 0
        self.agents = agents
        self.height=h
        if x != None:
            self.x = x
        else:
            self.x = random.randint(0,100)
        if y != None:
            self.y = y
        else:
            self.y = random.randint(0,100)

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def set_store(self,store):
        self.store = store

    def get_store(self):
        return self.store

    def move(self):
        if(self.height==0):#hit ground
            return
        tmp=random.random()
        #which direction to move(east south west north)
        if tmp < 0.05:
            self.x = (self.x - 1) % 300
        else:
            if tmp < 0.80:
                self.x = (self.x + 1) % 300
            else:
                if tmp < 0.90:
                    self.y = (self.y - 1) % 300
                else:
                    self.y = (self.y + 1) % 300
        tmp=random.random()
        #move up or down
        if self.height >= 75:
            if tmp<0.2:
                self.height = self.height + 1
            else:
                if tmp<0.9:
                    self.height = self.height - 1
        else:
            if self.height>0:
                self.height=self.height-1



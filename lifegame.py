# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 15:30:57 2020

@author: keigo
"""

import numpy as np
import random

class LifeGame():
    def __init__(self):
        self.size = 15
        self.white = 30
        self.field = np.zeros((self.size,self.size), dtype = str)
        self.length = 0
        self.width = 0
        self.counter = 0
        self.type = 0
        
    
    def fieldmaker(self):
        for i in range(self.size):
            for j in range(self.size):
                self.field[i,j] = '●'
        for i in range(self.white):
            self.field[random.randint(0,self.size-1),random.randint(0,self.size-1)] = '◯'
    def printfield(self):
        print(self.field)
    
    def checker(self):
        if length == 0 and width == 0:
            self.type = 5
        elif length == 0 and width == size-1:
            self.type = 6
        elif length == size-1 and width == 0:
            self.type = 7
        elif length == size-1 and width == size-1:
            self.type = 8
        elif length == 0 and width != 0 and width != size-1:
            self.type = 1
        elif length == size-1 and width != 0 and width != size-1:
            self.type = 2
        elif width == size-1 and length != 0 and length != size-1:
            self.type = 3
        elif width == 0 and length != 0 and length != size-1:
            self.type = 4
        else:
            self.type = 0

            
    
    def counting_four(self):
        self.counter = 0
        if self.field[self.length+1,self.width] = '◯':
            self.counter += 1
        if self.field[self.length-1,self.width] = '◯':
            self.counter += 1
        if self.field[self.length,self.width+1] = '◯':
            self.counter += 1
        if self.field[self.length,self.width-1] = '◯':
            self.counter += 1
    
    def counting_three(self):
        self.counter = 0
        if self.type = 1:
            if self.field[self.length+1,self.width] = '◯':
            self.counter += 1
            if self.field[self.length,self.width-1] = '◯':
            self.counter += 1
            if self.field[self.length,self.width+1] = '◯':
            self.counter += 1
        if self.type = 2:
            if self.field[self.length-1,self.width] = '◯':
            self.counter += 1
            if self.field[self.length,self.width-1] = '◯':
            self.counter += 1
            if self.field[self.length,self.width+1] = '◯':
            self.counter += 1
        if self.type = 3:
            if self.field[self.length,self.width-1] = '◯':
            self.counter += 1
            if self.field[self.length+1,self.width] = '◯':
            self.counter += 1
            if self.field[self.length-1,self.width] = '◯':
            self.counter += 1
        if self.type = 3:
            if self.field[self.length,self.width+1] = '◯':
            self.counter += 1
            if self.field[self.length+1,self.width] = '◯':
            self.counter += 1
            if self.field[self.length-1,self.width] = '◯':
            self.counter += 1
    
    def counting
lifegame = LifeGame()
lifegame.fieldmaker()
lifegame.printfield()

# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 15:45:42 2015

@author: tim
"""

class Math:
    PI = 3.14159
    
Math.PI

print(Math.__dict__)

Math.__dict__['PI']

m = Math()

m.PI = 3.14

class Some:
    def setx(self, x):
        self.x = x
        

s = Some()
print(Some.__dict__)

print(s.__dict__)

s.setx(10)



class Some:
    def __init__(self, x):
        self.x = x
        
s = Some(1)

class Some:
    w = 10
    def __getattr__(self, name):
        if name == 'w':
            return 20

s = Some()

class Some:
    def __init__(self):
        self.__x = 10
        




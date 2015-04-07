# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 13:36:44 2015

@author: tim
"""

class Some:
    def __init__(self, x):
        self.x = x
        
    def service(self, y):
        print('do service...', self.x + y)

s = Some(10)

s.service(2)          #相等
Some.service(s, 2)    #相等    

s1 = Some(10)
service = s1.service
service(5)

s2 = Some(20)
service = s2.service
service(5)


s1 = Some(10)
Some.service(s1, 5)

s2 = Some(20)
Some.service(s2, 5)

service = Some.service
service(s1, 5)
service(s2, 5)



class Other:
    def service():
        print('do service...')
        
o = Other()
#Other.service()

class Some:
    @staticmethod
    def service(x, y):
        print('do service...', x + y)

Some.service(10,20)

s = Some()
s.service(10, 20)
#s.service(10)

class Some:
    def __init__(self, x):
        self.x = x
        
    def service(self, y):
        print('do service...', self.x + y)
        
class Other:
    pass

o = Other()
o.x = 100
#Some.service(o, 200)

qoo = Some(100)

class Some:
    def __init__(self, x):
        self.x = x
    
    @classmethod
    def service(clz, y):
        print('do service...', clz, y)
s = Some(10)
s.service(20)
Some.service(30)














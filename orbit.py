# -*- coding: utf-8 -*-

import math
import numpy as np
import matplotlib.pyplot as plt

class Orbit:
    inOrbit = []
    
    def __init__(self, name):
        self.name = name
        self.inOrbit.append(name)
        self.status = 0
        self.path = []
        
    def calcOrbit(self, smajor=4000, sminor=0, e=0, steps=50, table='hide', image='hide', summary='hide'):
        self.smajor = smajor
        self.sminor = sminor
        self.eccen = e
        self.steps = steps
        
        # circular orbit - applies parametric equation for orbital motion
        if sminor == 0:
            e = 0
            for a in range(0, self.steps):
                self.angle = a * 2 * math.pi / self.steps
                self.path.append([self.angle, math.cos(self.angle) * smajor, math.sin(self.angle) * smajor])
            
        # elliptical orbit
        else:
            if self.sminor <= self.smajor:
                e = math.sqrt(self.smajor**2 - self.sminor**2)/self.smajor
            else:
                raise Exception('Semimajor axis must be >= semiminor axis.')
                           
        if table == 'show':
            for pa, px, py in self.path:
                print('{0:8.2f}\t{1:8.2f}\t{2:8.2f}'.format(pa, px, py))
            
        if image == 'show':
            
            
        if summary == 'show':
            
            # print orbit details after calculation       
            print('------Orbital Parameters------')
            print('Major Axis:', self.smajor)
            print('Minor Axis:', self.sminor)
            print('Eccentricity:', self.eccen)
            print('Steps:', self.steps)
            
    
    def orbitParameters(self):
        print('------Orbital Parameters------')
        print('Major Axis:', self.major)
        print('Minor Axis:', self.minor)
        print('Eccentricity:', self.eccen)
        print('Steps:', self.steps)
        
    def orbitingObjects(self):
        print('Objects in orbit:')
        print(*self.inOrbit)
            
sat1 = Orbit('123')
sat2 = Orbit('abc')

sat1.calcOrbit(table='show')
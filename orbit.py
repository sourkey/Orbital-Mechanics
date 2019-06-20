# -*- coding: utf-8 -*-

import math
import numpy as np
import matplotlib.pyplot as plt

class Orbit:
    _inOrbit = []
    _inOrbitCount = 0
    
    def __init__(self, name=''):
        if name == '':
            Orbit._inOrbit.append(len(Orbit._inOrbit) + 1)
        else:
            Orbit._inOrbit.append(name)

        self.status = 0
        self.path = []
        
    def showInOrbit(self):
        print('Items in orbit:',len(Orbit._inOrbit))
        print(*Orbit._inOrbit)
    
        
    def circularOrbit(self, smajor=4000, steps=50, table='hide', image='hide', summary='hide'):
        self.smajor = smajor
        self.sminor = 0
        self.eccen = 0
        self.steps = steps
        
        # circular orbit - applies parametric equation for orbital motion
        for a in range(0, self.steps):
            self.angle = a * 2 * math.pi / self.steps
            self.path.append([self.angle, math.cos(self.angle) * smajor, math.sin(self.angle) * smajor])
                  
        if table == 'show':
            for pa, px, py in self.path:
                print('{0:8.2f}\t{1:8.2f}\t{2:8.2f}'.format(pa, px, py))

        if image == 'show':
            pass
            
        if summary == 'show':           
            # print orbit details after calculation       
            print('------Orbital Parameters------')
            print('Major Axis:', self.smajor)
            print('Minor Axis:', self.sminor)
            print('Eccentricity:', self.eccen)
            print('Steps:', self.steps)
    
            
    def ellipticalOrbit(self, smajor=4000, sminor=0, e=0, steps=50, table='hide', image='hide', summary='hide'):
        self.smajor = smajor
        self.sminor = sminor
        self.eccen = e
        self.steps = steps
            
        # elliptical orbit
        if self.sminor <= self.smajor and self.sminor > 0 and self.smajor > 0:
            if self.eccen == 0:
                self.eccen = math.sqrt(self.smajor**2 - self.sminor**2)/self.smajor
            
            for a in range(0, self.steps):
                self.angle = a * 2 * math.pi / self.steps
                self.path.append([self.angle, math.cos(self.angle) * smajor, math.sin(self.angle) * smajor])
                
        elif (self.sminor > 0 and self.eccen > 0 and self.eccen <= 1) or (self.smajor == 0 and self.eccen > 0 and self.eccen <= 1):
            pass
        else:
            raise Exception('Check input arguments.')
                           
        if table == 'show':
            for pa, px, py in self.path:
                print('{0:8.2f}\t{1:8.2f}\t{2:8.2f}'.format(pa, px, py))
            
        if image == 'show':
            pass
            
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

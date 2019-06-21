#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: sourkey

"""

import math
import numpy as np
import matplotlib.pyplot as plt

class Orbit:
    _inOrbit = []
    _inOrbitCount = 0
    
    # object initialization
    def __init__(self, name=''):
        if name == '':
            Orbit._inOrbit.append(len(Orbit._inOrbit) + 1)
        else:
            Orbit._inOrbit.append(name)

        self.status = 0
        self.path = []
    
    # summary of orbital objects    
    def showInOrbit(self):
        print('Items in orbit:',len(Orbit._inOrbit))
        print(*Orbit._inOrbit)
    
    # circular orbit calcs    
    def circularOrbit(self, smajor=4000, steps=50, table='hide', image='hide', summary='hide'):
        self.smajor = smajor
        self.eccen = 0
        self.steps = steps
        self.mass = 5.972*10**24
        self.speed = 0
        
        # circular orbit - applies parametric equation for orbital motion
        self.speed = math.sqrt((6.674*10**-11) * self.mass / self.smajor / 1000)
        print(self.speed)
        for a in range(0, self.steps + 1):
            self.angle = a * 2 * math.pi / self.steps
            self.path.append([self.angle,\
                math.cos(self.angle) * smajor, math.sin(self.angle) * smajor, self.smajor, self.speed])
        
        # print table of positions at true anomoly          
        if table == 'show':
            print('Anomoly [rad]\tX [km]\t\tY [km]\t\tR [km]\t\tVelocity [m/s]')
            print('-' * 80)
            for pa, px, py, pr, pv in self.path:
                print('{0:8.2f}\t{1:8.2f}\t{2:8.2f}\t{3:8.2f}\t{4:8.2f}'.format(pa, px, py, pr, pv))

        # show image of orbit
        if image == 'show':
            fig = plt.figure()
            fig.suptitle('Circular Orbit, R={0}'.format(self.smajor))
            plt.plot(np.array(self.path)[:,1],np.array(self.path)[:,2], label='Path')
            plt.plot(0,0, label='Center', marker='x')
            plt.legend()
            plt.show()
            
            pass
        
        # print orbital paramenters
        if summary == 'show':           
            # print orbit details after calculation       
            print('------Orbital Parameters------')
            print('Major Axis:', self.smajor)
            print('Eccentricity:', self.eccen)
            print('Steps:', self.steps)
            print('Orbital Speed:', self.speed)

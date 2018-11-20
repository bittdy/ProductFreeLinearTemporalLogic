# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 12:38:58 2018

@author: bittdy
"""

import matplotlib.pyplot as plt
import csv
import numpy as np 

pref=[[['',-1] for i in range(0,14)] for j in range(0,1494)]

with open('Result.csv','r') as result:
    r = csv.DictReader(result)
    for line in r:
        pref[int(line['timestep'])][int(line['agent_id'])][0] = line['agent_color']
        pref[int(line['timestep'])][int(line['agent_id'])][1] = line['comm_dict']
print(pref)
fig, ax = plt.subplots()
ax.broken_barh([(110, 30), (150, 10)], (10, 30), facecolors='blue')
ax.broken_barh([(10, 50), (100, 20), (130, 10)], (20, 9),
               facecolors=('red', 'yellow', 'green'))
ax.set_ylim(0,75)
ax.set_xlim(0,1493)
ax.set_xlabel('seconds since start')
ax.set_yticks([5,10,15,20,25,30,35,40,45,50,55,60,65,70])
ax.set_yticklabels(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13'])
ax.grid(True)
ax.annotate('race interrupted', (610, 25),
            xytext=(0.8, 0.9), textcoords='axes fraction',
            arrowprops=dict(facecolor='black', shrink=0.05),
            fontsize=16,
            horizontalalignment='right', verticalalignment='top')

plt.show()
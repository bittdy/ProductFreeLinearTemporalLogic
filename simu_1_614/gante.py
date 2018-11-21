# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 12:38:58 2018

@author: bittdy
"""

import matplotlib.pyplot as plt
import csv
import numpy as np 

#圆柱宽度
width = 2
#仿真帧数
timestep_num = 1524
yticks = [5,10,15,20,25,30,35,40,45,50,55,60,65,70]
pref=[[['',-1] for i in range(0,14)] for j in range(0,timestep_num)]
fig, ax = plt.subplots()
count = 0
debug = 0
last_color= [-1 for i in range(0,14)]
with open('Result.csv','r') as result:
    r = csv.DictReader(result)
    for line in r:
        if debug == 1:
            if count>timestep_num:
                break
            else:
                print(count)
        count = count + 1
        print(count)
        pref[int(line['timestep'])][int(line['agent_id'])][0] = line['agent_color']
        pref[int(line['timestep'])][int(line['agent_id'])][1] = line['comm_dict']
        ax.broken_barh([(int(line['timestep']),1)],(yticks[int(line['agent_id'])]-width/2,width),facecolors=line['agent_color'])
        if line['agent_color']!=last_color[int(line['agent_id'])] and (line['agent_color'] == 'deepskyblue' or  line['agent_color'] == 'black'):
            ax.text(int(line['timestep']),yticks[int(line['agent_id'])]+width/2+0.5,line['comm_dict'],fontsize=10)
               
        last_color[int(line['agent_id'])] = line['agent_color']
#print(pref)




ax.set_ylim(0,75)
ax.set_xlim(0,timestep_num)
ax.set_xlabel('timestep')
ax.set_ylabel('agent index')
ax.set_yticks(yticks)
ax.set_yticklabels(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13'])
ax.grid(False)

#ax.broken_barh([(110, 30), (150, 10)], (20, width), facecolors='blue')
#ax.broken_barh([(10, 50), (100, 20), (130, 10)], (20, 9),
#               facecolors=('red', 'yellow', 'green'))
#
#ax.grid(True)
#ax.annotate('race interrupted', (610, 25),
#            xytext=(0.8, 0.9), textcoords='axes fraction',
#            arrowprops=dict(facecolor='black', shrink=0.05),
#            fontsize=16,
#            horizontalalignment='right', verticalalignment='top')

plt.show()
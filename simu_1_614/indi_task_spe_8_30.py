#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 22:59:38 2018

@author: bittdy
"""

# export PYTHONPATH=$PYTHONPATH:/to/your/P_MAS_TG

from simu_ts import MotionFts,distance
from simu_buchi import buchi_from_ltl
from simu_product import ProdAut
from networkx.classes.digraph import DiGraph
from simu_planner import ltl_planner
import time
from promela import find_symbols
#import numpy as np
#import matplotlib.pyplot as plt


##############################
# motion FTS for multi-agent

# lable for agent1    rij indicates that the agent i is at the region j
# ap1 = {'r11', 'r12', 'r13', 'r14', 'r15', 'r16'}
ap1 = {'start','r5','goods','r6','r9','door','depot','b','r1','r2','r8'}
ap2 = {'start','r2','r3','r4','open2','b'}
ap3 = {'start','r1','open_d','door_d','r7','open1','r8','r9','r6','goods','r5','b'}

#ap_array = [ap1,ap2,ap3]

# +-----+-----+-----+
# | r4,r| r5,b| r6,b|
# +-----+-----+-----+
# | r1,r| r2,b| r3,r|
# +-----+-----+-----+

# regions for agent1
regions1 = {  (2, 0, 1): set(['start']),
              (1, 0, 1): set(['r1']),
              (3 ,0, 1): set(['r2']),
              (1, 1, 1): set(['b']),
              (2, 1, 1): set(['r5']),
              (3, 1, 1): set(['b']),
              (1, 2, 1): set(['b']),
              (2, 2, 1):set(['goods']),
              (3, 2, 1):set(['b']),
              (1, 3, 1):set(['b']),
              (2, 3, 1):set(['r6']),
              (3, 3, 1):set(['b']),
              (4, 3, 1):set(['b']),
              (1, 4, 1):set(['r8']),
              #(1, 4, 1):set(['b']),
              (2, 4, 1):set(['r9']),
              (3, 4, 1):set(['door','rq']),
              (4, 4, 1):set(['depot'])
}

# regions for agent2
regions2 = {  (1, 0, 1):set(['r1']),
              (2, 0, 1):set(['start']),
              (3, 0, 1):set(['r2']),
              (4, 0, 1):set(['r3']),
              (1, 1, 1):set(['b']),
              (2, 1, 1):set(['r5']),
              (3, 1, 1):set(['b']),
              (4, 1, 1):set(['r4']),
              (3, 2, 1):set(['b']),
              (4, 2, 1):set(['open2','rp']),
              (3, 3, 1):set(['b']),
              (4, 3, 1):set(['b'])
}

# regions for agent3
regions3 = {  (0, 0, 1):set(['open_d']),
              (1, 0, 1):set(['r1']),
              (2, 0, 1):set(['start']),
              (3, 0, 1):set(['r2']),
              (0, 1, 1):set(['door_d']),
              (1, 1, 1):set(['b']),
              (0, 2, 1):set(['open_d']),
              (1, 2, 1):set(['b']),
              (0, 3, 1):set(['r7']),
              (1, 3, 1):set(['b']),
              (0, 4, 1):set(['open1','rp']),
              (1, 4, 1):set(['r8']),
              #(1, 4, 1):set(['b']),
              (2, 4, 1):set(['r9']),
              (2, 3, 1):set(['r6']),
              (2, 2, 1):set(['goods']),
              (2, 1, 1):set(['r5'])
}

regions_array = [regions1,regions2,regions3]

# edges for agent1
edges1 = [((2, 0, 1), (1, 0, 1)),
          ((2, 0, 1), (3, 0, 1)),
          ((2, 0, 1), (2, 1, 1)), 
          ((2, 1, 1), (2, 2, 1)),          
          ((2, 2, 1), (2, 3, 1)),
          ((2, 3, 1), (2, 4, 1)),
          ((2, 4, 1), (1, 4, 1)),
          ((2, 4, 1), (3, 4, 1)),
          ((3, 4, 1), (4, 4, 1)),
]

# edges for agent2
edges2 = [((2, 0, 1), (1, 0, 1)),
          ((2, 0, 1), (2, 1, 1)),
          ((2, 0, 1), (3, 0, 1)), 
          ((3, 0, 1), (4, 0, 1)),          
          ((4, 0, 1), (4, 1, 1)),
          ((4, 1, 1), (4, 2, 1))
]

# edges for agent3
edges3 = [((2, 0, 1), (3, 0, 1)),
          ((2, 0, 1), (1, 0, 1)),
          ((1, 0, 1), (0, 0, 1)), 
          ((0, 2, 1), (0, 3, 1)),          
          ((0, 3, 1), (0, 4, 1)),
          ((0, 4, 1), (1, 4, 1)),
          ((1, 4, 1), (2, 4, 1)),
          ((2, 4, 1), (2, 3, 1)),
          ((2, 3, 1), (2, 2, 1)),
          ((2, 2, 1), (2, 1, 1)),
          ((2, 1, 1), (2, 0, 1))
]


#edges_array = [edges1,edges2,edges3]

inital_regions = (2, 0, 1)

#robot_motion = MultiMotionFts(regions_array, ap_array, 'office' )
#robot_motion.set_initial(inital_regions)
#robot_motion.add_un_edges(edges_array, unit_cost = 0.1)

robot_motion_1 = MotionFts(regions1,ap1,'office')
robot_motion_2 = MotionFts(regions2,ap2,'office')
robot_motion_3 = MotionFts(regions3,ap3,'office')
robot_motion_1.set_initial(inital_regions)
robot_motion_2.set_initial(inital_regions)
robot_motion_3.set_initial(inital_regions)
robot_motion_1.add_un_edges(edges1,unit_cost = 0.1)
robot_motion_2.add_un_edges(edges2,unit_cost = 0.1)
robot_motion_3.add_un_edges(edges3,unit_cost = 0.1)
print ('build multi-robots fts done')

#print(robot_motion.nodes())
#print(robot_motion.edges())

# specify tasks for each Agent

# search r4,r5,r6 after turn on the light, cannot enter the lock region before unlock
#agent_task_1 = '(<>(light && (<> (r4) && <> (r7 && <>r11) ))) && ([](!lock || unlock))'
#agent_task_1 = '<>(r8&&<>(r11&&r21&&r31))'

#agent_task_1 = '[](goods->Xdepot)&&[](depot->Xgoods)&&[](!b)&&[](!door||open)&&[]<>goods&&[]<>depot'
#agent_task_1 = '[](goods-><>depot)&&[](depot-><>goods)&&[](!b)&&[](!door||open)&&[]<>goods&&[]<>depot'
#agent_task_1 = '[]<>depot&&[]<>goods&&[](!b)&&[](depot-><>goods)&&[](goods-><>depot)'
agent_task_1 = '[]<>depot&&[]<>goods&&[](!b)'
agent_task_2 = '[]<>open2&&[]<>start&&[](!b)'
agent_task_3 = '[]<>open1&&[]<>start&&[](!b)&&[](open_d->Xdoor_d)'
#couple_task = '[](! door U (open1&&open2))'
couple_task = '[](!door U (open1 && open2))'

#re-build agent task with couple task
agent_final_task_1 = agent_task_1+'&&'+couple_task
agent_final_task_2 = agent_task_2
agent_final_task_3 = agent_task_3


buchi_1 = buchi_from_ltl(agent_final_task_1,'hard_buchi')
buchi_2 = buchi_from_ltl(agent_final_task_2,'hard_buchi')
buchi_3 = buchi_from_ltl(agent_final_task_3,'hard_buchi')
couple_buchi = buchi_from_ltl(couple_task,'hard_buchi')

couple_task_symbols = find_symbols(couple_task)
#print('guard:')
#for f in buchi_1.nodes():
#    for t in buchi_1.nodes():
#        print(f,t,buchi_1.edges[f,t]['guard'])



#def build_static(indi_pro,couple_pro):
    
#    return new_indi_pro

pro_1 = ProdAut(robot_motion_1,buchi_1)
pro_1.build_full(couple_task_symbols)
#print('nodes:')
#for item in pro_1.nodes():
#    if item[1] == 'accept_S1':
#        print(item)
#print('end')
#
#
#print("product bian")
#for item in pro_1.edges():
#    print(item)

#
pro_2 = ProdAut(robot_motion_2,buchi_2)
pro_2.build_full([])


pro_3 = ProdAut(robot_motion_3,buchi_3)
pro_3.build_full([])
#print("product bian")
#for item in pro_3.edges():
#    print(item)


'''
couple = ProdAut(robot_motion_1,couple_buchi)
couple_final = couple.build_full()
print("product bian")
for item in couple.edges():
    print(item)
print("static bina")
for item in couple_final:
    print(item)
'''
robot_planner_1 = ltl_planner(pro_1)
robot_planner_2 = ltl_planner(pro_2)
robot_planner_3 = ltl_planner(pro_3)
# synthesis
start = time.time()
robot_planner_1.optimal(10,'static')
robot_planner_2.optimal(10,'static')
robot_planner_3.optimal(10,'static')
print ('full construction and synthesis done within %.10fs \n' %(time.time()-start))

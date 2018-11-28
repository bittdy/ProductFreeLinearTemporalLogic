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
import copy
#import numpy as np
#import matplotlib.pyplot as plt


##############################
# motion FTS for multi-agent

# lable for agent1    rij indicates that the agent i is at the region j
# ap1 = {'r11', 'r12', 'r13', 'r14', 'r15', 'r16'}
ap1 = {'n','b','t1','t2','t3','t4','t5','t6','o1'}
ap2 = {'n','b','d','g','r'}
ap3 = {'n','b','m1','m2','m3','m4','m5','m6','o2'}

#ap_array = [ap1,ap2,ap3]

# +-----+-----+-----+
# | r4,r| r5,b| r6,b|
# +-----+-----+-----+
# | r1,r| r2,b| r3,r|
# +-----+-----+-----+

# regions for agent1
regions1 = {  (0, 0, 1): set(['n']),
              (1, 0, 1): set(['n']),
              (2, 0, 1): set(['n']),
              (3, 0, 1): set(['n']),
              (0, 1, 1): set(['n']),
              (1, 1, 1): set(['n']),
              (2, 1, 1): set(['n']),
              (0, 2, 1): set(['n']),
              (1, 2, 1): set(['t4']),
              (2, 2, 1): set(['n']),
              (0, 3, 1): set(['n']),
              (1, 3, 1): set(['b']),
              (2, 3, 1): set(['n']),
              (0, 4, 1): set(['t5']),
              (1, 4, 1): set(['b']),
              (2, 4, 1): set(['t3']),
              (0, 5, 1): set(['n']),
              (1, 5, 1): set(['b']),
              (2, 5, 1): set(['n']),
              (0, 6, 1): set(['n']),
              (1, 6, 1): set(['b']),
              (2, 6, 1): set(['n']),
              (0, 7, 1): set(['t6']),
              (1, 7, 1): set(['b']),
              (2, 7, 1): set(['t2']),
              (0, 8, 1): set(['n']),
              (1, 8, 1): set(['b']),
              (2, 8, 1): set(['n']),
              (0, 9, 1): set(['n']),
              (1, 9, 1): set(['t1']),
              (2, 9, 1): set(['n']),
              (0, 10, 1): set(['n']),
              (1, 10, 1): set(['n']),
              (2, 10, 1): set(['n']),
              (0, 11, 1): set(['n']),
              (1, 11, 1): set(['o1']),
              (2, 11, 1): set(['n']),
              (3, 11, 1): set(['n'])
}

# regions for agent2
regions2 = {  (4, 0, 1):set(['n']),
              (5, 0, 1):set(['n']),
              (4, 1, 1):set(['n']),
              (4, 2, 1):set(['n']),
              (4, 3, 1):set(['g']),
              (4, 4, 1):set(['n']),
              (4, 5, 1):set(['n']),
              (4, 6, 1):set(['n']),
              (4, 7, 1):set(['n']),
              (4, 8, 1):set(['n']),
              (4, 9, 1):set(['n']),
              (4, 10, 1):set(['n']),
              (4, 11, 1):set(['n']),
              (5, 11, 1):set(['n']),
              (6, 11, 1):set(['d']),
              (7, 11, 1):set(['n']),
              (8, 11, 1):set(['r'])
}

# regions for agent3
regions3 = {  (6, 0, 1):set(['n']),
              (7, 0, 1):set(['n']),
              (8, 0, 1):set(['n']),
              (6, 1, 1):set(['n']),
              (7, 1, 1):set(['n']),
              (8, 1, 1):set(['n']),
              (6, 2, 1):set(['n']),
              (7, 2, 1):set(['n']),
              (8, 2, 1):set(['n']),
              (6, 3, 1):set(['n']),
              (7, 3, 1):set(['m4']),
              (8, 3, 1):set(['n']),
              (6, 4, 1):set(['m5']),
              (7, 4, 1):set(['b']),
              (8, 4, 1):set(['m3']),
              (6, 5, 1):set(['n']),
              (7, 5, 1):set(['b']),
              (8, 5, 1):set(['n']),
              (6, 6, 1):set(['m6']),
              (7, 6, 1):set(['b']),
              (8, 6, 1):set(['m2']),
              (6, 7, 1):set(['n']),
              (7, 7, 1):set(['m1']),
              (8, 7, 1):set(['n']),
              (6, 8, 1):set(['n']),
              (7, 8, 1):set(['n']),
              (8, 8, 1):set(['n']),
              (6, 9, 1):set(['n']),
              (7, 9, 1):set(['o2']),
              (8, 9, 1):set(['n'])
}

regions_array = [regions1,regions2,regions3]

# edges for agent1
edges1 = [((0, 0, 1), (1, 0, 1)),
          ((1, 0, 1), (2, 0, 1)),
          ((2, 0, 1), (3, 0, 1)),
          
          ((0, 0, 1), (0, 1, 1)),
          ((1, 0, 1), (1, 1, 1)),
          ((2, 0, 1), (2, 1, 1)),
          
          ((0, 1, 1), (1, 1, 1)),
          ((1, 1, 1), (2, 1, 1)),
                    
          ((0, 1, 1), (0, 2, 1)),
          ((1, 1, 1), (1, 2, 1)),
          ((2, 1, 1), (2, 2, 1)),
          
          ((0, 2, 1), (1, 2, 1)),
          ((1, 2, 1), (2, 2, 1)),
                    
          ((0, 2, 1), (0, 3, 1)),
          ((2, 2, 1), (2, 3, 1)),
          
          ((0, 3, 1), (0, 4, 1)),
          ((2, 3, 1), (2, 4, 1)),
          
          ((0, 4, 1), (0, 5, 1)),
          ((2, 4, 1), (2, 5, 1)),
 
          ((0, 5, 1), (0, 6, 1)),
          ((2, 5, 1), (2, 6, 1)),
          
          ((0, 6, 1), (0, 7, 1)),
          ((2, 6, 1), (2, 7, 1)),
          
          ((0, 7, 1), (0, 8, 1)),
          ((2, 7, 1), (2, 8, 1)),
          
          ((0, 8, 1), (0, 9, 1)),
          ((2, 8, 1), (2, 9, 1)),
          
          ((0, 9, 1), (1, 9, 1)),
          ((1, 9, 1), (2, 9, 1)),
          
          ((0, 9, 1), (0, 10, 1)),
          ((1, 9, 1), (1, 10, 1)),          
          ((2, 9, 1), (2, 10, 1)), 
          
          ((0, 10, 1), (1, 10, 1)),
          ((1, 10, 1), (2, 10, 1)),
          
          ((0, 10, 1), (0, 11, 1)),
          ((1, 10, 1), (1, 11, 1)),          
          ((2, 10, 1), (2, 11, 1)), 
          
          ((0, 11, 1), (1, 11, 1)),
          ((1, 11, 1), (2, 11, 1)),
          ((2, 11, 1), (3, 11, 1))        
]

# edges for agent2
edges2 = [((4, 0, 1), (5, 0, 1)),
          ((4, 0, 1), (4, 1, 1)),
          ((4, 1, 1), (4, 2, 1)), 
          ((4, 2, 1), (4, 3, 1)),          
          ((4, 3, 1), (4, 4, 1)),
          ((4, 4, 1), (4, 5, 1)),
          ((4, 5, 1), (4, 6, 1)),
          ((4, 6, 1), (4, 7, 1)),
          ((4, 7, 1), (4, 8, 1)),
          ((4, 8, 1), (4, 9, 1)),
          ((4, 9, 1), (4, 10, 1)),
          ((4, 10, 1), (4, 11, 1)),
          ((4, 11, 1), (5, 11, 1)),
          ((5, 11, 1), (6, 11, 1)),
          ((6, 11, 1), (7, 11, 1)),
          ((7, 11, 1), (8, 11, 1))
]

# edges for agent3
edges3 = [((6, 0, 1), (7, 0, 1)),
          ((7, 0, 1), (8, 0, 1)),
          
          ((6, 0, 1), (6, 1, 1)),
          ((7, 0, 1), (7, 1, 1)),
          ((8, 0, 1), (8, 1, 1)),
          
          ((6, 1, 1), (7, 1, 1)),
          ((7, 1, 1), (8, 1, 1)),
          
          ((6, 1, 1), (6, 2, 1)),
          ((7, 1, 1), (7, 2, 1)),
          ((8, 1, 1), (8, 2, 1)),
          
          ((6, 2, 1), (7, 2, 1)),
          ((7, 2, 1), (8, 2, 1)),
          
          ((6, 2, 1), (6, 3, 1)),
          ((7, 2, 1), (7, 3, 1)),
          ((8, 2, 1), (8, 3, 1)),
          
          ((6, 3, 1), (6, 4, 1)),
          ((8, 3, 1), (8, 4, 1)),
          
          ((6, 4, 1), (6, 5, 1)),
          ((8, 4, 1), (8, 5, 1)),
          
          ((6, 5, 1), (6, 6, 1)),
          ((8, 5, 1), (8, 6, 1)),
          
          ((6, 6, 1), (6, 7, 1)),
          ((8, 6, 1), (8, 7, 1)),
          
          ((6, 7, 1), (7, 7, 1)),
          ((7, 7, 1), (8, 7, 1)),
          
          ((6, 7, 1), (6, 8, 1)),
          ((7, 7, 1), (7, 8, 1)),
          ((8, 7, 1), (8, 8, 1)),         
        
          ((6, 8, 1), (7, 8, 1)),
          ((7, 8, 1), (8, 8, 1)),
          
          ((6, 8, 1), (6, 9, 1)),
          ((7, 8, 1), (7, 9, 1)),
          ((8, 8, 1), (8, 9, 1)), 
          
          ((6, 9, 1), (7, 9, 1)),
          ((7, 9, 1), (8, 9, 1))        
]


#edges_array = [edges1,edges2,edges3]

inital_regions = [(1, 2, 1),(4, 0, 1),(7, 3, 1)]

#robot_motion = MultiMotionFts(regions_array, ap_array, 'office' )
#robot_motion.set_initial(inital_regions)
#robot_motion.add_un_edges(edges_array, unit_cost = 0.1)

robot_motion_1 = MotionFts(regions1,ap1,'office')
robot_motion_2 = MotionFts(regions2,ap2,'office')
robot_motion_3 = MotionFts(regions3,ap3,'office')
robot_motion_1.set_initial(inital_regions[0])
robot_motion_2.set_initial(inital_regions[1])
robot_motion_3.set_initial(inital_regions[2])
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
agent_task_1 = '[]<>t1&&[]<>t2&&[]<>t3&&[]<>t4&&[]<>t5&&[]<>t6&&[](!b)'
agent_task_2 = '[]<>g&&[](!b)&&[](g-><>r)'
agent_task_3 = '[]<>m1&&[]<>m2&&[]<>m3&&[]<>m4&&[]<>m5&&[]<>m6&&[](!b)'
#couple_task = '[](! door U (open1&&open2))'
couple_task = '[](!d U (o1 && o2))'

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

#prod1 is going to inherit prod2
def union_product(Prod1,Prod2):
#    print(type(Prod1.nodes()))
    uni_pro = copy.deepcopy(Prod2)
    
    #jiang suo you prod1 de zhuang tai she wei initial
 
    for item in Prod1.edges():
        if item[0][1] == 'T0_init' and item[1][1] == 'T0_init':
            uni_pro.add_edge(item[0],item[1],weight=abs(item[0][0][0]-item[1][0][0])+abs(item[0][0][1]-item[1][0][1]))
#    uni_pro.add_edges_from(Prod1.edges())
    node_list = Prod1.graph['ts'].nodes()
    for n in node_list:
        uni_pro.graph['ts'].add_node(n,label=Prod1.graph['ts'].node[n]['label'])
    
    Prod2_bord_regions = []
     
    for pro1_node in Prod1.nodes():
        f_node_1 = pro1_node[0]
        b_node_1 = pro1_node[1]
        if b_node_1 != 'T0_init':
            continue
        for pro2_node in Prod2.nodes():
#            print('pro1_node:',pro1_node)
#            print('pro2_node:',pro2_node)

            uni_pro.add_node((f_node_1,'T0_init'))
            
            f_node_2 = pro2_node[0]
            b_node_2 = pro2_node[1]
            
            dist = (f_node_1[0]-f_node_2[0])**2 + (f_node_1[1]-f_node_2[1])**2
            if dist == 1:  #jie rang
                uni_pro.add_edge(uni_pro.composition(f_node_1,b_node_1),uni_pro.composition(f_node_2,b_node_2),weight=dist)
                if f_node_2 not in Prod2_bord_regions:
                    Prod2_bord_regions.append(f_node_2)
                print('add an edge:')
                print(uni_pro.composition(f_node_1,b_node_1),uni_pro.composition(f_node_2,b_node_2),dist)
                
    print('nodes:')
    for item in uni_pro.nodes():
        print(item)
                
#    print(Prod2_bord_regions)
    print('new paths')
    
    #prod1 de fys
    
    uni_pro.graph['initial'] = set([((0,6,1),'T0_init')])
    

    
    print('initial:',uni_pro.graph['initial'])
    
    new_planner = ltl_planner(uni_pro)
    new_planner.optimal(10,'static')
       
        

union_product(pro_1,pro_2)
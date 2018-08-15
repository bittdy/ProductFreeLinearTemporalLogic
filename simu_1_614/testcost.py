#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 19:53:19 2018

@author: bittdy
"""

from simu_ts import MotionFts,distance
from simu_buchi import buchi_from_ltl
from simu_product import ProdAut
from networkx.classes.digraph import DiGraph
from simu_planner import ltl_planner
import time
#import numpy as np
#import matplotlib.pyplot as plt


##############################
# motion FTS for multi-agent

# lable for agent1    rij indicates that the agent i is at the region j
# ap1 = {'r11', 'r12', 'r13', 'r14', 'r15', 'r16'}
ap1 = {'r1','r2','r3','r4','r5','goods','open','door','depot','b'}

# lable for agent2
# ap2 = {'r21', 'r22', 'r23', 'r24', 'r25', 'r26'}
#ap2 = {'r21','r22','r3','r4','r5','r6','r7','r8','lock','unlock','light'}

#ap3 = {'r31','r32','r3','r4','r5','r6','r7','r8','lock','unlock','light'}


#ap_array = [ap1,ap2,ap3]

# +-----+-----+-----+
# | r4,r| r5,b| r6,b|
# +-----+-----+-----+
# | r1,r| r2,b| r3,r|
# +-----+-----+-----+

# regions for agent1
regions1 = {   (0, 0, 1): set(['r1']),
              (1, 0, 1): set(['b']),
              (0, 1, 1):set(['r2']),
              (1, 1, 1): set(['b']),
              (0, 2, 1): set(['goods']),
              (1, 2, 1): set(['b']),
              (2, 2, 1): set(['open']),
              (0, 3, 1):set(['r3']),
              (1, 3, 1):set(['r4']),
              (2, 3, 1):set(['r5']),
              (3, 3, 1):set(['door']),
              (4, 3, 1):set(['depot'])
}

# regions for agent2
regions2 = {   (0, 0, 1): set(['r1']),
              (1, 0, 1): set(['b']),
              (0, 1, 1):set(['r2']),
              (1, 1, 1): set(['b']),
              (0, 2, 1): set(['goods']),
              (1, 2, 1): set(['b']),
              (2, 2, 1): set(['open']),
              (0, 3, 1):set(['r3']),
              (1, 3, 1):set(['r4']),
              (2, 3, 1):set(['r5']),
              (3, 3, 1):set(['door']),
              (4, 3, 1):set(['depot'])
}
'''
# regions for agent3
regions3 = {   (0, 1, 1): set(['r4']),
              (0, 0, 1): set(['r5']),
              (0.5, 0, 1):set(['lock']),
              (0, -1, 1): set(['r6','light']),
              (1, 0, 1): set(['r32']),
              (1, -1, 1): set(['r3','unlock']),
              (2, 0, 1): set(['r31']),
              (1,-2, 1):set(['r7']),
              (1, 1, 1):set(['r8']),
}

regions_array = [regions1,regions2,regions3]
'''
# edges for agent1
edges1 = [((0, 0, 1), (0, 1, 1)),
          ((0, 1, 1), (0, 2, 1)),
         ((0, 2, 1), (0, 3, 1)), 
         ((0, 3, 1), (1, 3, 1)),          
         ((1, 3, 1), (2, 3, 1)),
         ((2, 3, 1), (2, 2, 1)),
         ((3, 3, 1), (2, 3, 1)),
         ((3, 3, 1), (4, 3, 1))
]

# edges for agent1
edges2 = [((0, 0, 1), (0, 1, 1)),
          ((0, 1, 1), (0, 2, 1)),
         ((0, 2, 1), (0, 3, 1)), 
         ((0, 3, 1), (1, 3, 1)),          
         ((1, 3, 1), (2, 3, 1)),
         ((2, 3, 1), (2, 2, 1)),
         ((3, 3, 1), (2, 3, 1)),
         ((3, 3, 1), (4, 3, 1))
]
'''
# # edges for agent3
edges3 = [((0, 0, 1), (0.5, 0, 1)),
          ((1, 0, 1), (0.5, 0, 1)),
         ((0, 0, 1), (0, 1, 1)), 
         ((0, 0, 1), (0, -1, 1)),          
         ((1, 0, 1), (1, -1, 1)),
         ((1, 0, 1), (2, 0, 1)),
         ((1,-1, 1), (1,-2, 1)),
         ((1, 1, 1), (1, 0, 1)),
]
'''
#edges_array = [edges1,edges2,edges3]

inital_regions = (0,0,1)

#robot_motion = MultiMotionFts(regions_array, ap_array, 'office' )
#robot_motion.set_initial(inital_regions)
#robot_motion.add_un_edges(edges_array, unit_cost = 0.1)

robot_motion = MotionFts(regions1,ap1,'office')
robot_motion.set_initial(inital_regions)
robot_motion.add_un_edges(edges1,unit_cost = 0.1)


print ('build multi-robots fts done')

print(robot_motion.nodes())
print(robot_motion.edges())

robot_motion_1 = robot_motion_2 = robot_motion

# specify tasks for each Agent

# search r4,r5,r6 after turn on the light, cannot enter the lock region before unlock
#agent_task_1 = '(<>(light && (<> (r4) && <> (r7 && <>r11) ))) && ([](!lock || unlock))'
#agent_task_1 = '<>(r8&&<>(r11&&r21&&r31))'

agent_task_1 = '[](goods->Xdepot)&&[](depot->Xgoods)&&[](!b)&&[](!door||open)&&[]<>goods&&[]<>depot'
agent_task_2 = '[]<>open'

'''
agent_task_2 = '([]((!r4&&!r8&&!r7)||light))&&(<>(r4))'
agent_task_3 = '<>(r7)&&([](!lock||unlock))'

agents_task_array = [agent_task_1,agent_task_2,agent_task_3]

# agent_task_1_individual = '[](!lock||unlock)&&<>(r8)'
# agent_task_2_individual = '<>(r7)&&([]((!r4&&!r8&&!r7)||light))'
# agent_task_3_individual = '<>(r4)'
# 
# agents_task_array_individual = [agent_task_1_individual,agent_task_2_individual,agent_task_3_individual]

trigger_condition =  check_trigger_conditions_from_spec(agents_task_array)
'''

buchi_1 = buchi_from_ltl(agent_task_1,'hard_buchi')
buchi_2 = buchi_from_ltl(agent_task_2,'hard_buchi')

print(buchi_1.nodes())
print(buchi_1.edges())

pro_1 = ProdAut(robot_motion,buchi_1)
pro_1_static_list = pro_1.build_full()

pro_2 = ProdAut(robot_motion,buchi_2)
pro_2_static_list = pro_2.build_full()

static_list = [pro_1_static_list,pro_2_static_list]

print(pro_1.nodes())
print(pro_1.edges())
print(len(pro_1.nodes()))
print(len(pro_1.edges()))

#fts mu qian zan shi she zhi wei yi yang de 
region_array = [regions1,regions2]
fts_array = [robot_motion_1,robot_motion_2]
buchi_array = [buchi_1,buchi_2]
pro_array = [pro_1,pro_2]
colla_ap = [['door'],['open']]

print('state_list:')
print(pro_1_static_list)
print(pro_2_static_list)
print(type(pro_1_static_list[0][2]))

def find_region(ap,region):
    cor_pos_list = [ap]
    for item in region:
        if ap in region[item]:
                cor_pos_list.append(item)
    return cor_pos_list

for agent_index in range(len(pro_array)):  #对每一个机器人的product自动机
    for other_agent in range(len(pro_array)):
        if agent_index == other_agent:
            continue
        else:
            #no collative task
            if len(colla_ap[other_agent]) == 0: 
                continue
            else:
                for ap_item in colla_ap[other_agent]:
                    print(ap_item)
                    #zai region zhong zhao dao suo you yu ap dui ying de qu yu dian
                    cor_pos_list = find_region(ap_item,region_array[other_agent])
                    print(cor_pos_list)
                    #zai fts zhao dao mei ge qu yu dian de qian ji yi ji cost, qu zui xiao de cun xia lai
                    cost_static = float('inf')
                    fts_digraph = DiGraph()
                    fts_digraph.add_edges_from(fts_array[other_agent].edges())  
                    print(fts_digraph.edges())
                    for pos in cor_pos_list:
                        if len(pos) != 3:
                            continue
                        for pre_pos in fts_digraph.predecessors(pos):
                            if pre_pos == pos:  #pai chu yuan di bu dong de qing kuang
                                continue
                            cost_buf = distance(pos,pre_pos)
                            if cost_buf < cost_static:
                                cost_static = cost_buf
                    #zai ben ji qi ren de product zhong jia bian ,ju ti jia fa an guomeng zhi qian gou jian product zi dong ji de fang fa
                    print(cost_static)
                    for static_edge in static_list[agent_index]:#shu ju jie guo de tong yi
                        if ap_item in static_edge[2]:
                            print(static_edge[0],static_edge[1],static_edge[2],cost_static)
                            pro_array[agent_index].add_edge(static_edge[0],static_edge[1],weight = cost_static)
                            
print('0:')
print(pro_array[0].edges())
print('1:')
print(pro_array[1].edges())
    

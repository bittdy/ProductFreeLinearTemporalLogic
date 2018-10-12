# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 14:02:13 2018

@author: bittdy
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 21:22:43 2018

@author: bittdy
"""

#at first: change previous code, add the request attribute to the plan result

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.lines import Line2D
from matplotlib.animation import FuncAnimation 

#构建机器人运动序列
agents_path = [[ [(4,0),(4,1),(4,2),(4,3),(4,4),(4,5),(4,6)], [(4,7),(4,8),(4,9),(4,10),(4,11),(5,11,'req'),(6,11),(7,11,'req'),(6,11),(5,11),(4,11),(4,10),(4,9),(4,8),(4,7)] ], #agent1-2 goods depot
               [ [], [(7,11,'req'),(6,11),(5,11),(4,11),(4,10),(4,9),(4,8),(4,7),(4,8),(4,9),(4,10),(4,11),(5,11,'req'),(6,11),(7,11)] ],
               [ [], [(1,9),(0,9),(0,8),(0,7),(0,6),(0,5),(0,4),(0,3),(0,2),(1,2),(2,2),(2,3),(2,4),(2,5),(2,6),(2,7),(2,8),(2,9),(1,9)] ], #agent2-7 open1
               [ [], [(0,7),(0,6),(0,5),(0,4),(0,3),(0,2),(1,2),(2,2),(2,3),(2,4),(2,5),(2,6),(2,7),(2,8),(2,9),(1,9),(0,9),(0,8),(0,7)] ],
               [ [], [(0,4),(0,3),(0,2),(1,2),(2,2),(2,3),(2,4),(2,5),(2,6),(2,7),(2,8),(2,9),(1,9),(0,9),(0,8),(0,7),(0,6),(0,5),(0,4)] ],
               [ [], [(1,2),(2,2),(2,3),(2,4),(2,5),(2,6),(2,7),(2,8),(2,9),(1,9),(0,9),(0,8),(0,7),(0,6),(0,5),(0,4),(0,3),(0,2),(1,2)] ],
               [ [], [(2,4),(2,5),(2,6),(2,7),(2,8),(2,9),(1,9),(0,9),(0,8),(0,7),(0,6),(0,5),(0,4),(0,3),(0,2),(1,2),(2,2),(2,3),(2,4)] ],
               [ [], [(2,7),(2,8),(2,9),(1,9),(0,9),(0,8),(0,7),(0,6),(0,5),(0,4),(0,3),(0,2),(1,2),(2,2),(2,3),(2,4),(2,5),(2,6),(2,7)] ],
               [ [], [(7,7),(6,7),(6,6),(6,5),(6,4),(6,3),(7,3),(8,3),(8,4),(8,5),(8,6),(8,7),(7,7)] ], #agent8-13 open2
               [ [], [(6,6),(6,5),(6,4),(6,3),(7,3),(8,3),(8,4),(8,5),(8,6),(8,7),(7,7),(6,7),(6,6)] ],
               [ [], [(6,4),(6,3),(7,3),(8,3),(8,4),(8,5),(8,6),(8,7),(7,7),(6,7),(6,6),(6,5),(6,4)] ],
               [ [], [(7,3),(8,3),(8,4),(8,5),(8,6),(8,7),(7,7),(6,7),(6,6),(6,5),(6,4),(6,3),(7,3)] ],
               [ [], [(8,4),(8,5),(8,6),(8,7),(7,7),(6,7),(6,6),(6,5),(6,4),(6,3),(7,3),(8,3),(8,4)] ],
               [ [], [(8,6),(8,7),(7,7),(6,7),(6,6),(6,5),(6,4),(6,3),(7,3),(8,3),(8,4),(8,5),(8,6)] ]]
goal_point_index = [1 for i in range(0,len(agents_path))]
#创建画布
fig1 = plt.figure()
ax1 = fig1.add_subplot(111, aspect='equal')
ax1.set_xlim(left = -0.5,right = 8.5)
ax1.set_ylim(bottom = -0.5,top = 11.5)
# 画出维持不变的实验环境以及要变的那些对象的初始位置
#矩形构成的试验环境，蓝色为障碍物，白色为正常区域
ax1.add_patch(patches.Rectangle((0.5,2.5),1,6))
ax1.add_patch(patches.Rectangle((2.5,0.5),1,10))
ax1.add_patch(patches.Rectangle((4.5,0.5),1,10))
ax1.add_patch(patches.Rectangle((5.5,9.5),3,1))
ax1.add_patch(patches.Rectangle((6.5,3.5),1,3))
ax1.add_patch(patches.Rectangle((6.7,10.7),0.6,0.6))
xyrange = np.arange(11)+0.5
for i in xyrange:
    ax1.axhline(y = i,linestyle = '--')
    ax1.axvline(x = i,linestyle = '--')
##圆构成的机器人
agents_list = []
for i in range(0,len(agents_path)):
    if len(agents_path[i][0]) == 0:  #没有前缀
        agent = patches.Ellipse(xy=(agents_path[i][1][0][0],agents_path[i][1][0][1]),width=0.3,height=0.3,color='r',fill='True')
        ax1.add_artist(agent)
        agents_list.append(agent)
    else:
        agent = patches.Ellipse(xy=(agents_path[i][0][0][0],agents_path[i][0][0][1]),width=0.3,height=0.3,color='r',fill='True')
        ax1.add_artist(agent)
        agents_list.append(agent)
#文字，在之后的动画中的那一帧加
#门
door = Line2D((6,6),(10.53,11.5),linewidth='5',color='gray')
ax1.add_line(door)
##货物
#good = patches.Ellipse(xy=(2,2),width=0.15,height=0.15,color='green',fill='True')
#ax1.add_artist(good)
##开关
#open1 = patches.Ellipse(xy=(0,4),width=0.3,height=0.3,color='gray',fill='True')
#open2 = patches.Ellipse(xy=(4,2),width=0.3,height=0.3,color='gray',fill='True')
#ax1.add_artist(open1)
#ax1.add_artist(open2)
#
#req_list = []
#rep_list = []
#con_list = []
#
#def dist(pose1,pose2):
#    return ((pose1[0]-pose2[0])**2+(pose1[1]-pose2[1])**2)**0.5
#
#def movement(): #放到一个类里面去
#    #确定每个机器人点的运动，并判断是否需要发出req，rep，con信号
#    if len(agents_path[0][goal_point_index[0]])==3 and len(req_list)==0:
#        req_list.append('req')
#    if len(agents_path[1][goal_point_index[1]])==3 and 'rep1' not in rep_list and dist(agent2.center,agents_path[1][goal_point_index[1]])<0.01:
#        rep_list.append('rep1')
#    if len(agents_path[2][goal_point_index[2]])==3 and 'rep2' not in rep_list and dist(agent3.center,agents_path[2][goal_point_index[2]])<0.01:
#        rep_list.append('rep2')
#    if dist(agent1.center,(4,4))<0.5 and len(con_list)==0:
#        con_list.append('con')
#        
#    agent1_incre = [0,0]
#    agent2_incre = [0,0]  
#    agent3_incre = [0,0]  
#    
#    if len(req_list)==0 or (len(req_list)!=0 and len(rep_list)==2):#agent1可以继续前进
#        if agent1.center[0] < agents_path[0][goal_point_index[0]][0]:
#            agent1_incre[0] = 0.02
#        elif agent1.center[0] > agents_path[0][goal_point_index[0]][0]:
#            agent1_incre[0] = -0.02
#        else:
#            agent1_incre[0] = 0
#        if agent1.center[1] < agents_path[0][goal_point_index[0]][1]:
#            agent1_incre[1] = 0.02
#        elif agent1.center[1] > agents_path[0][goal_point_index[0]][1]:
#            agent1_incre[1] = -0.02
#        else:
#            agent1_incre[1] = 0
#    else:
#        agent1_incre = [0,0]
#    
#    if len(req_list)==0 or (len(req_list)!=0 and len(con_list)!=0) or (len(req_list)!=0 and 'rep1' not in rep_list):#agent2可以继续前进
#        if agent2.center[0] < agents_path[1][goal_point_index[1]][0]:
#            agent2_incre[0] = 0.01
#        elif agent2.center[0] > agents_path[1][goal_point_index[1]][0]:
#            agent2_incre[0] = -0.01
#        else:
#            agent2_incre[0] = 0
#        if agent2.center[1] < agents_path[1][goal_point_index[1]][1]:
#            agent2_incre[1] = 0.01
#        elif agent2.center[1] > agents_path[1][goal_point_index[1]][1]:
#            agent2_incre[1] = -0.01
#        else:
#            agent2_incre[1] = 0
#    else:
#        agent2_incre = [0,0]
#        
#    if len(req_list)==0 or (len(req_list)!=0 and len(con_list)!=0) or (len(req_list)!=0 and 'rep2' not in rep_list):#agent3可以继续前进
#        if agent3.center[0] < agents_path[2][goal_point_index[2]][0]:
#            agent3_incre[0] = 0.01
#        elif agent3.center[0] > agents_path[2][goal_point_index[2]][0]:
#            agent3_incre[0] = -0.01
#        else:
#            agent3_incre[0] = 0
#        if agent3.center[1] < agents_path[2][goal_point_index[2]][1]:
#            agent3_incre[1] = 0.01
#        elif agent3.center[1] > agents_path[2][goal_point_index[2]][1]:
#            agent3_incre[1] = -0.01
#        else:
#            agent3_incre[1] = 0
#    else:
#        agent3_incre = [0,0]
#    
#    
#    if dist(agent1.center,agents_path[0][goal_point_index[0]])<0.03 and goal_point_index[0]+1<len(agents_path[0]):
#        goal_point_index[0] = goal_point_index[0]+1
#    if dist(agent2.center,agents_path[1][goal_point_index[1]])<0.01 and goal_point_index[1]+1<len(agents_path[1]):
#        goal_point_index[1] = goal_point_index[1]+1
#    if dist(agent3.center,agents_path[2][goal_point_index[2]])<0.01 and goal_point_index[2]+1<len(agents_path[2]):
#        goal_point_index[2] = goal_point_index[2]+1
#        
#    return [agent1_incre,agent2_incre,agent3_incre]
#
#def update(i):
#    label = 'timestep {0}'.format(i)
#    #确定机器人新位置
#    agent_incre = movement()
#    agent1.center = (agent1.center[0]+agent_incre[0][0],agent1.center[1]+agent_incre[0][1])
#    agent2.center = (agent2.center[0]+agent_incre[1][0],agent2.center[1]+agent_incre[1][1])
#    agent3.center = (agent3.center[0]+agent_incre[2][0],agent3.center[1]+agent_incre[2][1])
#    #确定门，货物等物品状态
#    if dist(agent2.center,open1.center)<0.02 and dist(agent3.center,open2.center)<0.02:
#        door.set_linewidth('0')
#    else:
#        door.set_linewidth('5')
#        
#    if dist(agent1.center,good.center)<0.03:
#        good.center = agent1.center
#    
#    if dist(agent1.center,[4,4])<0.1:
#        good.set_color('red')
#        
#    if dist(agent2.center,open1.center)<0.02:
#        open1.set_color('yellow')
#    else:
#        open1.set_color('gray')  
#        
#    if dist(agent3.center,open2.center)<0.02:
#        open2.set_color('yellow')
#    else:
#        open2.set_color('gray')   
#    
#    repaint = (door,agent1,agent2,agent3,good,open1,open2)
#    ax1.set_xlabel(label)    
#    return repaint, ax1
#
## FuncAnimation 会在每一帧都调用“update” 函数。
## 在这里设置一个10帧的动画，每帧之间间隔200毫秒
#anim = FuncAnimation(fig1, update, frames=np.arange(0, 1000), interval=20)
#

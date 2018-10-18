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
#仿真参数为间隔20ms
interval = 20
#机器人速度
agent_velocity = [0.03,0.01,0.02,0.02,0.02,0.02,0.02,0.02,0.02,0.02,0.02,0.02,0.02,0.02]
#机器人分组
agents_split = [1,7,13]
#构建机器人运动序列
agents_path = [[ 9,(4,0),(4,1),(4,2),(4,3),(4,4),(4,5),(4,6),(4,7),(4,8),(4,9),(4,10),(4,11),(5,11,'req_1',[(1,11),(7,9)]),(6,11),(7,11,'con_1'),(8,11),(7,11,'req_2',[(1,11),(7,9)]),(6,11),(5,11,'con_2'),(4,11),(4,10),(4,9),(4,8),(4,7) ], #agent1-2 goods depot
               [ 2,(8,11),(7,11,'req_2',[(1,11),(7,9)]),(6,11),(5,11,'con_2'),(4,11),(4,10),(4,9),(4,8),(4,7),(4,8),(4,9),(4,10),(4,11),(5,11,'req_1',[(1,11),(7,9)]),(6,11),(7,11,'con_1'),(8,11) ],
               [ 2,(1,9),(0,9),(0,8),(0,7),(0,6),(0,5),(0,4),(0,3),(0,2),(1,2),(2,2),(2,3),(2,4),(2,5),(2,6),(2,7),(2,8),(2,9),(1,9) ], #agent2-7 open1
               [ 2,(0,7),(0,6),(0,5),(0,4),(0,3),(0,2),(1,2),(2,2),(2,3),(2,4),(2,5),(2,6),(2,7),(2,8),(2,9),(1,9),(0,9),(0,8),(0,7) ],
               [ 2,(0,4),(0,3),(0,2),(1,2),(2,2),(2,3),(2,4),(2,5),(2,6),(2,7),(2,8),(2,9),(1,9),(0,9),(0,8),(0,7),(0,6),(0,5),(0,4) ],
               [ 2,(1,2),(2,2),(2,3),(2,4),(2,5),(2,6),(2,7),(2,8),(2,9),(1,9),(0,9),(0,8),(0,7),(0,6),(0,5),(0,4),(0,3),(0,2),(1,2) ],
               [ 2,(2,4),(2,5),(2,6),(2,7),(2,8),(2,9),(1,9),(0,9),(0,8),(0,7),(0,6),(0,5),(0,4),(0,3),(0,2),(1,2),(2,2),(2,3),(2,4) ],
               [ 2,(2,7),(2,8),(2,9),(1,9),(0,9),(0,8),(0,7),(0,6),(0,5),(0,4),(0,3),(0,2),(1,2),(2,2),(2,3),(2,4),(2,5),(2,6),(2,7) ],
               [ 2,(7,7),(6,7),(6,6),(6,5),(6,4),(6,3),(7,3),(8,3),(8,4),(8,5),(8,6),(8,7),(7,7) ], #agent8-13 open2
               [ 2,(6,6),(6,5),(6,4),(6,3),(7,3),(8,3),(8,4),(8,5),(8,6),(8,7),(7,7),(6,7),(6,6) ],
               [ 2,(6,4),(6,3),(7,3),(8,3),(8,4),(8,5),(8,6),(8,7),(7,7),(6,7),(6,6),(6,5),(6,4) ],
               [ 2,(7,3),(8,3),(8,4),(8,5),(8,6),(8,7),(7,7),(6,7),(6,6),(6,5),(6,4),(6,3),(7,3) ],
               [ 2,(8,4),(8,5),(8,6),(8,7),(7,7),(6,7),(6,6),(6,5),(6,4),(6,3),(7,3),(8,3),(8,4) ],
               [ 2,(8,6),(8,7),(7,7),(6,7),(6,6),(6,5),(6,4),(6,3),(7,3),(8,3),(8,4),(8,5),(8,6) ]]
goal_point_index = [2 for i in range(0,len(agents_path))]
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
ax1.add_patch(patches.Rectangle((7.7,10.7),0.6,0.6))
xyrange = np.arange(11)+0.5
for i in xyrange:
    ax1.axhline(y = i,linestyle = '--')
    ax1.axvline(x = i,linestyle = '--')
##圆构成的机器人
agents_list = []
for i in range(0,len(agents_path)):
    agent = patches.Ellipse(xy=(agents_path[i][1][0],agents_path[i][1][1]),width=0.3,height=0.3,color='r',fill='True')
    ax1.add_artist(agent)
    agents_list.append(agent)
#文字，在之后的动画中的那一帧加
#门
door = Line2D((6,6),(10.53,11.5),linewidth='5',color='gray')
ax1.add_line(door)
##货物
good = patches.Ellipse(xy=(4,7),width=0.15,height=0.15,color='green',fill='True')
ax1.add_artist(good)
##开关
open1 = patches.Ellipse(xy=(1,11),width=0.3,height=0.3,color='gray',fill='True')
open2 = patches.Ellipse(xy=(7,9),width=0.3,height=0.3,color='gray',fill='True')
ax1.add_artist(open1)
ax1.add_artist(open2)

comm_dict = [{'agent_state':'normal','raise_agent':[],'raise_event':[],'request_position':[],'estimate_time':[]} for n in range(0,len(agents_path))]

def dist(pose1,pose2):
    return ((pose1[0]-pose2[0])**2+(pose1[1]-pose2[1])**2)**0.5


def movement(): #放到一个类里面去
    #确定每个机器人点的运动，并判断是否需要发出req，rep，con信号
    #最早的请求时间
    Tm = float('inf')
    for i in range(0,agents_split[0]+1):
        #限定机器人视野为3，找第一个request，加入到所有机器人的消息队列中
        current_goal = goal_point_index[i]
        horizen = 3
        for j in range(0,horizen):
            current_goal = current_goal + 1
            #如果超过路径长度，重置为后缀第一个路径点
            if current_goal == len(agents_path[i]):
                current_goal = agents_path[i][0]
            if len(agents_path[i][current_goal]) > 3: #有request event raise
                #若消息队列中已经存在相应的event代号，直接break，但是应该返回index并更新对应的估计时间，这里先不更新了
                if agents_path[i][current_goal][2] in comm_dict[i]['raise_event']:
                    break
                #否则加入此新的事件
                else:
                    if (j+1)/agent_velocity[i]*20<Tm:
                        Tm = (j+1)/agent_velocity[i]*20
                    for item in comm_dict:
                        if item['agent_state'] == 'lock':
                            continue
                        item['raise_agent'].append(i)
                        item['raise_event'].append(agents_path[i][current_goal][2])
                        item['request_position'].append(agents_path[i][current_goal][3])
                        item['estimate_time'].append((j+1)/agent_velocity[i]*20) #单位为ms
                    break
#confirm事件之后再加
#            elif len(agents_path[i][current_goal]) == 3:#有confirm event raise
#                #若消息队列中已经存在相应的event代号，直接break，但是应该返回index并更新对应的估计时间，这里先不更新了
#                if agents_path[i][current_goal][2] in comm_dict[i]['raise_event']:
#                    break
#                #否则加入此新的事件
#                else:
#                    for item in comm_dict:
#                        item['raise_agent'].append(i)
#                        item['raise_event'].append(agents_path[i][current_goal][2])
#                        item['request_position'].append(agents_path[i][current_goal][3])
#                        item['estimate_time'].append(j+1)
#                    break
                    
    #确定谁去reply
    min_rep_dis = float('inf')
    min_rep_ind = -1   
    for i in range(agents_split[0]+1,agents_split[1]+1):
        #检查是否有还未相应的request
        has_req = 0
        for item in comm_dict[i]['raise_event']:
            if item[0:3] == 'req':
                has_req = 1
                break
        if has_req == 1:
            break
        
    if has_req == 1:
        for i in range(agents_split[0]+1,agents_split[1]+1):
            #锁定状态的机器人不能reply
            if comm_dict[i]['agent_state'] == 'lock':
                continue
            #计算代价
            rep_dis = abs(abs(agents_list[i].center[0]-1)+abs(agents_list[i].center[1]-11)-Tm)+10*(abs(agents_list[i].center[0]-1)+abs(agents_list[i].center[1]-11))
            if rep_dis < min_rep_dis:
                min_rep_dis = rep_dis
                min_rep_ind = i
                
    #锁定该机器人，删除request，改变goal——position，寄存当前goalposition
    
    
        #添加req，rep，con的机制
        
        
        #多个req能否一个rep解决
        
        
        #rep，req后的动作控制
        
        
        #防长时间占用
        
    if len(agents_path[0][goal_point_index[0]])==3 and len(req_list)==0:
        req_list.append('req')
    if len(agents_path[1][goal_point_index[1]])==3 and 'rep1' not in rep_list and dist(agent2.center,agents_path[1][goal_point_index[1]])<0.01:
        rep_list.append('rep1')
    if len(agents_path[2][goal_point_index[2]])==3 and 'rep2' not in rep_list and dist(agent3.center,agents_path[2][goal_point_index[2]])<0.01:
        rep_list.append('rep2')
    if dist(agent1.center,(4,4))<0.5 and len(con_list)==0:
        con_list.append('con')
        
    agent1_incre = [0,0]
    agent2_incre = [0,0]  
    agent3_incre = [0,0]  
    
    if len(req_list)==0 or (len(req_list)!=0 and len(rep_list)==2):#agent1可以继续前进
        if agent1.center[0] < agents_path[0][goal_point_index[0]][0]:
            agent1_incre[0] = 0.02
        elif agent1.center[0] > agents_path[0][goal_point_index[0]][0]:
            agent1_incre[0] = -0.02
        else:
            agent1_incre[0] = 0
        if agent1.center[1] < agents_path[0][goal_point_index[0]][1]:
            agent1_incre[1] = 0.02
        elif agent1.center[1] > agents_path[0][goal_point_index[0]][1]:
            agent1_incre[1] = -0.02
        else:
            agent1_incre[1] = 0
    else:
        agent1_incre = [0,0]
    
    if len(req_list)==0 or (len(req_list)!=0 and len(con_list)!=0) or (len(req_list)!=0 and 'rep1' not in rep_list):#agent2可以继续前进
        if agent2.center[0] < agents_path[1][goal_point_index[1]][0]:
            agent2_incre[0] = 0.01
        elif agent2.center[0] > agents_path[1][goal_point_index[1]][0]:
            agent2_incre[0] = -0.01
        else:
            agent2_incre[0] = 0
        if agent2.center[1] < agents_path[1][goal_point_index[1]][1]:
            agent2_incre[1] = 0.01
        elif agent2.center[1] > agents_path[1][goal_point_index[1]][1]:
            agent2_incre[1] = -0.01
        else:
            agent2_incre[1] = 0
    else:
        agent2_incre = [0,0]
        
    if len(req_list)==0 or (len(req_list)!=0 and len(con_list)!=0) or (len(req_list)!=0 and 'rep2' not in rep_list):#agent3可以继续前进
        if agent3.center[0] < agents_path[2][goal_point_index[2]][0]:
            agent3_incre[0] = 0.01
        elif agent3.center[0] > agents_path[2][goal_point_index[2]][0]:
            agent3_incre[0] = -0.01
        else:
            agent3_incre[0] = 0
        if agent3.center[1] < agents_path[2][goal_point_index[2]][1]:
            agent3_incre[1] = 0.01
        elif agent3.center[1] > agents_path[2][goal_point_index[2]][1]:
            agent3_incre[1] = -0.01
        else:
            agent3_incre[1] = 0
    else:
        agent3_incre = [0,0]
    
    
    if dist(agent1.center,agents_path[0][goal_point_index[0]])<0.03 and goal_point_index[0]+1<len(agents_path[0]):
        goal_point_index[0] = goal_point_index[0]+1
    if dist(agent2.center,agents_path[1][goal_point_index[1]])<0.01 and goal_point_index[1]+1<len(agents_path[1]):
        goal_point_index[1] = goal_point_index[1]+1
    if dist(agent3.center,agents_path[2][goal_point_index[2]])<0.01 and goal_point_index[2]+1<len(agents_path[2]):
        goal_point_index[2] = goal_point_index[2]+1
        
    return [agent1_incre,agent2_incre,agent3_incre]

def update(i):
    label = 'timestep {0}'.format(i)
    #确定机器人新位置
    agent_incre = movement()
    agent1.center = (agent1.center[0]+agent_incre[0][0],agent1.center[1]+agent_incre[0][1])
    agent2.center = (agent2.center[0]+agent_incre[1][0],agent2.center[1]+agent_incre[1][1])
    agent3.center = (agent3.center[0]+agent_incre[2][0],agent3.center[1]+agent_incre[2][1])
    #确定门，货物等物品状态
    if dist(agent2.center,open1.center)<0.02 and dist(agent3.center,open2.center)<0.02:
        door.set_linewidth('0')
    else:
        door.set_linewidth('5')
        
    if dist(agent1.center,good.center)<0.03:
        good.center = agent1.center
    
    if dist(agent1.center,[4,4])<0.1:
        good.set_color('red')
        
    if dist(agent2.center,open1.center)<0.02:
        open1.set_color('yellow')
    else:
        open1.set_color('gray')  
        
    if dist(agent3.center,open2.center)<0.02:
        open2.set_color('yellow')
    else:
        open2.set_color('gray')   
    
    repaint = (door,agent1,agent2,agent3,good,open1,open2)
    ax1.set_xlabel(label)    
    return repaint, ax1

# FuncAnimation 会在每一帧都调用“update” 函数。
# 在这里设置一个10帧的动画，每帧之间间隔200毫秒
anim = FuncAnimation(fig1, update, frames=np.arange(0, 1000), interval=20)

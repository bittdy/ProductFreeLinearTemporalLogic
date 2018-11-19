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
from matplotlib.pyplot import savefig
from matplotlib.lines import Line2D
from matplotlib.animation import FuncAnimation 
import csv
result = open('Result.csv','w+')
csv_write = csv.writer(result)
csv_write.writerow(["agent_id","timestep","agent_color","comm_dict"])
#仿真参数为间隔20ms
interval = 20
#机器人视野
agent_horizon = [3,5]
#机器人速度
agent_velocity = [0.02,0.04,0.02,0.02,0.02,0.02,0.02,0.02,0.02,0.02,0.02,0.02,0.02,0.02]
#机器人颜色
agent_color = ['red','red','silver','silver','silver','silver','silver','silver','silver','silver','silver','silver','silver','silver']
#机器人分组
agents_split = [1,7,13]
#构建机器人运动序列
agents_path = [[ 5,(4,0),(4,1),(4,2),(4,3),(4,4),(4,5),(4,6),(4,7),(4,8),(4,9),(4,10),(4,11),(5,11,'req_1',[(1,11),(7,9)]),(6,11),(7,11,'con_1'),(8,11),(7,11,'req_2',[(1,11),(7,9)]),(6,11),(5,11,'con_2'),(4,11),(4,10),(4,9),(4,8),(4,7),(4,6),(4,5),(4,4),(4,3) ], #agent1-2 goods depot
               [ 2,(8,11),(7,11,'req_2',[(1,11),(7,9)]),(6,11),(5,11,'con_2'),(4,11),(4,10),(4,9),(4,8),(4,7),(4,6),(4,5),(4,4),(4,3),(4,4),(4,5),(4,6),(4,7),(4,8),(4,9),(4,10),(4,11),(5,11,'req_1',[(1,11),(7,9)]),(6,11),(7,11,'con_1'),(8,11) ],
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
current_point_index = [1 for i in range(0,len(agents_path))]
agents_incre = [[0,0] for i in range(0,len(agents_path))]
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
    if i in range(0,agents_split[0]+1):
        agent = patches.Ellipse(xy=(agents_path[i][1][0],agents_path[i][1][1]),width=0.3,height=0.3,color='r',fill='True')
    if i in range(agents_split[0]+1,agents_split[1]+1):
        agent = patches.Ellipse(xy=(agents_path[i][1][0],agents_path[i][1][1]),width=0.3,height=0.3,color='silver',fill='True')
    if i in range(agents_split[1]+1,agents_split[2]+1):
        agent = patches.Ellipse(xy=(agents_path[i][1][0],agents_path[i][1][1]),width=0.3,height=0.3,color='silver',fill='True')
    ax1.add_artist(agent)
    agents_list.append(agent)
#文字，在之后的动画中的那一帧加
#门
door = Line2D((6,6),(10.53,11.5),linewidth='5',color='gray')
ax1.add_line(door)
#通信线
line1 = Line2D((6,6),(10.53,11.5),linewidth='0',color='red')
line2 = Line2D((6,6),(10.53,11.5),linewidth='0',color='red')
line3 = Line2D((6,6),(10.53,11.5),linewidth='0',color='red')
line4 = Line2D((6,6),(10.53,11.5),linewidth='0',color='red')
ax1.add_line(line1)
ax1.add_line(line2)
ax1.add_line(line3)
ax1.add_line(line4)
##货物
good = patches.Ellipse(xy=(4,3),width=0.15,height=0.15,color='green',fill='True')
ax1.add_artist(good)
##开关
open1 = patches.Ellipse(xy=(1,11),width=0.3,height=0.3,color='gray',fill='True')
open2 = patches.Ellipse(xy=(7,9),width=0.3,height=0.3,color='gray',fill='True')
ax1.add_artist(open1)
ax1.add_artist(open2)

comm_dict = [{'agent_state':'normal','raise_agent':[],'raise_event':[],'request_position':[],'estimate_time':[]} for n in range(0,len(agents_path))]

def dist(pose1,pose2):
    return ((pose1[0]-pose2[0])**2+(pose1[1]-pose2[1])**2)**0.5

def get_incre(pose1,pose2,index):
    agent_incre = [0,0]
    go_next = 0
    if pose1[1]-pose2[1]>0.001:
        agent_incre = [0,-(agent_velocity[index])]
        return agent_incre,go_next
    elif pose1[1]-pose2[1]<-0.001:
        agent_incre = [0,agent_velocity[index]]
        return agent_incre,go_next
    elif pose1[0]-pose2[0]>0.001:
        agent_incre = [-(agent_velocity[index]),0]
        return agent_incre,go_next
    elif pose1[0]-pose2[0]<-0.001:
        agent_incre = [agent_velocity[index],0]
        return agent_incre,go_next
    else:
        agent_incre = [0,0]
        go_next = 1
        return agent_incre,go_next
    
def movement(): #放到一个类里面去
    #确定每个机器人点的运动，并判断是否需要发出req，rep，con信号
    #最早的请求时间
    Tm = float('inf')
    event = ''
    raise_agent = -1

    for i in range(0,agents_split[0]+1):
        #限定机器人视野为3，找第一个request，加入到所有机器人的消息队列中
        current_goal = goal_point_index[i]
        horizen = agent_horizon[i]
        #如果已经有req了，直接continue
        if i in comm_dict[i]['raise_agent']:
            continue
        for j in range(0,horizen):
            current_goal = goal_point_index[i] + j
            #如果超过路径长度，重置为后缀第一个路径点
            if current_goal >= len(agents_path[i]):
                current_goal = agents_path[i][0]
            if len(agents_path[i][current_goal]) > 3: #有request event raise
                #若消息队列中已经存在相应的event代号，直接break，但是应该返回index并更新对应的估计时间，这里先不更新了
                if agents_path[i][current_goal][2] in comm_dict[i]['raise_event']:
                    break
                #否则加入此新的事件
                else:
                    if (j+1)/agent_velocity[i]*20<Tm:
                        Tm = (j+1)/agent_velocity[i]*20
                        event = agents_path[i][current_goal][2]
                        raise_agent = i
                    #加入到本机器人消息队列
                    comm_dict[i]['raise_agent'].append(i)
                    comm_dict[i]['raise_event'].append(agents_path[i][current_goal][2])
                    comm_dict[i]['request_position'].append(agents_path[i][current_goal][3])
                    comm_dict[i]['estimate_time'].append((j+1)/agent_velocity[i]*20) #单位为ms
                    #加入到协作机器人消息队列，如果已经有机器人lock则直接加入到该机器人中
                    lock_agent = []
                    for nn in range(2,len(comm_dict)):
                        if comm_dict[nn]['agent_state'] == 'lock':
                            lock_agent.append(nn)
                    #没有lock机器人，全部加入消息队列
                    if len(lock_agent) == 0:
                        for t in range(2,len(comm_dict)):
#                            if comm_dict[t]['agent_state'] == 'lock':
#                                continue
                            comm_dict[t]['raise_agent'].append(i)
                            comm_dict[t]['raise_event'].append(agents_path[i][current_goal][2])
                            comm_dict[t]['request_position'].append(agents_path[i][current_goal][3])
                            #estimate_time的计算可能有问题
                            comm_dict[t]['estimate_time'].append((j+1)/agent_velocity[i]*20) #单位为ms
                        break
                    else:
                        for item in lock_agent:
                            comm_dict[item]['raise_agent'].append(i)
                            comm_dict[item]['raise_event'].append(agents_path[i][current_goal][2])
                            comm_dict[item]['request_position'].append(agents_path[i][current_goal][3])
                            #estimate_time的计算可能有问题
                            comm_dict[item]['estimate_time'].append((j+1)/agent_velocity[i]*20) #单位为ms
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
                    
                
    #若有多个request，Tm相隔很近，直接给lock的机器人，同时lock机器人变为normal的条件也要变，是所有对应的req都没有了才能变
    
    
    
    #确定谁去reply，机器人集群1
    min_rep_dis1 = float('inf')
    min_rep_ind1 = -1   
    for i in range(agents_split[0]+1,agents_split[1]+1):
        #检查是否有还未相应的request
        has_req = 0
        if comm_dict[i]['agent_state'] == 'lock':
            continue
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
            rep_dis = abs(abs(agents_list[i].center[0]-1)+abs(agents_list[i].center[1]-11)-Tm)+1000*(abs(agents_list[i].center[0]-1)+abs(agents_list[i].center[1]-11))
            if rep_dis < min_rep_dis1:
                min_rep_dis1 = rep_dis
                min_rep_ind1 = i
            #锁定该机器人，删除request，改变goal——position，寄存当前goalposition
        if min_rep_ind1 != -1:
            comm_dict[min_rep_ind1]['agent_state'] = 'lock'
            goal_point_index[min_rep_ind1] = (1,11)       

    for i in range(agents_split[0]+1,agents_split[1]+1): 
        #先在响应的机器人中保留req信息，方便rep时向指定机器人发送消息，在rep时再删掉对应的req
        if i==min_rep_ind1:
            continue
        if raise_agent == -1:
            break
        if comm_dict[i]['agent_state'] == 'lock':
            continue
        if raise_agent in comm_dict[i]['raise_agent']:
            _index = comm_dict[i]['raise_agent'].index(raise_agent)
            comm_dict[i]['raise_agent'].pop(_index)
            comm_dict[i]['raise_event'].pop(_index)
            comm_dict[i]['request_position'].pop(_index)
            comm_dict[i]['estimate_time'].pop(_index)
        
        
    #机器人集群2
    min_rep_dis2 = float('inf')
    min_rep_ind2 = -1 
    for i in range(agents_split[1]+1,agents_split[2]+1):
        #检查是否有还未相应的request
        has_req = 0
        if comm_dict[i]['agent_state'] == 'lock':
            continue
        for item in comm_dict[i]['raise_event']:
            if item[0:3] == 'req':
                has_req = 1
                break
        if has_req == 1:
            break
        
    if has_req == 1:
        for i in range(agents_split[1]+1,agents_split[2]+1):
            #锁定状态的机器人不能reply
            if comm_dict[i]['agent_state'] == 'lock':
                continue
            #计算代价
            rep_dis = abs(abs(agents_list[i].center[0]-1)+abs(agents_list[i].center[1]-11)-Tm)+1000*(abs(agents_list[i].center[0]-1)+abs(agents_list[i].center[1]-11))
            if rep_dis < min_rep_dis2:
                min_rep_dis2 = rep_dis
                min_rep_ind2 = i
        if min_rep_ind2 != -1:        
            #锁定该机器人，删除request，改变goal——position，寄存当前goalposition
            comm_dict[min_rep_ind2]['agent_state'] = 'lock'
            goal_point_index[min_rep_ind2] = (7,9)
    for i in range(agents_split[1]+1,agents_split[2]+1): 
        #先在响应的机器人中保留req信息，方便rep时向指定机器人发送消息，在rep时再删掉对应的req
        if event == '':
            break
        if i==min_rep_ind2:
            continue
        if comm_dict[i]['agent_state'] == 'lock':
            continue
        if raise_agent in comm_dict[i]['raise_agent']:
            _index = comm_dict[i]['raise_agent'].index(raise_agent)
            comm_dict[i]['raise_agent'].pop(_index)
            comm_dict[i]['raise_event'].pop(_index)
            comm_dict[i]['request_position'].pop(_index)
            comm_dict[i]['estimate_time'].pop(_index)
        
    #检测是否有机器人在开门处，并记录该机器人序号
    reply_1 = -1
    reply_2 = -1
    for tt in range(agents_split[0]+1,agents_split[1]+1):    
        if dist(agents_list[tt].center,open1.center)<0.001:
            reply_1 = tt
            break
    
    for tt in range(agents_split[1]+1,agents_split[2]+1):    
        if dist(agents_list[tt].center,open2.center)<0.001:
            reply_2 = tt
            break
        
    #检测是否有机器人在req处，记录req机器人标号
    requ = []
    requ_event = []
    for ll in range(0,2):
        if dist(agents_list[ll].center,(5,11))<0.001 and not (ll in requ and 'req_1' in requ_event):
            requ.append(ll)
            requ_event.append('req_1')
        elif dist(agents_list[ll].center,(7,11))<0.001 and not (ll in requ and 'req_2' in requ_event):
            requ.append(ll)
            requ_event.append('req_2')
    
    #如果到达open点，向指定的机器人发送rep，同时删除本身所存的req信息，有两个以上req同时时这里要重写
    #不要在这里删除req信息，在con之后再删
    if reply_1 != -1:
        for c in range(0,len(requ)):
            #判断是否已经在第一次到达时处理过消息
            if len(comm_dict[requ[c]]['raise_event'])!= 0 and not (reply_1 in comm_dict[requ[c]]['raise_agent'] and 'rep_1' in comm_dict[requ[c]]['raise_event'] and comm_dict[requ[c]]['raise_agent'].index(reply_1) == comm_dict[requ[c]]['raise_event'].index('rep_1')):
                comm_dict[requ[c]]['raise_event'].append('rep_1')
                comm_dict[requ[c]]['raise_agent'].append(reply_1)
                comm_dict[requ[c]]['request_position'].append((1,11))
                comm_dict[requ[c]]['estimate_time'].append(0)
                
#                _index = comm_dict[reply_1]['raise_agent'].index(requ[c])
#                comm_dict[reply_1]['raise_event'].pop(_index)
#                comm_dict[reply_1]['raise_agent'].pop(_index)
#                comm_dict[reply_1]['request_position'].pop(_index)
#                comm_dict[reply_1]['estimate_time'].pop(_index)

    if reply_2 != -1:      
        for c in range(0,len(requ)):
            #判断是否已经在第一次到达时处理过消息
            if len(comm_dict[requ[c]]['raise_event'])!= 0 and not (reply_2 in comm_dict[requ[c]]['raise_agent'] and 'rep_2' in comm_dict[requ[c]]['raise_event'] and comm_dict[requ[c]]['raise_agent'].index(reply_2) == comm_dict[requ[c]]['raise_event'].index('rep_2')):
                comm_dict[requ[c]]['raise_event'].append('rep_2')
                comm_dict[requ[c]]['raise_agent'].append(reply_2)
                comm_dict[requ[c]]['request_position'].append((7,9))
                comm_dict[requ[c]]['estimate_time'].append(0)
            
#                _index = comm_dict[reply_2]['raise_agent'].index(requ[c])
#                comm_dict[reply_2]['raise_event'].pop(_index)
#                comm_dict[reply_2]['raise_agent'].pop(_index)
#                comm_dict[reply_2]['request_position'].pop(_index)
#                comm_dict[reply_2]['estimate_time'].pop(_index)
        
    #如果机器人con，删掉自身所存的req和rep，恢复协作机器人目标点，解除lock，要匹配是哪个req
    #恢复协作机器人目标点要加一步检测，是否没有req了
    
    for p in range(0,2):
        cop_req = ''
        if dist(agents_list[p].center,(7,11))<0.001 and 'req_1' in comm_dict[p]['raise_event']:
            cop_req = 'req_1'
        elif dist(agents_list[p].center,(5,11))<0.001 and 'req_2' in comm_dict[p]['raise_event']:
            cop_req = 'req_2'
        if cop_req == '':
            continue
        _index = comm_dict[p]['raise_event'].index(cop_req)
        comm_dict[p]['raise_event'].pop(_index)
        comm_dict[p]['raise_agent'].pop(_index)
        comm_dict[p]['request_position'].pop(_index)
        comm_dict[p]['estimate_time'].pop(_index)
        
#        if p not in comm_dict[p]['raise_agent']:
#            #本机已无req，清空所有
#        comm_dict[p]['raise_event'].pop(_index)
#        comm_dict[p]['raise_agent'].pop(_index)
#        comm_dict[p]['request_position'].pop(_index)
#        comm_dict[p]['estimate_time'].pop(_index)
        
        if reply_2 != -1:
            cop_index = comm_dict[reply_1]['raise_event'].index(cop_req)
            comm_dict[reply_1]['raise_event'].pop(cop_index)
            comm_dict[reply_1]['raise_agent'].pop(cop_index)
            comm_dict[reply_1]['request_position'].pop(cop_index)
            comm_dict[reply_1]['estimate_time'].pop(cop_index)
            
        if reply_2 != -1:
            cop_index = comm_dict[reply_2]['raise_event'].index(cop_req)
            comm_dict[reply_2]['raise_event'].pop(cop_index)
            comm_dict[reply_2]['raise_agent'].pop(cop_index)
            comm_dict[reply_2]['request_position'].pop(cop_index)
            comm_dict[reply_2]['estimate_time'].pop(cop_index)
        
        _index = comm_dict[p]['raise_event'].index('rep_1')
#        if len(comm_dict[comm_dict[p]['raise_agent'][_index]]['raise_event']) == 0:
#            comm_dict[comm_dict[p]['raise_agent'][_index]]['agent_state'] = 'normal'
#            goal_point_index[comm_dict[p]['raise_agent'][_index]] = agents_path[comm_dict[p]['raise_agent'][_index]].index((1,9))
        if len(comm_dict[reply_1]['raise_event']) == 0:
            comm_dict[reply_1]['agent_state'] = 'normal'
            goal_point_index[reply_1] = agents_path[comm_dict[p]['raise_agent'][_index]].index((1,9))
        comm_dict[p]['raise_event'].pop(_index)
        comm_dict[p]['raise_agent'].pop(_index)
        comm_dict[p]['request_position'].pop(_index)
        comm_dict[p]['estimate_time'].pop(_index)   

        
        _index = comm_dict[p]['raise_event'].index('rep_2')
#        if len(comm_dict[comm_dict[p]['raise_agent'][_index]]['raise_event']) == 0:
#            comm_dict[comm_dict[p]['raise_agent'][_index]]['agent_state'] = 'normal'
#            goal_point_index[comm_dict[p]['raise_agent'][_index]] = agents_path[comm_dict[p]['raise_agent'][_index]].index((7,7))
        if len(comm_dict[reply_2]['raise_event']) == 0:
            comm_dict[reply_2]['agent_state'] = 'normal'
            goal_point_index[reply_2] = agents_path[comm_dict[p]['raise_agent'][_index]].index((7,7))

        comm_dict[p]['raise_event'].pop(_index)
        comm_dict[p]['raise_agent'].pop(_index)
        comm_dict[p]['request_position'].pop(_index)
        comm_dict[p]['estimate_time'].pop(_index)      
        
        
        #rep，req后的动作控制，要判断目标点是元组还是整数
    for m in range(0,2):
        #可以走向下一个点
        if len(agents_path[m][current_point_index[m]])!=4 or (len(agents_path[m][current_point_index[m]])==4 and 'rep_1' in comm_dict[m]['raise_event'] and 'rep_2' in comm_dict[m]['raise_event']):
            agents_incre[m],go_next = get_incre(agents_list[m].center,agents_path[m][goal_point_index[m]],m)
            if go_next == 1:
                current_point_index[m] = goal_point_index[m]
                goal_point_index[m] = goal_point_index[m] + 1
                if goal_point_index[m] == len(agents_path[m]):
                    goal_point_index[m] = agents_path[m][0]
        else:
            agents_incre[m] = [0,0]
        
    for n in range(2,len(agents_path)):
        if isinstance(goal_point_index[n],tuple):
            agents_incre[n],go_next = get_incre(agents_list[n].center,goal_point_index[n],n)
        else:
            agents_incre[n],go_next = get_incre(agents_list[n].center,agents_path[n][goal_point_index[n]],n)
            if go_next == 1:
                goal_point_index[n] = goal_point_index[n] + 1
                if goal_point_index[n] == len(agents_path[n]):
                    goal_point_index[n] = agents_path[n][0]
    #print(comm_dict)

    return agents_incre

def update(i):
    label = 'timestep {0}'.format(i)
    #确定机器人新位置
    agents_incre = movement()
    for p in range(0,agents_split[0]+1):
        agents_list[p].center = (agents_list[p].center[0]+agents_incre[p][0],agents_list[p].center[1]+agents_incre[p][1])
        if p in comm_dict[p]['raise_agent']:
            agents_list[p].set_color('deepskyblue')
            raise_agent_str=[str(z) for z in comm_dict[p]['raise_agent']]
            fistr = " ".join(raise_agent_str)
            result_string = ['%d'%p,'%d'%i,'deepskyblue',fistr]
        else:
            agents_list[p].set_color(agent_color[p])
            raise_agent_str=[str(z) for z in comm_dict[p]['raise_agent']]
            fistr = " ".join(raise_agent_str)
            result_string = ['%d'%p,'%d'%i,agent_color[p],fistr]
        csv_write.writerow(result_string)
    for p in range(agents_split[0]+1,agents_split[2]+1):
        agents_list[p].center = (agents_list[p].center[0]+agents_incre[p][0],agents_list[p].center[1]+agents_incre[p][1])
        if comm_dict[p]['agent_state'] == 'lock':
            agents_list[p].set_color('black')
            raise_agent_str=[str(z) for z in comm_dict[p]['raise_agent']]
            fistr = " ".join(raise_agent_str)
            result_string = ['%d'%p,'%d'%i,'black',fistr]
        else:
            agents_list[p].set_color(agent_color[p])
            raise_agent_str=[str(z) for z in comm_dict[p]['raise_agent']]
            fistr = " ".join(raise_agent_str)
            result_string = ['%d'%p,'%d'%i,agent_color[p],fistr]
        csv_write.writerow(result_string)       
    co = 0
    line1.set_linewidth(0)
    line2.set_linewidth(0)
    line3.set_linewidth(0)
    line4.set_linewidth(0)
    for t in range(0,agents_split[0]+1):
        for z in range(agents_split[0]+1,agents_split[2]+1):
            if t in comm_dict[t]['raise_agent'] and t in comm_dict[z]['raise_agent']:
                if co==0:
                    line1.set_linewidth(1)
                    line1.set_xdata([agents_list[t].center[0],agents_list[z].center[0]])
                    line1.set_ydata([agents_list[t].center[1],agents_list[z].center[1]])
                    co = co+1
                elif co==1:
                    line2.set_linewidth(1)
                    line2.set_xdata([agents_list[t].center[0],agents_list[z].center[0]])
                    line2.set_ydata([agents_list[t].center[1],agents_list[z].center[1]])
                    co = co+1
                elif co==2:
                    line3.set_linewidth(1)
                    line3.set_xdata([agents_list[t].center[0],agents_list[z].center[0]])
                    line3.set_ydata([agents_list[t].center[1],agents_list[z].center[1]])
                    co = co+1
                elif co==3:
                    line4.set_linewidth(1)
                    line4.set_xdata([agents_list[t].center[0],agents_list[z].center[0]])
                    line4.set_ydata([agents_list[t].center[1],agents_list[z].center[1]])
                    co = co+1
    #print(agents_list[0].center)
    #确定门，货物等物品状态
    open1_on = 0
    open2_on = 0
    for t in range(agents_split[0]+1,agents_split[1]+1):    
        if dist(agents_list[t].center,open1.center)<0.001:
            open1.set_color('yellow')
            open1_on = 1
            break
        else:
            open1.set_color('gray')
            open1_on = 0
    
    for t in range(agents_split[1]+1,agents_split[2]+1):    
        if dist(agents_list[t].center,open2.center)<0.001:
            open2.set_color('yellow')
            open2_on = 1
            break
        else:
            open2.set_color('gray')
            open2_on = 0
            
    if open1_on == 1 and open2_on == 1:
        door.set_linewidth('0')
    else:
        door.set_linewidth('5')
    
    #for t in range(0,2)
     #   if dist(agent1.center,good.center)<0.03:
      #      good.center = agent1.center
    
    #if dist(agent1.center,[4,4])<0.1:
     #   good.set_color('red')
        
 
    
    repaint = (door,agents_list,open1,open2)
    ax1.set_xlabel(label)    
    return repaint, ax1

 #FuncAnimation 会在每一帧都调用“update” 函数。
 #在这里设置一个10帧的动画，每帧之间间隔200毫秒
anim = FuncAnimation(fig1, update, frames=np.arange(0, 10000), interval=20)
    
#if __name__ == '__main__':
#    i = 0
#    while(1):
#        print(i)
#        update(i)
#        savefig('D:/debug/'+str(i)+'.jpg')
#        #print(i)
#        i = i+1

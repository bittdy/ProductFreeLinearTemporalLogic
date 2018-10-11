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
from matplotlib.animation import FuncAnimation  # 动图的核心函数
#构建机器人运动序列

#创建画布
fig1 = plt.figure()
ax1 = fig1.add_subplot(111, aspect='equal')
ax1.set_xlim(left = -0.5,right = 4.5)
ax1.set_ylim(bottom = -0.5,top = 4.5)
# 画出维持不变的实验环境以及要变的那些对象的初始位置
#矩形构成的试验环境，蓝色为障碍物，白色为正常区域
ax1.add_patch(patches.Rectangle((0.5,0.5),1,3))
ax1.add_patch(patches.Rectangle((2.5,0.5),1,3))
ax1.add_patch(patches.Rectangle((3.5,2.5),1,1))
ax1.add_patch(patches.Rectangle((3.7,3.7),0.6,0.6))
xyrange = np.arange(5)+0.5
for i in xyrange:
    ax1.axhline(y = i,linestyle = '--')
    ax1.axvline(x = i,linestyle = '--')
##圆构成的机器人
agent1 = patches.Ellipse(xy=(2,0.3),width=0.3,height=0.3,color='r',fill='True')
agent2 = patches.Ellipse(xy=(1.7,0),width=0.3,height=0.3,color='r',fill='True')
agent3 = patches.Ellipse(xy=(2.3,0),width=0.3,height=0.3,color='r',fill='True')
ax1.add_artist(agent1)
ax1.add_artist(agent2)
ax1.add_artist(agent3)
#文字，在之后的动画中的那一帧加
#门
door = Line2D((3,3),(3.53,4.5),linewidth='5',color='gray')
ax1.add_line(door)
#货物
good = patches.Ellipse(xy=(2,2),width=0.15,height=0.15,color='green',fill='True')
ax1.add_artist(good)
#开关
open1 = patches.Ellipse(xy=(0,4),width=0.3,height=0.3,color='gray',fill='True')
open2 = patches.Ellipse(xy=(4,2),width=0.3,height=0.3,color='gray',fill='True')
ax1.add_artist(open1)
ax1.add_artist(open2)
#def update(i):
#    label = 'timestep {0}'.format(i)
#    print(label)
#    # 更新直线和x轴（用一个新的x轴的标签）。
#    # 用元组（Tuple）的形式返回在这一帧要被重新绘图的物体
#    line.set_ydata(x - 5 + i)  # 这里是重点，更新y轴的数据
#    ax.set_xlabel(label)    # 这里是重点，更新x轴的标签
#    return repaint, ax
#
#
#def movement(): #放到一个类里面去
#    #确定每个机器人点的运动，并判断是否需要发出req，rep，con信号
#
#
## FuncAnimation 会在每一帧都调用“update” 函数。
## 在这里设置一个10帧的动画，每帧之间间隔200毫秒
#anim = FuncAnimation(fig, update, frames=np.arange(0, 10), interval=200)
#

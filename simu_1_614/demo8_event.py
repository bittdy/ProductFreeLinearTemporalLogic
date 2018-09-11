# export PYTHONPATH=$PYTHONPATH:/to/your/P_MAS_TG

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

#print(robot_motion.nodes())
#print(robot_motion.edges())

robot_motion_1 = robot_motion_2 = robot_motion

# specify tasks for each Agent

# search r4,r5,r6 after turn on the light, cannot enter the lock region before unlock
#agent_task_1 = '(<>(light && (<> (r4) && <> (r7 && <>r11) ))) && ([](!lock || unlock))'
#agent_task_1 = '<>(r8&&<>(r11&&r21&&r31))'

#agent_task_1 = '[](goods->Xdepot)&&[](depot->Xgoods)&&[](!b)&&[](!door||open)&&[]<>goods&&[]<>depot'
#agent_task_1 = '[](goods-><>depot)&&[](depot-><>goods)&&[](!b)&&[](!door||open)&&[]<>goods&&[]<>depot'
agent_task_1 = '[]<>depot&&[]<>goods&&[](!b)&&[](goods-><>depot)&&[](depot-><>goods)'
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

#print('guard:')
#for f in buchi_1.nodes():
#    for t in buchi_1.nodes():
#        print(f,t,buchi_1.edges[f,t]['guard'])


#print(buchi_1.nodes())
#print(buchi_1.edges())

pro_1 = ProdAut(robot_motion,buchi_1)
pro_1_static_list = pro_1.build_full()

print("product bian")
for item in pro_1.edges():
    print(item)
print("static bina")
for item in pro_1_static_list:
    print(item)

pro_2 = ProdAut(robot_motion,buchi_2)
pro_2_static_list = pro_2.build_full()

static_list = [pro_1_static_list,pro_2_static_list]

#print(pro_1.nodes())
#print(pro_1.edges())
#print(len(pro_1.nodes()))
#print(len(pro_1.edges()))

#fts mu qian zan shi she zhi wei yi yang de 
region_array = [regions1,regions2]
fts_array = [robot_motion_1,robot_motion_2]
buchi_array = [buchi_1,buchi_2]
pro_array = [pro_1,pro_2]
colla_ap = [['door'],['open']]

#print('state_list:')
#print(pro_1_static_list)
#for item in pro_1_static_list:
#    print(item)
#print(pro_2_static_list)
#print(type(pro_1_static_list[0][2]))

'''
for item in pro_1.edges():
    if item[0][0] == (2,3,1) or item[0][0] == (3,3,1) or item[1][0] == (2,3,1) or item[1][0] == (3,3,1):
        print(item)
        
'''
# 创建一个 8 * 8 点（point）的图，并设置分辨率为 80  
'''plt.figure(figsize=(50,50), dpi=80)  
  
# 创建一个新的 1 * 1 的子图，接下来的图样绘制在其中的第 1 块（也是唯一的一块）  
plt.subplot(1,1,1)  
  
#设置坐标轴  
ax = plt.gca()  
ax.spines['right'].set_color('none')  
ax.spines['top'].set_color('none')  
ax.yaxis.set_ticks_position('left')  
ax.spines['left'].set_position(('data',0))  

theta = np.linspace(0, 2*np.pi,800)  


for item in pro.nodes():
    
#画外圆  
x,y = np.cos(theta)*2, np.sin(theta)*2  
plt.plot(x, y, color='blue', linewidth=2.0)  
  
#画內圆  
x,y = np.cos(theta), np.sin(theta)  
plt.plot(x, y, color='red', linewidth=2.0)  
  
#填充环  
v = np.linspace(1.01,1.99,10)  
v.shape = (10, 1)  
x1 = v * x  
y1 = v * y  
plt.plot(x1, y1, color='yellow', linewidth=1.0)  
  
#填充內圆  
v = np.linspace(0,0.99,10)  
v.shape = (10, 1)  
x1 = v * x  
y1 = v * y  
plt.plot(x1, y1, color='green', linewidth=1, linestyle=':')  
  
  
# 在屏幕上显示  
plt.show()  
#planner = MultiLTLPlanner(robot_motion, agents_task_array)

# get each buchi from the ltl task spec array

#run = planner.optimal()

#paths_list = []

#for path in run.pre_plan:
#    paths_list.append(list(path))

#print 'event_trigger_condition ', trigger_condition

#print 'paths_list ',paths_list

#tt = check_robot_steps(trigger_condition, paths_list, regions_array)

#for zz in range(len(tt)):
#    print tt[zz]
'''
   

class multi_prod(DiGraph):
    def __init__(self,region_array,agent_prod_array,agent_fts_array,colla_ap,static_list):
        DiGraph.__init__(self, region_array = region_array, agent_prod_array = agent_prod_array, agent_fts_array = agent_fts_array, colla_ap = colla_ap, static_list = static_list,initial=set(), accept=set(), type='multi_prod')
        #structure: {(edge):[require_robot_index,responde_robot_index,require_position]}
        self.req_edges = {}
        
    def build_static(self):
        for agent_index in range(len(self.graph['agent_prod_array'])):  #对每一个机器人的product自动机
            for other_agent in range(len(self.graph['agent_prod_array'])):
                if agent_index == other_agent:
                    continue
                else:
                    #no collative task
                    if len(self.graph['colla_ap'][other_agent]) == 0: 
                        continue
                    else:
                        for ap_index in range(len(self.graph['colla_ap'][other_agent])):
                            #zai region zhong zhao dao suo you yu ap dui ying de qu yu dian
                            cor_pos_list = self.find_region(self.graph['colla_ap'][other_agent][ap_index],self.graph['region_array'][other_agent])
                            #zai fts zhao dao mei ge qu yu dian de qian ji yi ji cost, qu zui xiao de cun xia lai
                            cost_static = float('inf')
                            fts_digraph = DiGraph()
                            fts_digraph.add_edges_from(self.graph['agent_fts_array'][other_agent].edges())  
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
                            for static_edge in self.graph['static_list'][agent_index]:#shu ju jie guo de tong yi
                                #yao qiu colla_ap gei chu dui ying de dong zuo,bi ru door dui ying open,zhe ge ke yi tong guo ren wu de sheng ming fang shi jin xing zi dong shi bie? 
                                if self.graph['colla_ap'][agent_index][ap_index] in static_edge[2]:
                                    cost_local = distance(static_edge[0][0],static_edge[1][0])
                                    #print(static_edge[0])
                                    self.graph['agent_prod_array'][agent_index].add_edge(static_edge[0],static_edge[1],weight = cost_static+cost_local)
                                    self.req_edges[(static_edge[0][0],static_edge[1][0])] = [agent_index,other_agent,static_edge[2]]  #chuan ap?

                                    #duo ge ji qi ren shi ,cost wei mei ge ji qi ren cost de he,req_edges jie gou ye yao gai
                            
    def find_region(self,ap,region):
        cor_pos_list = [ap]
        for item in region:
            if ap in region[item]:
                    cor_pos_list.append(item)
        return cor_pos_list
    
    
    #def build_float(self):
        


p = multi_prod(region_array,pro_array,fts_array,colla_ap,static_list)
p.build_static()

#print('final result:')
#
#for item in p.graph['agent_prod_array'][0].edges():
#    print(item)
#    print(p.graph['agent_prod_array'][0][item[0]][item[1]]['weight'])
    
# set planner
#print(p.graph['agent_prod_array'][0].edges())

robot_planner = ltl_planner(p.graph['agent_prod_array'][0])

# synthesis
start = time.time()
robot_planner.optimal(10,'static')

print ('full construction and synthesis done within %.2fs \n' %(time.time()-start))

#    
#    
#    
#'''def build_float(self,loc_label,to_label):   #任务区域触发的工作去外面做，不在本函数内做，仅传进来两个标签建立float链接
#        for agent_index in range(len(self.graph['agent_prod_array'])):  #对每一个机器人的product自动机
#            for indi_edge in self.graph['agent_prod_array'][agent_index]:    #每一个自动机的每一条边
#                if indi_edge[0][0] == loc_label:                            #indi_edge[0][1]一定会出现在indi_edge[0][0]里吗？？
#                    for to_agent_index in range(len(self.graph['agent_prod_array'])):
#                        if agent_index == to_agent_index:
#                            continue
#                        else:
#                            for to_indi_edge in self.graph['agent_prod_array'][to_agent_index]:
#                                if to_indi_edge[0][0] == to_label:
#                                    self.add_edge(indi_edge[0], to_indi_edge[0], weight = cost * dist, label = 'float')
#                                    self.add_edge(to_indi_edge[0], indi_edge[0], weight = cost * dist, label = 'float')
#'''                                    '''
#if __name__=='__main__':
#    a = multi_prod(pro_array,buchi_array,fts_array)
#'''

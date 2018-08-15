# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 22:06:18 2018

@author: bittdy
"""

# -*- coding: utf-8 -*-


from math import sqrt
from networkx.classes.digraph import DiGraph

def distance(pose1, pose2):
    return (sqrt((pose1[0]-pose2[0])**2+(pose1[1]-pose2[1])**2)+0.001)

def reach_waypoint(pose, waypoint, margin):
    if distance(pose, waypoint)<=margin:
        return True
    else:
        return False

class MotionFts(DiGraph):
    def __init__(self, node_dict, symbols, ts_type):
        DiGraph.__init__(self, symbols=symbols, type=ts_type, initial=set())
        for (n, label) in node_dict.items():
            self.add_node(n, label=label, status='confirmed')
            

    def add_un_edges(self, edge_list, unit_cost=1):
        for edge in edge_list:
            f_node = edge[0]
            t_node = edge[1]
            dist = distance(f_node, t_node)
            self.add_edge(f_node, t_node, weight=dist*unit_cost)
            self.add_edge(t_node, f_node, weight=dist*unit_cost)
        for node in self.nodes():
            #self.add_edge(node, node, weight=unit_cost)
            # allow self-transit to 0-cost
            self.add_edge(node, node, weight=0)

    def add_un_edges_by_ap(self, edge_list, unit_cost=1):
        for edge in edge_list:            
            f_ap = edge[0]
            t_ap = edge[1]
            f_nodes = [n for n in self.nodes() if f_ap in self.node[n]['label']]
            if len(f_nodes)> 1:
                print('ambiguity more than one with f_ap %s, see %s' %(f_ap, str(f_nodes)))
            else:
                f_node = f_nodes[0]
            t_nodes = [n for n in self.nodes() if t_ap in self.node[n]['label']]
            if len(t_nodes)> 1:
                print('ambiguity more than one with t_ap %s, see %s' %(t_ap, str(t_nodes)))
            else:
                t_node = t_nodes[0]
            dist = distance(f_node, t_node)
            self.add_edge(f_node, t_node, weight=dist*unit_cost)
            self.add_edge(t_node, f_node, weight=dist*unit_cost)
        for node in self.nodes():
            #self.add_edge(node, node, weight=unit_cost)
            # allow self-transit to 0-cost
            self.add_edge(node, node, weight=0)            

    def add_full_edges(self,unit_cost=1):
        for f_node in self.nodes():
            for t_node in self.nodes():
                dist = distance(f_node, t_node)
                if (f_node, t_node) not in self.edges():
                    self.add_edge(f_node, t_node, weight=dist*unit_cost)

    def set_initial(self, pose):
        init_node = self.closest_node(pose)
        self.graph['initial'] = set([init_node])
        return init_node

    def closest_node(self, pose):
        node = min(self.nodes(), key= lambda n: distance(n,pose))
        return node

    


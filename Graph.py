#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  9 00:01:55 2022

@author: hunchoahmad
"""

#betweennness_centrality
from pathlib import Path

import networkx as nx

import matplotlib.pyplot as plt

import networkx as nx
import matplotlib.pyplot as plt
G_fbcent = nx.read_edgelist("/Users/hunchoahmad/Downloads/facebook_combined.TXT", create_using = nx.Graph(), nodetype = int)
print(nx.info(G_fbcent))

pos = nx.spring_layout(G_fbcent)
betCent = nx.betweenness_centrality(G_fbcent, normalized = True, endpoints = True)
node_color = [20000.0 * G_fbcent.degree(v) for v in G_fbcent]
node_size = [v * 10000 for v in betCent.values()]
plt.figure(figsize =(20,20))
nx.draw_networkx(G_fbcent, pos=pos, with_labels = False,
                 node_color=node_color,
                 node_size=node_size)

plt.axis('off')

sorted(betCent, key=betCent.get, reverse=True)[:10]

print(betCent)

#eigenvector_centrality
from pathlib import Path

import networkx as nx

import matplotlib.pyplot as plt

import networkx as nx
import matplotlib.pyplot as plt
G_fbcent = nx.read_edgelist("/Users/hunchoahmad/Downloads/facebook_combined.TXT", create_using = nx.Graph(), nodetype = int)
print(nx.info(G_fbcent))

pos = nx.spring_layout(G_fbcent)
betCent = nx.eigenvector_centrality(G_fbcent)
node_color = [20000.0 * G_fbcent.degree(v) for v in G_fbcent]
node_size = [v * 10000 for v in betCent.values()]
plt.figure(figsize =(20,20))
nx.draw_networkx(G_fbcent, pos=pos, with_labels = False,
                 node_color=node_color,
                 node_size=node_size)

plt.axis('off')

sorted(betCent, key=betCent.get, reverse=True)[:10]

print(betCent)


#deree_centralit
from pathlib import Path

import networkx as nx

import matplotlib.pyplot as plt

import networkx as nx
import matplotlib.pyplot as plt
G_fbcent = nx.read_edgelist("/Users/hunchoahmad/Downloads/facebook_combined.TXT", create_using = nx.Graph(), nodetype = int)
print(nx.info(G_fbcent))

pos = nx.spring_layout(G_fbcent)
betCent = nx.eigenvector_centrality(G_fbcent)
node_color = [20000.0 * G_fbcent.degree(v) for v in G_fbcent]
node_size = [v * 10000 for v in betCent.values()]
plt.figure(figsize =(20,20))
nx.draw_networkx(G_fbcent, pos=pos, with_labels = False,
                 node_color=node_color,
                 node_size=node_size)

plt.axis('off')

sorted(betCent, key=betCent.get, reverse=True)[:10]

print(betCent)



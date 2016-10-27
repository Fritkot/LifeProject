import networkx as nx 
import matplotlib.pyplot as plt 
G = nx.Graph() 
G.add_node('1') 
G.add_node('2') 
G.add_node('3') 
G.add_node('4') 
G.add_node('5') 
G.add_edge('1', '2') 
G.add_edge('2', '3') 
G.add_edge('3', '4') 
G.add_edge('4', '1') 
G.add_edge('4', '5') 
nx.draw_spectral(G) 
plt.show()

G = nx.Graph()

for n in extraitListNoeuds(sousGraphe):
    G.add_node(n)

for arrete in sousGraphe.keys():
    G.add_edge(arrete[0],arrete[1])
nx.draw_spectral(G)
plt.show()

G = nx.Graph()
acm = kruskall(sousGraphe)
# for n in extraitListNoeuds(acm):
#     G.add_node(n)

for arrete in acm.keys():
    G.add_edge(arrete[0],arrete[1],weight = acm[arrete])
# nx.draw_spectral(G)
edge_labels=dict([((u,v,),d['weight'])
                 for u,v,d in G.edges(data=True)])
pos=nx.spring_layout(G)
nx.draw_networkx_edge_labels(G,pos,edge_labels=edge_labels)
nx.draw(G,pos, node_size=1500,edge_cmap=plt.cm.Reds)
import pylab
pylab.show()
# plt.show()
import networkx as nx 
import matplotlib.pyplot as plt 

G = nx.Graph()
G.add_node(1)
G.add_nodes_from([2,3])
G.add_edge(1,2)
G.add_edge(2,3)
G.add_edge(1,3)

nx.draw(G, with_labels=True, font_weight = 'bold')
plt.show()

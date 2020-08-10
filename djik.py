import matplotlib.pyplot as plt 
import networkx as nx
import time


G = nx.Graph()


G.add_nodes_from(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'])
G.add_edges_from([
                    ('A', 'B', {'weight': 8}),
                    ('A', 'C', {'weight': 2}),
                    ('B', 'D', {'weight': 2}),
                    ('C', 'D', {'weight': 2}),
                    ('C', 'E', {'weight': 5}),
                    ('D', 'E', {'weight': 1}),
                    ('E', 'G', {'weight': 1}),
                    ('G', 'F', {'weight': 2}),
                    ('G', 'H', {'weight': 6}),
                    ('F', 'H', {'weight': 3}),
                    ('D', 'F', {'weight': 6}),
                    ('B', 'F', {'weight': 13}),
                ])

L = nx.spring_layout(G)


shortestDistanceMap = {
                        'A': (None, 0),
                        'B': (None, float('inf')),
                        'C': (None, float('inf')),
                        'D': (None, float('inf')),
                        'E': (None, float('inf')),
                        'F': (None, float('inf')),
                        'G': (None, float('inf')),
                        'H': (None, float('inf'))
                      }

nodeList = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

nx.draw(G, pos = L, with_labels=True, font_weight="bold")


start = 'A'
end = 'F'

toVisit = start #Start with A
visited = []

while True:
    x = toVisit
    visited.append(x)

    minDist = float('inf')
    minDistNode = None

    for y in G[x]:
        calculated = G[x][y]['weight'] + shortestDistanceMap[x][1]
        if y not in visited:

            #Plot this edge as being considered
            nx.draw_networkx_edges(G, L, edgelist=[(x, y)], width=8, edge_color='b', alpha=0.2)
            plt.pause(1e-17)

            #Calculate and update
            if calculated <= shortestDistanceMap[y][1]:
                shortestDistanceMap[y] = (x, calculated)
            
            if calculated < minDist:
                minDist = calculated
                minDistNode = y
    
    time.sleep(0.75)

    if minDistNode != None:
        #Draw selected node
        nx.draw_networkx_edges(G, L, edgelist=[(x, minDistNode)], width=8, edge_color='b', alpha=0.5)
        plt.pause(1e-17)

        #Go to min node
        toVisit = minDistNode
    else:
        break

    time.sleep(1)

    

toVisit = end
while toVisit != start:
    nextVertex = shortestDistanceMap[toVisit][0]

    #Draw
    nx.draw_networkx_edges(G, L, edgelist=[(toVisit, nextVertex)], width=8, edge_color='r', alpha=0.5)
    plt.pause(1e-17)

    #Go to predecessor
    toVisit = nextVertex

    #Wait
    time.sleep(0.5)    
    

print(shortestDistanceMap)

plt.show()


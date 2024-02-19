import networkx as nx

# i Create a graph (G) using nx.graph

G = nx.Graph()

# Adding edges to the graph , the weight represent distance between nodes
#edges are added to the graph using G.add_edge()

G.add_edge(0, 1, weight=2)
G.add_edge(0, 7, weight=8)
G.add_edge(1, 2, weight=16)
G.add_edge(1, 7, weight=10)
G.add_edge(2, 3, weight=7)
G.add_edge(2, 8, weight=4)
G.add_edge(2, 5, weight=4)
G.add_edge(3, 4, weight=9)
G.add_edge(3, 5, weight=8)

# Minimum Spanning Tree - Prim's Algorithm
prim_alg = nx.minimum_spanning_tree(G) #function to find minimum spanning tree using Prim

# Minimum Spanning Tree - Kruskal's Algorithm
kruskal_alg = nx.minimum_spanning_tree(G, algorithm="kruskal") #the same function but with parameter

# Shortest Path from Node 0 using Dijkstra's , function computes the shortest path from node 0 to all other nodes using Dijkstra.
dijkstra_shortest_path = nx.single_source_dijkstra_path_length(G, source=0)

print("Minimum Spanning Tree using Prim's Algorithm:")
print(list(prim_alg.edges(data=True)))

print("\nMinimum Spanning Tree using Kruskal's Algorithm:")
print(list(kruskal_alg.edges(data=True)))

print("\nShortest Path from Node 0 using Dijkstra's Algorithm:")
print(dijkstra_shortest_path)

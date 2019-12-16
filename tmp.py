import networkx as nx
import random
from collections import defaultdict

def bfs(g, node):
    total = 0
    queue = [node]
    visited = defaultdict(int)
    while len(queue) > 0:
        v = queue.pop(0)
        print(v)
        predecessors = list(g.predecessors(v))
        parent = predecessors[0] if len(predecessors) == 1 else None
        if parent is not None:
            if parent not in visited:
                total += 1
            visited[parent] = 1
        for d in g.out_edges(v):
            p,q = d
            queue.append(q)
        if (100, 100) == v:
            break

    return total

N = 6
Gr = nx.Graph()
for i in range(N):
    Gr.add_node(i)

edges = [(0, 1), (0, 2), (1, 5), (2, 3), (2, 4), (5,6), (6,7), (4,8)]
for i,j in edges:
    Gr.add_edge(i,j)

# print(bfs(Gr, 0))
print(nx.shortest_path_length(Gr,7))
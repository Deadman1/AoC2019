from Utils import read_input_as_list
from Computer import Computer
from copy import deepcopy
import networkx as nx

lines = read_input_as_list("inputs/15.txt")
intcode = [int(ele) for ele in lines[0].split(",")]

c = Computer(intcode)
graph = nx.DiGraph()
grid = {}
is_found = False
directions = { (0,-1): 1, (0,1): 2, (-1,0): 3, (1,0): 4 }
def explore(curr_pos):
    global c, graph, grid, is_found
    if not is_found:
        c_copy = deepcopy(c)
        for d_k, d_v in directions.items():
            point = (curr_pos[0]+d_k[0], curr_pos[1]+d_k[1])
            c = deepcopy(c_copy)
            if point not in grid:
                c.run_program([d_v])
                grid[point] = c.outputs[-1]
                if c.outputs[-1] != 0:
                    graph.add_edge(point, curr_pos)
                    if c.outputs[-1] != 2:
                        explore(point)
                    else:
                        is_found = True

explore((100,100))
c_n = [c for c in grid if grid[c] == 2][0]

print("Part 1")
a = nx.algorithms.traversal.depth_first_search.dfs_preorder_nodes(graph, (c_n))
print(len(list(a)) -1)

print("Part 2")
dist_dict = nx.shortest_path_length(nx.to_undirected(graph), c_n)
print(dist_dict[max(dist_dict, key=lambda x: dist_dict[x])])
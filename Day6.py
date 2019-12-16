import networkx as nx
from Utils import read_input_as_list

lines = read_input_as_list("inputs/6.txt")
input = [line.split(")") for line in lines]
dg = nx.DiGraph()
for (n1, n2) in input:
    dg.add_edge(n1, n2)

print("Part 1")
print(sum([len(nx.ancestors(dg,n)) for n in dg.nodes]))

print("Part 2")
print(nx.shortest_path_length(dg.to_undirected(), 'SAN', 'YOU')-2)

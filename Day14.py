import networkx as nx
from Utils import read_input_as_list
from collections import defaultdict

def extract_element(element_tuple):
    element_tuple = element_tuple.strip()
    quantity = int(element_tuple.split(" ")[0])
    element = element_tuple.split(" ")[1]
    return (element, quantity)

def construct_graph():
    global g
    lines = read_input_as_list("inputs/14.txt")
    for line in lines:
        lh_elements = [extract_element(ele_tuple) for ele_tuple in line.split("=>")[0].split(",")]
        rh_element = [extract_element(ele_tuple) for ele_tuple in line.split("=>")[1].split(",")][0]

        if rh_element not in g.nodes:
            g.add_node(rh_element, name=rh_element)
        for lh_element in lh_elements:
            if lh_element not in g.nodes:
                g.add_node(lh_element, name=lh_element)
            g.add_edge(rh_element[0], lh_element[0], l_val=lh_element[1], r_val=rh_element[1])

def get_resources(node_name, node_quant):
    global g, res_dict, surplus
    answer = node_quant
    for d in g.out_edges(node_name):
        u,v = d
        r_quant = g.edges[d]['r_val']
        l_quant = g.edges[d]['l_val']
        factor = -(-node_quant // r_quant) # Ceil division
        answer = factor * r_quant
        res_quant = get_resources(v, l_quant*factor - surplus[v])
        surplus[v] = res_quant - (l_quant*factor - surplus[v])
        res_dict[v] = res_dict[v] + res_quant if v in res_dict else res_quant

    return answer

g = nx.DiGraph()
res_dict = {}
surplus = defaultdict(int)
construct_graph()

# Part 1
res_dict = {}    
surplus = defaultdict(int)
answer = get_resources('FUEL', 1)
print("Part 1")
print(res_dict['ORE'])

# Part 2
low = 0
high = 1000000000000 
while low < high:
    mid = (low + high) // 2
    res_dict = {}
    surplus = defaultdict(int)
    answer = get_resources('FUEL', mid)
    if res_dict['ORE'] > 1000000000000:
        high = mid - 1
    elif res_dict['ORE'] < 1000000000000:
        low = mid + 1
        
print("Part 2")
print(low-1)
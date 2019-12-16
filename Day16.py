from Utils import read_input_as_list
from Computer import Computer
import networkx as nx

lines = read_input_as_list("inputs/15.txt")
intcode = [int(ele) for ele in lines[0].split(",")]
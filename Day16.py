from Utils import read_input_as_list
from Computer import Computer
import networkx as nx

lines = read_input_as_list("inputs/16.txt")
input = [int(ele) for ele in list(str(lines[0]))]

# Part 1
print("Part 1")
b_p = [0, 1, 0, -1]
current_input = []
current_input.extend(input)
for i in range(100):    
    for j, inp in enumerate(current_input):
        sum = 0
        for k, inp_1 in enumerate(current_input):
            sum += inp_1 * b_p[int((k + 1) / (j + 1)) % len(b_p)]
        current_input[j] = abs(sum)%10

print("".join([str(i) for i in current_input[:8]]))

# Part 2
print("Part 2")
input = input * 10000
index = len(input) - int("".join([str(i) for i in input[:7]]))
curr_input = input[-index:]
curr_input.reverse()
for j in range(100):
    for i in range(index):
        curr_input[i] = (curr_input[i] + curr_input[i-1] if i > 0 else 0) % 10

ans = curr_input[-8:]
ans.reverse()
print("".join([str(i) for i in ans]))
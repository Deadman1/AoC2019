from Utils import read_input_as_list
from Computer import Computer

lines = read_input_as_list("inputs/5.txt")
input = [int(ele) for ele in lines[0].split(",")]

print("Part 1")
c = Computer(input, [1])
c.run_program()
print(c.outputs[-1])

print("Part 2")
c = Computer(input, [5])
c.run_program()
print(c.outputs[-1])
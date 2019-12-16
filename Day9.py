from Utils import read_input_as_list
from Computer import Computer

lines = read_input_as_list("inputs/9.txt")
intcode = [int(ele) for ele in lines[0].split(",")]

print("Part 1")
c1 = Computer(intcode, [1], print_output=True)
c1.run_program()

print("Part 2")
c2 = Computer(intcode, [2], print_output=True)
c2.run_program()
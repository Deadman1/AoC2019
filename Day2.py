from Utils import read_input_as_list
from Computer import Computer

lines = read_input_as_list("inputs/2.txt")
input = [int(ele) for ele in lines[0].split(",")]

c = Computer(input)
c.run_program()

print("Part 1")
print(c.temp_copy[0])

print("Part 2")
for i in range(99):
    for j in range(99):
        input[1] = i
        input[2] = j
        c = Computer(input)
        c.run_program()
        if c.temp_copy[0] == 19690720:
            print(100*i+j)
            break

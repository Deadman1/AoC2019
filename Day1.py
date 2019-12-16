from Utils import read_input_as_list

def calc_fuel(mass):
    total = 0
    while mass > 0:
        mass = int(mass/3) - 2
        total += mass if mass > 0 else 0
    return total

lines = read_input_as_list("inputs/1.txt")
input = [int(line) for line in lines]

print("Part 1")
print(sum(int(val/3) - 2 for val in input))

print("Part 2")
print(sum(calc_fuel(val) for val in input))
from Utils import read_input_as_list
from Computer import Computer
from itertools import permutations


lines = read_input_as_list("inputs/7.txt")
intcode = [int(ele) for ele in lines[0].split(",")]

def run_controller_software(intcode, signal):
    computers = []
    for i in range(5):
        c = Computer(intcode)
        computers.append(c)
    j = 0
    while any([not c.is_finished for c in computers]):
        j += 1
        for i in range(5):
            input_i = 0 if len(computers[i-1].outputs) == 0 else computers[i-1].outputs[-1]
            inputs = [signal[i], input_i] if j == 1 else [input_i]
            computers[i].run_program(inputs)
        
    return computers[-1].outputs[-1]

print("Part 1")
signals = list(permutations([0,1,2,3,4], 5))
final_signals = [run_controller_software(intcode, signal) for signal in signals]
max_final_signal = max(final_signals)
print(max_final_signal)

print("Part 2")
signals = list(permutations([5,6,7,8,9], 5))
final_signals = [run_controller_software(intcode, signal) for signal in signals]
max_final_signal = max(final_signals)
print(max_final_signal)
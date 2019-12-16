from Utils import read_input_as_list
import re
import math

def get_tuple(line):
    transform = re.match(r"<x=(-?\d+), y=(-?\d+), z=(-?\d+)>", line)
    return tuple([int(t) for t in transform.groups()])

def get_input():
    lines = read_input_as_list("inputs/12.txt")
    pos = {}
    points = [get_tuple(line) for line in lines]
    for p1 in points:
        pos[p1] = p1
    return pos

def get_key(p_v_list):
    result = tuple()
    for p_v_pair in p_v_list:
        result += p_v_pair
    return result

def calc_change(p, q):
    return 1 if p < q else -1 if p > q else 0

def calc_total_moon_energy(position, velocity):
    return sum([abs(i) for i in position]) * sum([abs(i) for i in velocity])

def run_iteration(pos, vel):
    for p1_k in pos:
        p1 = pos[p1_k]
        for p2_k in pos:
            if p1_k != p2_k:
                p2 = pos[p2_k]
                vel_p1 = vel[p1_k] if p1_k in vel else (0, 0, 0)
                vel[p1_k] = tuple([vel_i + calc_change(p1[i], p2[i]) for i, vel_i in enumerate(vel_p1)])
    for p1 in pos.keys():
        pos[p1] = tuple([pos_i + vel_i for pos_i, vel_i in zip(pos[p1], vel[p1])])

points = get_input()

print("Part 1")
pos_part1 = dict(points)
vel_part1 = {}
for i in range(1000):
    run_iteration(pos_part1, vel_part1)

energy = sum([calc_total_moon_energy(pos_part1[point], vel_part1[point]) for point in pos_part1])
print(energy)

print("Part 2")
pos_part2 = dict(points)
vel_part2 = {}
j = 0
dim_freq = [0, 0, 0]
all_keys = [set(), set(), set()]
while 0 in dim_freq:
    run_iteration(pos_part2, vel_part2)
    for i in range(3):
        point_dim_key = get_key([(pos_part2[p_k][i], vel_part2[p_k][i]) for p_k in pos_part2.keys()])
        if dim_freq[i] == 0:
            if point_dim_key in all_keys[i]:
                dim_freq[i] = j
                continue
            all_keys[i].add(point_dim_key)    
    j += 1

lcm = dim_freq[0]
for i in dim_freq[1:]:
  lcm = lcm * i // math.gcd(lcm, i)
print(lcm)
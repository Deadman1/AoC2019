from math import atan2, degrees
from collections import defaultdict
from Utils import read_input_as_list

lines = read_input_as_list("inputs/10.txt")
points = [(j,i) for i, l in enumerate(lines) for j, p in enumerate(l) if p == "#"]

def find_best_location(points):
    max_vis = 0
    roi = None
    for p1 in points:
        ray_degrees = defaultdict(list)
        for p2 in points:
            if p1 == p2:
                continue
            deg = (degrees(atan2(p2[1] - p1[1], p2[0] - p1[0])) + 360) % 360
            ray_degrees[deg].append(p2)
        if len(ray_degrees.keys()) > max_vis:
            max_vis = len(ray_degrees.keys())
            roi = ray_degrees
    return (max_vis, roi)

print("Part 1")
max_vis, rays_of_interest = find_best_location(points)
print(max_vis)

print("Part 2")
start_degree = 90
ordered_angles = sorted(rays_of_interest.keys(), key = lambda x: (x+start_degree) % 360)
vap_index = 0
while vap_index < len(points) and vap_index != 200:
    for angle in ordered_angles:
        p = rays_of_interest[angle].pop(0)
        vap_index += 1
        if vap_index == 200:
            print(p[0]*100+p[1])
            break

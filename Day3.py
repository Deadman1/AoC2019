from Utils import read_input_as_list

def get_key(point):
    return str(point[0])+"_"+str(point[1])

def get_range(a, b):
    return (a,b) if a < b else (b, a)

def update_list(x1, y1, instruction, existing_dist):
    x2 = x1
    y2 = y1
    direction = instruction[0]
    distance = int(instruction[1:])
    if direction == 'R':
        x2 = x1 + distance
    elif direction == 'L':
        x2 = x1 - distance
    elif direction == 'U':
        y2 = y1 + distance
    elif direction == 'D':
        y2 = y1 - distance

    rx1, rx2 = get_range(x1, x2)
    ry1, ry2 = get_range(y1, y2)
    new_distance = existing_dist + distance
    points = set([(x,y) for y in range(ry1, ry2+1) for x in range(rx1, rx2+1)])

    return x2, y2, new_distance, points

def get_points(wire):
    prev_x = prev_y = prev_dist = 0
    all_points = set()
    wire_steps = {}
    for instruction in wire:
        x, y, current_dist, points = update_list(prev_x, prev_y, instruction, prev_dist)
        all_points |= points
        for p in points:
            key = get_key(p)
            if key not in wire_steps.keys():
                wire_steps[key] = prev_dist + abs(p[0] - prev_x) + abs(p[1] - prev_y)
        prev_dist = current_dist
        prev_x = x
        prev_y = y

    return all_points, wire_steps

lines = read_input_as_list("inputs/3.txt")
w1, w2 = [line.split(",") for line in lines]
w1_points, w1_steps = get_points(w1)
w2_points, w2_steps = get_points(w2)

intersection = w1_points & w2_points
intersection.remove((0,0))

print("Part 1")
print(min(intersection, key=lambda x: abs(x[0]) + abs(x[1])))

print("Part 2")
point_of_interest = min(intersection, key=lambda x: w1_steps[get_key(x)] + w2_steps[get_key(x)])
key = get_key(point_of_interest)
print(w1_steps[key] + w2_steps[key])
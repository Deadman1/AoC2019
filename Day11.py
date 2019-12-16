from Utils import read_input_as_list
from Computer import Computer
from collections import defaultdict
from enum import Enum

class Direction(Enum):
    UP = 1
    DOWN = 2
    RIGHT = 3
    LEFT = 4

lines = read_input_as_list("inputs/11.txt")
intcode = [int(ele) for ele in lines[0].split(",")]

def run_robot(grid):
    point = (0,0)
    prev_dir = Direction.UP
    c1 = Computer(intcode)
    while not c1.is_finished:
        input = grid[point] if point in grid else 0
        c1.run_program([input])
        grid[point] = c1.outputs[-2]
        dir_factor = 1 if c1.outputs[-1] == 0 else -1
        if prev_dir == Direction.UP:
            point = (point[0] - 1 * dir_factor, point[1])
            prev_dir = Direction.LEFT if dir_factor == 1 else Direction.RIGHT
        elif prev_dir == Direction.DOWN:
            point = (point[0] + 1 * dir_factor, point[1])
            prev_dir = Direction.RIGHT if dir_factor == 1 else Direction.LEFT
        elif prev_dir == Direction.LEFT:
            point = (point[0], point[1] + 1 * dir_factor)
            prev_dir = Direction.DOWN if dir_factor == 1 else Direction.UP
        elif prev_dir == Direction.RIGHT:
            point = (point[0], point[1] - 1 * dir_factor)
            prev_dir = Direction.UP if dir_factor == 1 else Direction.DOWN

print("Part 1")
grid = {}
run_robot(grid)
print(len(grid.keys()))

print("Part 2")
grid = {(0,0):1}
run_robot(grid)
two_d_grid = [[0 for j in range(50)] for i in range(10)]
for k in grid.keys():
    x,y = k
    two_d_grid[y][x] = grid[k]

for i in range(len(two_d_grid)):
    for j in range(len(two_d_grid[0])):
        val = "1" if two_d_grid[i-1][j-1] == 1 else " "
        print(val, end=" ")
    print()
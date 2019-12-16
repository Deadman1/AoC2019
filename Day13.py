from Utils import read_input_as_list
from Computer import Computer
import matplotlib.pyplot as plt

lines = read_input_as_list("inputs/13.txt")
intcode = [int(ele) for ele in lines[0].split(",")]

c = Computer(intcode)
c.run_program()
total = 0
for i in range(2,len(c.outputs), 3):
    total+= 1 if c.outputs[i] == 2 else 0   

# Part 1
# print(total)

# points = {}
# ball = None
# paddle = None
# for i in range(0,len(c.outputs), 3):
#     x, y, tile_id = c.outputs[i:i+3]
#     points[(x, y)] = tile_id
#     if c.outputs[i+2] == 4:
#         ball = (x, y)
#     if c.outputs[i+2] == 3:
#         paddle = (x, y)

# # print(len(points.keys()))
# # print(ball)
# print(paddle)

def update_grid(outputs, grid):
    for i in range(0,len(outputs), 3):
        x, y, tile_id = outputs[i:i+3]
        if tile_id <= 4:
            grid[(x, y)] = tile_id


def print_grid(grid,score, not_final=True):
    x = [max(grid.keys(), key=lambda k:k[0])[0] - k[0] for k in grid.keys() if grid[k] != 0]
    y = [max(grid.keys(), key=lambda k:k[1])[1] - k[1] for k in grid.keys() if grid[k] != 0]
    c = [grid[k] for k in grid.keys() if grid[k] != 0]
    scat = plt.scatter(x, y, c=c)
    ann = plt.annotate("Score = {0}".format(score), xy=(10, 10), xycoords='figure pixels')
    plt.pause(0.05)
    if not_final:
        scat.remove()
        ann.remove()

# part 2
intcode[0] = 2
c = Computer(intcode)
ball_pos = 0
paddle_pos = 0
op_index = 0
grid = {}
score = 0
while not c.is_finished:
    input = 0 if ball_pos == paddle_pos else 1 if ball_pos > paddle_pos else -1
    c.run_program([input])
    run_op = c.outputs[op_index:len(c.outputs)] 
    op_index = len(c.outputs)
    for p in range(0, len(run_op), 3):
        x,y,tile_id = run_op[p:p+3]
        if x == -1 and y == 0 and tile_id > 4:
            score = tile_id
        elif tile_id == 4:
            ball_pos = x
        elif tile_id == 3:
            paddle_pos = x
    update_grid(run_op, grid)
    print_grid(grid, score=score)

print_grid(grid, tile_id, False)
plt.show()
from Utils import read_input_as_list
from Computer import Computer
import matplotlib.pyplot as plt

lines = read_input_as_list("inputs/13.txt")
intcode = [int(ele) for ele in lines[0].split(",")]

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

# part 1
print("Part 1")
c = Computer(intcode)
c.run_program()
total = 0
for i in range(2,len(c.outputs), 3):
    total+= 1 if c.outputs[i] == 2 else 0  
print(total)

# part 2
print("Part 2")
show_visualization = False # Set this flag to true to display visuals.
intcode[0] = 2
c = Computer(intcode)
ball_pos = paddle_pos = score = 0
grid = {}
while not c.is_finished:
    input = 0 if ball_pos == paddle_pos else 1 if ball_pos > paddle_pos else -1
    c.run_program([input])
    for p in range(0, len(c.outputs), 3):
        x,y,tile_id = c.outputs[p:p+3]
        if x == -1 and y == 0 and tile_id > 4:
            score = tile_id
        elif tile_id == 4:
            ball_pos = x
        elif tile_id == 3:
            paddle_pos = x
    
    if show_visualization:
        update_grid(c.outputs, grid)
        print_grid(grid, score=score)
    
    # Wipe c.outputs before the next run since output is stored across iterations.
    c.outputs = []

print("Score = ", score)
if show_visualization:
    print_grid(grid, tile_id, False)
    plt.show()
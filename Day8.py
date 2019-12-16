from Utils import read_input_as_list
import sys

lines = read_input_as_list("inputs/8.txt")
input = [int(i) for i in list(str(lines[0]))]
width = 25
height = 6

k = i = z_c = o_c = t_c = ans = 0
min_z_c = sys.maxsize
image = [2] * (width * height)
for j, num in enumerate(input):
    z_c += 1 if num == 0 else 0
    o_c += 1 if num == 1 else 0
    t_c += 1 if num == 2 else 0

    if j % (width * height) == 0 and j != 0:
        if min_z_c > z_c:
            ans = o_c * t_c
            min_z_c = z_c
        z_c = 1 if num == 0 else 0
        o_c = 1 if num == 1 else 0
        t_c = 1 if num == 2 else 0
        k = 0
    image[k] = num if image[k] == 2 else image[k]
    k += 1

if min_z_c > z_c:
    ans = o_c * t_c

print("Part 1")
print(ans)

print("Part 2")
for i in range(6):
    for l in image[i * 25: (i+1)*25]:
        print('1' if l == 1 else " ", end=" ")
    print()

import numpy as np
import time

with open("input06.txt") as f:
    input_real = f.read()

def solve(input_text, question):
    grid = np.zeros((1000, 1000))

    for instruction in input_text.split("\n"):
        parts = instruction.split()
        if not parts:
            continue

        x1,y1 = [int(x) for x in parts[-3].split(",")]
        x2,y2 = [int(x) + 1 for x in parts[-1].split(",")]

        if parts[0] == "toggle":
            if question == 1:
                grid[x1:x2, y1:y2] = np.mod(grid[x1:x2, y1:y2] + 1, 2)
            else:
                grid[x1:x2, y1:y2] += 2
        elif parts[1] == "on":
            if question == 1:
                grid[x1:x2, y1:y2] = 1
            else:
                grid[x1:x2, y1:y2] += 1
        elif parts[1] == "off":
            if question == 1:
                grid[x1:x2, y1:y2] = 0
            else:
                grid[x1:x2, y1:y2] = np.maximum(grid[x1:x2, y1:y2] - 1, 0)

    print(int(grid.sum()))

start_time = time.time()
solve(input_real, 1)
solve(input_real, 2)
elapsed_time = time.time() - start_time
print(f"Execution time: {elapsed_time} seconds")

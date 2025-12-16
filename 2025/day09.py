import heapq
import time
import numpy as np
from scipy.sparse import csr_array

with open("input09.txt") as f:
    input_real = f.read()

input_test = """7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3
7,1"""

def solve(input_text):
    points = input_text.split()
    max_x = 0
    max_y = 0

    for i in range(len(points)):
        parts = points[i].split(",")
        points[i] = (int(parts[0]), int(parts[1]))
        max_x = max(max_x, points[i][0])
        max_y = max(max_y, points[i][1])

    max_area = 0
    heap = []
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            x1, y1 = points[i]
            x2, y2 = points[j]
            area = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
            max_area = max(max_area, area)
            heapq.heappush(heap, (-area, i, j))

    print(max_area)

    grid = np.zeros((max_x+1,max_y+1), dtype=bool)
    last_x = None
    last_y = None
    for i in range(len(points)):
        x,y = points[i]
        if last_x is not None:
            if last_x == x:
                grid[x,min(y,last_y)+1:max(y,last_y)] = True
            elif last_y == y:
                grid[min(x,last_x)+1:max(x,last_x),y] = True
            else:
                raise ValueError()
        last_x = x
        last_y = y

    grid = csr_array(grid)
    
    while heap:
        area, i, j = heapq.heappop(heap)
        x1, y1 = [min(points[i][k], points[j][k]) for k in range(2)]
        x2, y2 = [max(points[i][k], points[j][k]) for k in range(2)]
        if grid[x1+1:x2, y1+1:y2].nnz == 0:
            print(-area)
            return

print("Test")
solve(input_test)
print("Real")
start_time = time.time()
solve(input_real)
elapsed_time = time.time() - start_time
print(f"Execution time: {elapsed_time} seconds")

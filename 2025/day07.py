import time
from collections import deque

input_test = """.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
..............."""

with open("input07.txt") as f:
    input_real = f.read()        

def solve(input_text, question):
    grid = input_text.split()
    height = len(grid)
    width = len(grid[0])
    start = None

    for i in range(height):
        grid[i] = list(grid[i])
        if not start:
            for j in range(width):
                if grid[i][j] == "S":
                    start = (i,j)
                    break

    if question == 1:
        to_visit = deque([(start[0]+1, start[1])])
        splitters_visited = set()
        while to_visit:
            i,j = to_visit.popleft()
            if i+1 >= height:
                continue
            elif grid[i+1][j] == ".":
                to_visit.append((i+1,j))
                grid[i+1][j] = "|"
            elif grid[i+1][j] == "^":
                splitters_visited.add((i+1,j))
                if j > 0 and grid[i+1][j-1] == ".":
                    to_visit.append((i+1,j-1))
                if j + 2 < width and grid[i+1][j+1] == ".":
                    to_visit.append((i+1,j+1))
        
        print(len(splitters_visited))
    
    else:
        counts = [1] * width
        for i in range(height-1, 1, -1):
            for j in range(width):
                if grid[i][j] == "^":
                    counts[j] = counts[j-1] + counts[j+1]

        print(counts[start[1]])

print("Test")
solve(input_test, 1)
solve(input_test, 2)
print("Real")
start_time = time.time()
solve(input_real, 1)
solve(input_real, 2)
elapsed_time = time.time() - start_time
print(f"Execution time: {elapsed_time} seconds")

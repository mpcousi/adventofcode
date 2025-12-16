
import time

with open("input04.txt") as f:
    input_real = f.read()

input_test = "..@@.@@@@. @@@.@.@.@@ @@@@@.@.@@ @.@@@@..@. @@.@@@@.@@ .@@@@@@@.@ .@.@.@.@@@ @.@@@.@@@@ .@@@@@@@@. @.@.@@@.@."


def solve(input_text):
    grid = input_text.split()
    n = len(grid)
    m = len(grid[0])
    
    total = 0
    
    grid2 = input_text.split()
    for y in range(n):
        grid2[y] = [x for x in grid2[y]]


    first_iteration = True
    while True:
        num_rolls = 0
        for y in range(n):
            for x in range(m):
                if grid[y][x] != "@":
                    continue

                num_adjacents = 0
                for i,j in ((-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)):
                    x2 = x + i
                    y2 = y + j
                    if x2 >= 0 and x2 < m and y2 >= 0 and y2 < n and grid[y2][x2] == "@":
                        num_adjacents += 1
                
                if num_adjacents < 4:
                    grid2[y][x] = "."
                    num_rolls += 1

        total += num_rolls
        if first_iteration:
            print(total)
            first_iteration = False
        if num_rolls == 0:
            print(total)
            return

        grid = grid2

print("Test")
solve(input_test)
print("Real")
start_time = time.time()
solve(input_real)
elapsed_time = time.time() - start_time
print(f"Execution time: {elapsed_time} seconds")

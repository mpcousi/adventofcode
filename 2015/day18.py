import time

with open("input18.txt") as f:
    input_real = f.read()

input_test = """.#.#.#
...##.
#....#
..#...
#.#..#
####.."""

def solve(input_text, num_steps, question):
    grid = input_text.strip().split()
    n = len(grid)
    m = len(grid[0])
    for i in range(n):
        grid[i] = list(grid[i])
    
    if question == 2:
        corners = {(0,0), (0,m-1), (n-1,0), (n-1,m-1)}
        for x,y in corners:
            grid[x][y] = "#"

    for _ in range(num_steps):
        to_toggle = []
        for x in range(n):
            for y in range(m):
                num_neighbors = 0
                for i,j in ((-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)):
                    x2 = x + i
                    y2 = y + j
                    if x2 >= 0 and x2 < n and y2 >= 0 and y2 < m and grid[x2][y2] == "#":
                        num_neighbors += 1
                if grid[x][y] == "#" and (num_neighbors < 2 or num_neighbors > 3):
                    to_toggle.append((x,y,"."))
                elif grid[x][y] == "." and num_neighbors == 3:
                    to_toggle.append((x,y,"#"))
        
        for x,y,value in to_toggle:
            if question == 1 or (x,y) not in corners:
                grid[x][y] = value
    
    total = 0
    for x in range(n):
        for y in range(m):
            if grid[x][y] == "#":
                total += 1
    
    print(total)

print("Test")
solve(input_test, 4, 1)
solve(input_test, 5, 2)
print("Real")
start_time = time.time()
solve(input_real, 100, 1)
solve(input_real, 100, 2)
elapsed_time = time.time() - start_time
print(f"Execution time: {elapsed_time} seconds")

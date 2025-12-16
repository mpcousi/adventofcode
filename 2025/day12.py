import time

with open("input12.txt") as f:
    input_real = f.read()

input_test = """0:
###
##.
##.

1:
###
##.
.##

2:
.##
###
##.

3:
##.
###
##.

4:
###
#..
###

5:
###
.#.
###

4x4: 0 0 0 0 2 0
12x5: 1 0 1 0 2 2
12x5: 1 0 1 0 3 2"""

def solve(input_text):
    presents = {}
    regions = []
    present_so_far = []
    next_id = None
    for line in input_text.split("\n"):
        if "x" in line:
            parts = line.split(":")
            areas = [int(x) for x in parts[0].split("x")]
            area = 1
            for x in areas:
                area *= x
            regions.append({
                "name": parts[0],
                "area": area,
                "presents": [int(x) for x in parts[1].split()]
            })
        elif ":" in line:
            next_id = int(line.split(":")[0])
            present_so_far = []
        elif not line:
            area = 0
            for x in range(len(present_so_far)):
                for y in range(len(present_so_far[0])):
                    if present_so_far[x][y] == "#":
                        area += 1
            presents[next_id] = {
                "area": area,
                "grid": present_so_far
            }
        else:
            present_so_far.append(list(line))

    count = 0
    for region in regions:
        area = 0
        for present, n in enumerate(region["presents"]):
            area += presents[present]["area"] * n
        if region["area"] >= area:
            count += 1
        
    print(count)

print("Test")
solve(input_test)

print("Real")
start_time = time.time()
solve(input_real)
elapsed_time = time.time() - start_time
print(f"Execution time: {elapsed_time} seconds")

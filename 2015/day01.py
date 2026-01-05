import time

with open("input01.txt") as f:
    input_real = f.read()

def solve(input_text):
    part2 = None
    floor = 0

    for i, c in enumerate(input_text):
        if c == "(":
            floor += 1
        elif c == ")":
            floor -=1

        if floor < 0 and part2 is None:
            part2 = i + 1

    print(floor)
    print(part2)

start_time = time.time()
solve(input_real)
elapsed_time = time.time() - start_time
print(f"Execution time: {elapsed_time} seconds")
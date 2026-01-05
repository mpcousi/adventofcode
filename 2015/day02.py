import time

with open("input02.txt") as f:
    input_real = f.read()

def solve(input_text):
    part1 = 0
    part2 = 0

    for present in input_text.split():
        parts = [int(x) for x in present.split("x")]
        sorted_parts = sorted(parts)
        sides = [parts[0] * parts[1], parts[1] * parts[2], parts[0] * parts[2]]
        part1 += sum([2*x for x in sides]) + min(sides)
        part2 += 2 * sorted_parts[0] + 2 * sorted_parts[1] + parts[0] * parts[1] * parts[2]

    print(part1)
    print(part2)

start_time = time.time()
solve(input_real)
elapsed_time = time.time() - start_time
print(f"Execution time: {elapsed_time} seconds")

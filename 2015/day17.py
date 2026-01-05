import time
from collections import deque

with open("input17.txt") as f:
    input_real = f.read()

input_test = "20 15 10 5 5"

def solve(input_text, volume):
    bottles = [int(x) for x in input_text.strip().split()]
    n = len(bottles)
    queue = deque([(volume, set())])
    result = set()
    already_processed = set()

    while queue:
        liters, so_far = queue.pop()
        current = (liters, tuple(so_far))
        if current in already_processed:
            continue
        already_processed.add(current)

        for i in range(n):
            if i not in so_far:
                if liters == bottles[i]:
                    result.add(tuple(sorted(so_far | set([i]))))
                elif liters > bottles[i]:
                    queue.append((liters - bottles[i], so_far | set([i])))

    print(len(result))

    smallest_combination = None
    num_combinations = 0
    for combination in result:
        if smallest_combination is None or len(combination) < smallest_combination:
            smallest_combination = len(combination)
            num_combinations = 1
        elif len(combination) == smallest_combination:
            num_combinations += 1
    print(num_combinations)

print("Test")
solve(input_test, 25)
print("Real")
start_time = time.time()
solve(input_real, 150)
elapsed_time = time.time() - start_time
print(f"Execution time: {elapsed_time} seconds")

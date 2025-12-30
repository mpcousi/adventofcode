import numpy as np
import scipy
import time
from collections import deque

with open("input10.txt") as f:
    input_real = f.read()

input_test = """[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}"""

def apply_button(state, button):
    new_state = state.copy()
    for n in button:
        new_state[n] = not new_state[n]
    return new_state

def solve1(buttons, lights):
    final = 0
    for i, x in enumerate(lights):
        if x == "#":
            final |= 2 ** i

    operations = []
    for button in buttons:
        operation = 0
        for i in button:
            operation |= 2 ** i
        operations.append(operation)

    distances = [0] + [2 ** 32] * (2 ** len(lights) - 1)
    queue = deque([0])
    while queue:
        state = queue.popleft()
        if state == final:
            return distances[state]

        for operation in operations:
            state2 = state ^ operation
            distance2 = distances[state] + 1
            if distance2 < distances[state2]:
                distances[state2] = distance2
                queue.append(state2)

def solve2(buttons, joltages):
    num_buttons = len(buttons)
    num_counters = len(joltages)
    A = np.zeros((num_counters, num_buttons))
    b = np.array(joltages)
    c = np.array([1] * num_buttons)

    for j in range(num_counters):
        for k in range(num_buttons):
            if j in buttons[k]:
                A[j,k] = 1

    return int(sum(scipy.optimize.linprog(c, A_eq=A, b_eq=b, integrality=1).x))


def solve(input_text):
    lines = input_text.split("\n")
    part1 = 0
    part2 = 0

    for i in range(len(lines)):
        parts = lines[i].split()
        lights = parts[0][1:-1]
        buttons = [[int(x) for x in y[1:-1].split(",")] for y in parts[1:-1]]
        joltages = [int(x) for x in parts[-1][1:-1].split(",")]

        part1 += solve1(buttons, lights)
        part2 += solve2(buttons, joltages)

    print(part1)
    print(part2)

print("Test")
solve(input_test)
print("Real")
start_time = time.time()
solve(input_real)
elapsed_time = time.time() - start_time
print(f"Execution time: {elapsed_time} seconds")

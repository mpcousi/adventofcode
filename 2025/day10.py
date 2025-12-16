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

def solve1(input_text):
    total = 0
    lines = input_text.split("\n")

    for i in range(len(lines)):
        parts = lines[i].split()
        final = np.array([False if x == "." else True for x in parts[0][1:-1]])
        buttons = [[int(x) for x in y[1:-1].split(",")] for y in parts[1:-1]]
        state = np.array([False] * len(final))
        
        answer = None
        queue = deque([])
        for button in buttons:
            new_state = apply_button(state, button)
            if not np.bitwise_xor(new_state, final).any():
                answer = 1
                break
            queue.append((1, new_state))
        
        while answer is None and queue:
            count, state = queue.popleft()

            for button in buttons:
                new_state = apply_button(state, button)
                if not np.bitwise_xor(new_state, final).any():
                    answer = count + 1
                    break
                queue.append((count + 1, new_state))

        total += answer
        
    print(total)

def solve2(input_text):
    total = 0
    lines = input_text.split("\n")
    for i in range(len(lines)):
        parts = lines[i].split()
        joltages = [int(x) for x in parts[-1][1:-1].split(",")]
        num_counters = len(joltages)
        num_buttons = len(parts[1:-1])
        buttons = [[int(x) for x in y[1:-1].split(",")] for y in parts[1:-1]]
        A = np.zeros((num_counters, num_buttons))
        b = np.array(joltages)
        c = np.array([1] * num_buttons)

        for j in range(num_counters):
            for k in range(num_buttons):
                if j in buttons[k]:
                    A[j,k] = 1

        total += sum(scipy.optimize.linprog(c, A_eq=A, b_eq=b, integrality=1).x)

    print(int(total))

print("Test")
solve1(input_test)
solve2(input_test)
print("Real")
start_time = time.time()
solve1(input_real)
solve2(input_real)
elapsed_time = time.time() - start_time
print(f"Execution time: {elapsed_time} seconds")

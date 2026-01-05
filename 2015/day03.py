import time

with open("input03.txt") as f:
    input_real = f.read()

def solve(input_text, question):
    pos = [[0,0], [0,0]]
    presents = set()

    for i, c in enumerate(input_text):
        santa = 1 if question == 2 and i % 2 == 1 else 0

        if c == "<":
            pos[santa][0] -= 1
        elif c == ">":
            pos[santa][0] += 1
        elif c == "v":
            pos[santa][1] -= 1
        elif c == "^":
            pos[santa][1] += 1

        presents.add(tuple(pos[santa]))

    print(len(presents))

start_time = time.time()
solve(input_real, 1)
solve(input_real, 2)
elapsed_time = time.time() - start_time
print(f"Execution time: {elapsed_time} seconds")

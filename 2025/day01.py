import time

with open("input01.txt") as f:
    input_real = f.read().split()

input_test = "L68 L30 R48 L5 R60 L55 L1 L99 R14 L82".split()

def solve(question, inputs):
    state = 50
    counter = 0

    for input_ in inputs:
        op = input_[0]
        num = int(input_[1:])

        if num == 0:
            continue

        for _ in range(num):
            state += 1 if op == "R" else -1        
            if state in (0, 100):
                state = 0
                if question == 2:
                    counter += 1
            elif state == -1:
                state = 99

        if question == 1 and state == 0:
            counter += 1

    print(counter)


print("Test")
solve(1, input_test)
solve(2, input_test)
print("Real")
start_time = time.time()
solve(1, input_real)
solve(2, input_real)
elapsed_time = time.time() - start_time
print(f"Execution time: {elapsed_time} seconds")

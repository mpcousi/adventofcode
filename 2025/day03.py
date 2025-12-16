import time

with open("input03.txt") as f:
    input_real = f.read()

input_test = "987654321111111 811111111111119 234234234234278 818181911112111"

def solve(input_text, question):
    total = 0

    for line in input_text.split():
        num_batteries = 2 if question == 1 else 12
        left = 0
        selected = 0

        while num_batteries > 0:
            max_num = -1
            max_right = None
            for right in range(left, len(line) - num_batteries + 1):
                num = int(line[right])
                if num > max_num:
                    max_num = num
                    max_right = right

            selected = 10 * selected + max_num
            left = max_right + 1
            num_batteries -= 1

        total += selected

    return total

print("Real")
print(solve(input_test, 1))
print(solve(input_test, 2))
print("Test")
start_time = time.time()
print(solve(input_real, 1))
print(solve(input_real, 2))
elapsed_time = time.time() - start_time
print(f"Execution time: {elapsed_time} seconds")

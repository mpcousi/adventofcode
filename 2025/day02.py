import time

with open("input02.txt") as f:
    input_real = f.read()

input_test = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"


def solve(input_text):
    part1 = 0
    part2 = 0

    for r in input_text.split(","):
        left, right = [int(x) for x in r.split("-")]
        for num in range(left, right+1):
            num_str = str(num)
            n = len(num_str)

            if n % 2 == 0 and num_str[:n//2] == num_str[n//2:]:
                part1 += num
            for i in range(1, n//2 + 1):
                if n % i != 0:
                    continue
                for j in range(i, n-i+1, i):
                    if num_str[j:j+i] != num_str[:i]:
                        break
                else:
                    part2 += num
                    break

    print(part1)
    print(part2)

print("Test")
solve(input_test)
print("Real")
start_time = time.time()
solve(input_real)
elapsed_time = time.time() - start_time
print(f"Execution time: {elapsed_time} seconds")

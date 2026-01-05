import time

with open("input10.txt") as f:
    input_real = f.read()

def solve(input_text, times):
    n = input_text.strip()
    for _ in range(times):
        n2 = ""
        last_c = n[0]
        start = 0
        i = 1
        while i < len(n):
            if n[i] != last_c:
                n2 += str(i - start) + last_c
                last_c = n[i]
                start = i
            i += 1
        n2 += str(i - start) + last_c
        n = n2
    print(len(n))

print("Test")
solve("1", 5)
print("Real")
start_time = time.time()
solve(input_real, 40)
solve(input_real, 50)
elapsed_time = time.time() - start_time
print(f"Execution time: {elapsed_time} seconds")

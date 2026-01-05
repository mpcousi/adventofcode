import hashlib
import time

with open("input04.txt") as f:
    input_real = f.read()

def solve(input_text, prefix):
    i = 0
    last_hash = ""

    while not last_hash.startswith(prefix):
        i += 1
        last_hash = hashlib.md5((input_text + str(i)).encode()).hexdigest()

    print(i)

start_time = time.time()
solve(input_real, "00000")
solve(input_real, "000000")
elapsed_time = time.time() - start_time
print(f"Execution time: {elapsed_time} seconds")

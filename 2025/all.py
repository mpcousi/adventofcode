import subprocess
import sys
import time

global_start_time = time.time()

for i in range(1, 13):
    start_time = time.time()
    subprocess.run([sys.executable, f"day{str(i).zfill(2)}.py"], capture_output=True)
    elapsed_time = time.time() - start_time
    print(f"Day {i}: {str(elapsed_time)[:10]} seconds")

elapsed_time = time.time() - global_start_time
print(f"All runs: {elapsed_time} seconds")

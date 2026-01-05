import time
from itertools import permutations

with open("input09.txt") as f:
    input_real = f.read()

input_test = """London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141"""

def solve(input_text):
    distances = {}
    for line in input_text.split("\n"):
        if not line:
            continue
        parts = line.split()
        city1 = parts[0]
        city2 = parts[2]
        dist = int(parts[-1])
        if city1 not in distances:
            distances[city1] = {}
        distances[city1][city2] = dist
        if city2 not in distances:
            distances[city2] = {}
        distances[city2][city1] = dist
    
    cities = distances.keys()
    smallest_distance = None
    longest_distance = None
    for p in permutations(cities):
        dist = 0
        for i in range(len(cities) - 1):
            dist += distances[p[i]][p[i+1]]
        if smallest_distance is None or dist < smallest_distance:
            smallest_distance = dist
        if longest_distance is None or dist > longest_distance:
            longest_distance = dist

    print(smallest_distance)
    print(longest_distance)

print("Test")
solve(input_test)
print("Real")
start_time = time.time()
solve(input_real)
elapsed_time = time.time() - start_time
print(f"Execution time: {elapsed_time} seconds")

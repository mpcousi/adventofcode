import time
from itertools import permutations

with open("input13.txt") as f:
    input_real = f.read()

input_test = """Alice would gain 54 happiness units by sitting next to Bob.
Alice would lose 79 happiness units by sitting next to Carol.
Alice would lose 2 happiness units by sitting next to David.
Bob would gain 83 happiness units by sitting next to Alice.
Bob would lose 7 happiness units by sitting next to Carol.
Bob would lose 63 happiness units by sitting next to David.
Carol would lose 62 happiness units by sitting next to Alice.
Carol would gain 60 happiness units by sitting next to Bob.
Carol would gain 55 happiness units by sitting next to David.
David would gain 46 happiness units by sitting next to Alice.
David would lose 7 happiness units by sitting next to Bob.
David would gain 41 happiness units by sitting next to Carol."""

def solve(input_text, question):
    lines = input_text.strip().split("\n")
    happiness = {}
    for line in lines:
        parts = line.split()
        person1 = parts[0]
        person2 = parts[-1][:-1]
        value = int(parts[3]) * (-1 if parts[2] == "lose" else 1)
        if person1 not in happiness:
            happiness[person1] = {}
        happiness[person1][person2] = value

    people = list(happiness.keys())
    if question == 2:
        happiness["You"] = {}
        for p in people:
            happiness[p]["You"] = 0
            happiness["You"][p] = 0
        people.append("You")

    n = len(people)
    max_happiness = None
    for p in permutations(people):
        total = 0
        for i in range(n):
            total += happiness[p[i]][p[(i - 1) % n]] + happiness[p[i]][p[(i + 1) % n]]
        if max_happiness is None or total > max_happiness:
            max_happiness = total
    
    print(max_happiness)

print("Test")
solve(input_test, 1)
print("Real")
start_time = time.time()
solve(input_real, 1)
solve(input_real, 2)
elapsed_time = time.time() - start_time
print(f"Execution time: {elapsed_time} seconds")

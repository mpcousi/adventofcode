import time

with open("input16.txt") as f:
    input_real = f.read()

target = """children: 3
cats: 7
samoyeds: 2
pomeranians: 3
akitas: 0
vizslas: 0
goldfish: 5
trees: 3
cars: 2
perfumes: 1"""

def solve(input_text, target_str):
    target = {}
    for line in target_str.strip().split("\n"):
        parts = line.split(":")
        target[parts[0]] = int(parts[1].strip())
    
    part1 = None
    part2 = None
    for line in input_text.strip().split("\n"):
        i = line.index(":")
        aunt_id = int(line[:i].split()[-1])
        matches1 = True
        matches2 = True

        for part in line[i+1:].split(","):
            parts = part.split(":")
            prop = parts[0].strip()
            value = int(parts[1].strip())

            if prop in {"cats", "trees"}:
                if value != target[prop]:
                    matches1 = False
                if value <= target[prop]:
                    matches2 = False
            elif prop in {"pomeranians", "goldfish"}:
                if value != target[prop]:
                    matches1 = False
                if value >= target[prop]:
                    matches2 = False
            elif target[prop] != value:
                matches1 = False
                matches2 = False
                break

        if matches1:
            part1 = aunt_id
        elif matches2:
            part2 = aunt_id

    print(part1)
    print(part2)

start_time = time.time()
solve(input_real, target)
elapsed_time = time.time() - start_time
print(f"Execution time: {elapsed_time} seconds")

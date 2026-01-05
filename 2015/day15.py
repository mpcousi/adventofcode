import time

with open("input15.txt") as f:
    input_real = f.read()

input_test = """Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3"""

def all_combinations(num_ingredients, num_teaspoons):
    if num_ingredients == 1:
        yield [num_teaspoons]
    else:
        for i in range(num_teaspoons + 1):
            teaspoons_left = num_teaspoons - i
            for combinations in all_combinations(num_ingredients - 1, teaspoons_left):
                yield [i] + combinations

def solve(input_text):
    ingredients = []
    for line in input_text.strip().split("\n"):
        parts = line.split()
        ingredients.append({
            "capacity": int(parts[2][:-1]),
            "durability": int(parts[4][:-1]),
            "flavor": int(parts[6][:-1]),
            "texture": int(parts[8][:-1]),
            "calories": int(parts[-1]),
        })

    n = len(ingredients)
    part1 = 0
    part2 = 0
    for combination in all_combinations(n, 100):
        score = 1
        num_calories = None
        for property in ingredients[0].keys():
            value = max(0, sum([ingredients[i][property] * combination[i] for i in range(n)]))
            if property == "calories":
                num_calories = value
            else:
                score *= value

        part1 = max(part1, score)
        if num_calories == 500:
            part2 = max(part2, score)
    print(part1)
    print(part2)

print("Test")  
solve(input_test)
print("Real")
start_time = time.time()
solve(input_real)
elapsed_time = time.time() - start_time
print(f"Execution time: {elapsed_time} seconds")

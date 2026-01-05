import json
import time

with open("input12.txt") as f:
    input_real = f.read()

def solve_recursive(data, question):
    if isinstance(data, list):
        return sum([solve_recursive(x, question) for x in data])
    elif isinstance(data, dict):
        if question == 2 and "red" in data.values():
            return 0
        else:
            return sum([solve_recursive(x, question) for x in data.values()])
    elif isinstance(data, int):
        return data
    else:
        return 0

def solve(input_text, question):
    s = input_text.strip()
    answer = solve_recursive(json.loads(s), question)

    if len(s) > 100:
        print(answer)
    else:
        print(f"{s}: {answer}")

print("Test")
print("Part 1")
solve("[1,2,3]", 1)
solve('{"a":2,"b":4}', 1)
solve("[[[3]]]", 1)
solve('{"a":{"b":4},"c":-1}', 1)
solve('{"a":[-1,1]}', 1)
solve('[-1,{"a":1}]', 1)
solve("[]", 1)
solve("{}", 1)
print("Part 2")
solve("[1,2,3]", 2)
solve('[1,{"c":"red","b":2},3]', 2)
solve('{"d":"red","e":[1,2,3,4],"f":5}', 2)
solve('[1,"red",5]', 2)

print("\nReal")
start_time = time.time()
solve(input_real, 1)
solve(input_real, 2)
elapsed_time = time.time() - start_time
print(f"Execution time: {elapsed_time} seconds")

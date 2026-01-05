import time

with open("input08.txt") as f:
    input_real = f.read()

input_test = '"" "abc" "aaa\\"aaa" "\\x27"'

def solve1(input_text):
    total = 0
    for word in input_text.split():
        n = 0
        i = 1
        while i < len(word) - 1:
            if word[i] == "\\":
                i += 4 if word[i+1] == "x" else 2
            else:
                i += 1
            n += 1
        total += len(word) - n
    print(total)

def solve2(input_text):
    total = 0
    for word in input_text.split():
        n = 0
        for c in word:
            n += 2 if c in ('"', "\\") else 1
        total += n - len(word) + 2
    print(total)

print("Test")
solve1(input_test)
solve2(input_test)
print("Real")
start_time = time.time()
solve1(input_real)
solve2(input_real)
elapsed_time = time.time() - start_time
print(f"Execution time: {elapsed_time} seconds")

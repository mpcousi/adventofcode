import time

with open("input05.txt") as f:
    input_real = f.read()

input_test1 = "ugknbfddgicrmopn aaa jchzalrnumimnmhp haegwjzuvuyypxyu dvszwmarrgswjxmb"
input_test2 = "qjhvhtzxzqqjkmpb xxyxx uurcxstgmygtbstg ieodomkazucvgmuy"

VOWELS = set(["a", "e", "i", "o", "u"])
SKIP = set(["ab", "cd", "pq", "xy"])

def solve1(input_text):
    total = 0

    for word in input_text.split():
        num_vowels = 1 if word[-1] in VOWELS else 0
        repeat = False
        skip = False

        for i in range(len(word) - 1):
            if word[i:i+2] in SKIP:
                skip = True
                break

            if word[i] == word[i+1]:
                repeat = True
            
            if word[i] in VOWELS:
                num_vowels += 1

        if not skip and repeat and num_vowels > 2:
            total += 1
        
    print(total)

def solve2(input_text):
    total = 0

    for word in input_text.split():
        repeats = False
        for i in range(len(word) - 1):
            for j in range(i+2, len(word) - 1):
                if word[i:i+2] == word[j:j+2]:
                    repeats = True
                    break
            if repeats:
                break

        if not repeats:
            continue

        repeats = False
        for i in range(1, len(word) - 1):
            if word[i-1] == word[i+1]:
                repeats = True
                break

        if repeats:
            total += 1
    
    print(total)

print("Test")
solve1(input_test1)
solve2(input_test2)
print("Real")
start_time = time.time()
solve1(input_real)
solve2(input_real)
elapsed_time = time.time() - start_time
print(f"Execution time: {elapsed_time} seconds")

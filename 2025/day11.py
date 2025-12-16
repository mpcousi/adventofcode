import time

with open("input11.txt") as f:
    input_real = f.read()

input_test1 = """aaa: you hhh
you: bbb ccc
bbb: ddd eee
ccc: ddd eee fff
ddd: ggg
eee: out
fff: out
ggg: out
hhh: ccc fff iii
iii: out"""

input_test2 = """svr: aaa bbb
aaa: fft
fft: ccc
bbb: tty
tty: ccc
ccc: ddd eee
ddd: hub
hub: fff
eee: dac
dac: fff
fff: ggg hhh
ggg: out
hhh: out"""

def solve1(state, connections, cache):
    if state in cache:
        return cache[state]
    elif state == "out":
        count = 1
    else:
       count = 0
       for output in connections[state]:
           count += solve1(output, connections, cache)
    
    cache[state] = count
    return count

def solve2(state, seen_fft, seen_dac, connections, cache):
    elem = (state, seen_fft, seen_dac)
    if elem in cache:
        return cache[elem]
    elif state == "out":
        count = int(seen_fft and seen_dac)
    else:
        count = 0
        for output in connections[state]:
            seen_fft2 = seen_fft or output == "fft"
            seen_dac2 = seen_dac or output == "dac"
            count += solve2(output, seen_fft2, seen_dac2, connections, cache)
    
    cache[elem] = count
    return count

def solve(input_text, question):
    connections = {}
    for line in input_text.split("\n"):
        parts = line.split(":")
        connections[parts[0]] = parts[1].split()

    if question == 1:
        answer = solve1("you", connections, {})
    else:
        answer = solve2("svr", False, False, connections, {})

    print(answer)

print("Test")
solve(input_test1, 1)
solve(input_test2, 2)
print("Real")
start_time = time.time()
solve(input_real, 1)
solve(input_real, 2)
elapsed_time = time.time() - start_time
print(f"Execution time: {elapsed_time} seconds")

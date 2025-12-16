import time

input_test = """3-5
10-14
16-20
12-18

1
5
8
11
17
32"""


with open("input05.txt") as f:
    input_real = f.read()


def merge_ranges(ranges, l2, r2):
    for i in range(len(ranges)):
        l,r = ranges[i]
        if l2 >= l and r2 <= r:
            return
        elif l2 <= l and r2 >= r:
            ranges[i][0] = l2
            ranges[i][1] = r2
            return
        elif l2 < l and r2 <= r and r2 + 1 >= l:
            ranges[i][0] = l2
            return
        elif l2 >= l and r2 > r and l2 - 1 <= r:
            ranges[i][1] = r2
            return
    
    ranges.append([l2,r2])


def solve(input_text):
    ranges = []
    num_fresh = 0
    gathering_ranges = True

    for x in input_text.split("\n"):
        if not x:
            gathering_ranges = False
        elif gathering_ranges:
            l,r = [int(x) for x in x.split("-")]
            merge_ranges(ranges, l, r)
        else:
            id = int(x)
            for l,r in ranges:
                if id >= l and id <= r:
                    num_fresh += 1
                    break

    print(num_fresh)

    while True:
        ranges2 = []
        for l,r in ranges:
            merge_ranges(ranges2, l, r)
        if len(ranges2) == len(ranges):
            break
        ranges = ranges2

    n = 0
    for l,r in ranges2:
        n += r-l+1

    print(n)

print("Test")
solve(input_test)

print("Real")
start_time = time.time()
solve(input_real)
elapsed_time = time.time() - start_time
print(f"Execution time: {elapsed_time} seconds")

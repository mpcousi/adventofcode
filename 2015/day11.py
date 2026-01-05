import time

with open("input11.txt") as f:
    input_real = f.read()

def increment(lst, i=None):
    i = len(lst) - 1 if i is None else i
    remainder = True
    while remainder and i >= 0:
        lst[i] = (lst[i] + 1) % 26
        remainder = lst[i] == 0
        i -= 1
    return [1] + lst if remainder else lst

SKIP = ["i", "o", "l"]
def solve(input_text):
    values = [ord(c) - ord("a") for c in input_text.strip()]
    skip = [ord(c) - ord("a") for c in SKIP]
    to_increment = True

    while True:
        if to_increment:
            values = increment(values)
        
        i_skip = None
        for c in skip:
            try:
                pos = values.index(c)
                if i_skip is None or pos < i_skip:
                    i_skip = pos
            except ValueError:
                pass
        if i_skip:
            values = increment(values, i_skip)
            for j in range(i_skip + 1, len(values)):
                values[j] = 0
            to_increment = False
            continue
        else:
            to_increment = True
        
        sequence_length = 1
        found_sequence = False
        found_pairs = 0
        i_last_pair = -1
        for i in range(1, len(values)):
            if values[i-1] == values[i] - 1:
                sequence_length += 1
                if sequence_length == 3:
                    found_sequence = True
            else:
                sequence_length = 1
                if values[i-1] == values[i] and i-1 != i_last_pair:
                    found_pairs += 1
                    i_last_pair = i
        
        if found_sequence and found_pairs > 1:
            break

    result = "".join([chr(ord("a") + x) for x in values])
    print(result)
    return result

print("Test")
solve("abcdefgh")
solve("ghijklmn")
print("Real")
start_time = time.time()
part1 = solve(input_real)
solve(part1)
elapsed_time = time.time() - start_time
print(f"Execution time: {elapsed_time} seconds")

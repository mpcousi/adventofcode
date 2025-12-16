import time

input_test = """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  """

with open("input06.txt") as f:
    input_real = f.read()

def solve1(input_text, question):
    lines = input_text.split("\n")
    nums = None
    total = 0

    for i in range(len(lines)):
        if i < len(lines) - 1:
            line_nums = [int(x) for x in lines[i].split()]
            if not nums:
                nums = [[] for _ in range(len(line_nums))]

            if len(nums) != len(line_nums):
                raise ValueError("Uh oh!")
            for j in range(len(line_nums)):
                nums[j].append(line_nums[j])
        else:
            operations = [x for x in lines[i].split()]
            if question == 1:
                for j in range(len(nums)):
                    subtotal = nums[j][0]
                    for k in range(1, len(nums[j])):
                        if operations[j] == "*":
                            subtotal *= nums[j][k]
                        elif operations[j] == "+":
                            subtotal += nums[j][k]
                    total += subtotal
            else:
                for j in range(len(nums)):
                    line_str = [str(x) for x in nums[j]]
                    max_str_len = max([len(x) for x in line_str])
                    subtotal = None
                    for k in range(-1, -max_str_len-1, -1):
                        operand = ""
                        for l in range(len(nums[j])):
                            if len(line_str[l]) >= -k:
                                operand += line_str[l][k]
                        
                        operand = int(operand)
                        if subtotal is None:
                            subtotal = operand
                        elif operations[j] == "*":
                            subtotal *= operand
                        else:
                            subtotal += operand
                    total += subtotal

    return total

def solve2(input_text):
    lines = input_text.split("\n")
    all_nums = []
    total = 0

    operations = []
    distances = []
    distance = None
    for j in range(len(lines[-1])):
        if lines[-1][j] == " ":
            distance += 1
        else:
            operations.append(lines[-1][j])
            if distance is not None:
                distances.append(distance)
            distance = 0

    if distance > 0:
        distances.append(distance + 1)

    ii = 0
    jj = 0
    for l in range(len(operations)):
        subtotal = None
        jj += distances[l] + 1

        for j in range(distances[l]):
            operand = ""
            for i in range(len(lines) - 1):
                num = lines[i][ii:jj]
                if j < len(num):
                    operand += num[j]
                else:
                    raise ValueError("This should not happen!")
            try:
                n = int(operand.strip())
            except:
                continue
            if subtotal is None:
                subtotal = n
            elif operations[l] == "+":
                subtotal += n
            else:
                subtotal *= n
        ii = jj

        if subtotal is not None:
            total += subtotal
    return total

print("Test")
print(solve1(input_test, 1))
print(solve2(input_test))
print("Real")
start_time = time.time()
print(solve1(input_real, 1))
print(solve2(input_real))
elapsed_time = time.time() - start_time
print(f"Execution time: {elapsed_time} seconds")

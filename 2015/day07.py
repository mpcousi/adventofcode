import time
from collections import deque

with open("input07.txt") as f:
    input_real = f.read()

def get_value(operator, values):
    return int(operator) if operator.isnumeric() else values[operator]

def compute(operation, operands):
    if operation == None:
        return operands[0]
    elif operation == "NOT":
        return ~operands[0]
    elif operation == "AND":
        return operands[0] & operands[1]
    elif operation == "OR":
        return operands[0] | operands[1]
    elif operation == "LSHIFT":
        return operands[0] << operands[1]
    elif operation == "RSHIFT":
        return operands[0] >> operands[1]

def solve(input_text, values={}):
    to_skip = set(values.keys())
    instructions = deque(input_text.split("\n"))

    while instructions:
        instruction = instructions.popleft()
        if not instruction:
            continue
        operators, operand = instruction.split(" -> ")
        if operand in to_skip:
            continue

        operators = operators.split()
        op_index = len(operators) - 2
        operation = operators[op_index] if op_index >= 0 else None

        try:
            operands = [get_value(x, values) for i,x in enumerate(operators) if i != op_index]
        except KeyError:
            instructions.append(instruction)
            continue

        values[operand] = compute(operation, operands) & 0xFFFF

    print(values["a"])
    return values["a"]

start_time = time.time()
solve(input_real, {"b": solve(input_real)})
elapsed_time = time.time() - start_time
print(f"Execution time: {elapsed_time} seconds")

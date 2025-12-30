import time

with open("input09.txt") as f:
    input_real = f.read()

input_test = """7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3
7,1"""

def solve(input_text):
    points = [[int(x) for x in y.split(",")] for y in input_text.split()]
    part1 = 0
    part2 = 0

    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            red_x1, red_y1 = points[i]
            red_x2, red_y2 = points[j]

            red_x1, red_x2 = min(red_x1, red_x2), max(red_x1, red_x2)
            red_y1, red_y2 = min(red_y1, red_y2), max(red_y1, red_y2)

            area = (red_x2 - red_x1 + 1) * (red_y2 - red_y1 + 1)
            part1 = max(part1, area)

            if area > part2:
                green_line_intersects = False
                for k in range(len(points)):
                    l = k + 1 if k < len(points) - 1 else 0
                    green_x1, green_y1 = points[k]
                    green_x2, green_y2 = points[l]

                    green_x1, green_x2 = min(green_x1, green_x2), max(green_x1, green_x2)
                    green_y1, green_y2 = min(green_y1, green_y2), max(green_y1, green_y2)

                    if green_x1 < red_x2 and green_x2 > red_x1 and green_y1 < red_y2 and green_y2 > red_y1:
                        green_line_intersects = True
                        break

                if not green_line_intersects:
                    part2 = area

    print(part1)
    print(part2)

print("Test")
solve(input_test)
print("Real")
start_time = time.time()
solve(input_real)
elapsed_time = time.time() - start_time
print(f"Execution time: {elapsed_time} seconds")

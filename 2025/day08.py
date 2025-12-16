import heapq
import time

with open("input08.txt") as f:
    input_real = f.read()

input_test = """162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689"""

def solve(input_text, n=None):
    heap = []
    points = []
    circuits_to_points = {}
    points_to_circuits = {}

    for i, line in enumerate(input_text.split()):
        points.append([int(x) for x in line.split(",")])
        circuits_to_points[i] = set([i])
        points_to_circuits[i] = i

    for i in range(len(points)):
        for j in range(i+1, len(points)):
            dist = sum([(points[i][l] - points[j][l]) ** 2 for l in range(3)])
            heapq.heappush(heap, (dist, i, j))

    it = 0
    while heap:
        _, i, j = heapq.heappop(heap)
        circuit1 = points_to_circuits[i]
        circuit2 = points_to_circuits[j]
        if circuit1 != circuit2:
            for point in circuits_to_points[circuit2]:
                points_to_circuits[point] = circuit1
            circuits_to_points[circuit1] = circuits_to_points[circuit1].union(circuits_to_points[circuit2])
            del circuits_to_points[circuit2]

        it += 1
        if it == n:
            circuit_heap = []
            for circuit in circuits_to_points:
                heapq.heappush(circuit_heap, len(circuits_to_points[circuit]))
            largest3 = heapq.nlargest(3, circuit_heap)
            print(largest3[0] * largest3[1] * largest3[2])
        elif len(circuits_to_points) == 1:
            print(points[i][0] * points[j][0])
            return

print("Test")
solve(input_test, 10)
print("Real")
start_time = time.time()
solve(input_real, 1000)
elapsed_time = time.time() - start_time
print(f"Execution time: {elapsed_time} seconds")

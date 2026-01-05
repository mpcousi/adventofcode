import time

with open("input14.txt") as f:
    input_real = f.read()

input_test = """Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds."""

def solve(input_text, seconds):
    birds = {}
    for line in input_text.strip().split("\n"):
        parts = line.split()
        fly_time = int(parts[6])
        birds[parts[0]] = {
            "speed": int(parts[3]),
            "fly_time": fly_time,
            "rest_time": int(parts[-2]),
            "fly_time_left": fly_time,
            "rest_time_left": None,
            "dist": 0,
            "points": 0
        }

    for _ in range(seconds):
        max_dist = 0
        birds_max_dist = None
        for bird, vals in birds.items():
            if vals["fly_time_left"] is not None:
                vals["fly_time_left"] -= 1
                vals["dist"] += vals["speed"]
                if vals["fly_time_left"] == 0:
                    vals["fly_time_left"] = None
                    vals["rest_time_left"] = vals["rest_time"]
            else:
                vals["rest_time_left"] -= 1
                if vals["rest_time_left"] == 0:
                    vals["rest_time_left"] = None
                    vals["fly_time_left"] = vals["fly_time"]

            if vals["dist"] > max_dist:
                max_dist = vals["dist"]
                birds_max_dist = [bird]
            elif vals["dist"] == max_dist:
                birds_max_dist.append(bird)

        for bird in birds_max_dist:
            birds[bird]["points"] += 1

    print(max_dist)
    max_point = 0
    for bird in birds:
        max_point = max(max_point, birds[bird]["points"])
    print(max_point)

print("Test")
solve(input_test, 1000)
print("Real")
start_time = time.time()
solve(input_real, 2503)
elapsed_time = time.time() - start_time
print(f"Execution time: {elapsed_time} seconds")

import os
import subprocess
import sys
import time
from multiprocessing import Process, Queue
from rich.progress import Progress, SpinnerColumn, TextColumn, TimeElapsedColumn

script_dir = os.path.dirname(os.path.abspath(__file__))

def execute_script(day_id, queue, parent_folder):
    start_time = time.time()
    subprocess.run([sys.executable, f"day{str(day_id).zfill(2)}.py"], cwd=parent_folder, capture_output=True)
    elapsed_time = time.time() - start_time
    queue.put((day_id, elapsed_time))

def execute_year(year, parent_folder, num_tasks):
    num_workers = 8
    num_finished = 0
    next_process = num_workers
    queue = Queue()

    processes = [Process(target=execute_script, args=(i, queue, parent_folder)) for i in range(1, num_tasks+1)]
    global_start_time = time.time()

    with Progress(SpinnerColumn(), TextColumn("{task.description}"), TimeElapsedColumn(), transient=False) as progress:
        tasks = [progress.add_task(f"{year}.{str(i).zfill(2)}", total=None) for i in range(1, num_tasks+1)]
        for i in range(num_workers):
            processes[i].start()

        while num_finished < num_tasks:
            day_id, elapsed_time = queue.get()
            progress.update(tasks[day_id-1], description=f"{year}.{str(day_id).zfill(2)} - done in {elapsed_time:.4f}s")
            progress.stop_task(tasks[day_id-1])
            num_finished += 1
            if next_process < num_tasks:
                processes[next_process].start()
                next_process += 1

    for process in processes:
        process.join()

    elapsed_time = time.time() - global_start_time
    print(f"All runs: {elapsed_time:.4f} seconds")

if __name__ == "__main__":
    is_year = lambda x: os.path.isdir(os.path.join(script_dir, x)) and x.startswith("2")
    valid_years = [x for x in os.listdir(script_dir) if is_year(x)]
    
    if len(sys.argv) < 2 or sys.argv[1] not in valid_years:
        print(f"Please specify a year to run. Valid: {', '.join(valid_years)}")
    else:
        year_folder = os.path.join(script_dir, sys.argv[1])
        days = [x for x in os.listdir(year_folder) if x.startswith("day")]
        last_day = int(sorted(days)[-1].split("y")[1].split(".")[0])
        execute_year(sys.argv[1], year_folder, last_day)

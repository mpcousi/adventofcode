import subprocess
import sys
import time
from multiprocessing import Process, Queue
from rich.progress import Progress, SpinnerColumn, TextColumn, TimeElapsedColumn


def execute_script(day_id, queue):
    start_time = time.time()
    subprocess.run([sys.executable, f"day{str(day_id).zfill(2)}.py"], capture_output=True)
    elapsed_time = time.time() - start_time
    queue.put((day_id, elapsed_time))


if __name__ == "__main__":
    num_tasks = 25
    num_workers = 8
    num_finished = 0
    next_process = num_workers
    queue = Queue()

    processes = [Process(target=execute_script, args=(i, queue)) for i in range(1, num_tasks+1)]
    global_start_time = time.time()

    with Progress(SpinnerColumn(), TextColumn("{task.description}"), TimeElapsedColumn(), transient=False) as progress:
        tasks = [progress.add_task(f"Day {str(i).zfill(2)}", total=None) for i in range(1, num_tasks+1)]
        for i in range(num_workers):
            processes[i].start()

        while num_finished < num_tasks:
            day_id, elapsed_time = queue.get()
            progress.update(tasks[day_id-1], description=f"Day {str(day_id).zfill(2)} - done in {elapsed_time:.4f}s")
            progress.stop_task(tasks[day_id-1])
            num_finished += 1
            if next_process < num_tasks:
                processes[next_process].start()
                next_process += 1

    for process in processes:
        process.join()

    elapsed_time = time.time() - global_start_time
    print(f"All runs: {elapsed_time:.4f} seconds")

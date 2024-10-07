# Here's an example of multiprocessing in Python using the multiprocessing module. 
# This example demonstrates how to run CPU-bound tasks in parallel across multiple processes to take advantage of multiple CPU cores.

# Example: Multiprocessing in Python
import multiprocessing
# Task: A function that performs a heavy computation (CPU-bound task)
def cpu_bound_task(number):
    total = 0
    for i in range(1, 10000000):  # Simulate a heavy computation task
        total += i
    print(f"Task for number {number} completed. Total sum: {total}")

if __name__ == "__main__":
    # Creating multiple processes to run the CPU-bound task
    process1 = multiprocessing.Process(target=cpu_bound_task, args=(1,))
    process2 = multiprocessing.Process(target=cpu_bound_task, args=(2,))
    process3 = multiprocessing.Process(target=cpu_bound_task, args=(3,))

    # Starting the processes
    process1.start()
    process2.start()
    process3.start()

    # Waiting for all processes to complete
    process1.join()
    process2.join()
    process3.join()

    print("All tasks completed")
# Explanation:
# Process 1, Process 2, and Process 3 each run cpu_bound_task in parallel. This simulates CPU-bound work (e.g., number crunching), where the sum of numbers from 1 to 10,000,000 is calculated independently in each process.
# The multiprocessing.Process class is used to create separate processes that run concurrently on different CPU cores.
# start() is called to begin the execution of each process, and join() ensures that the main program waits until all processes are completed.
# Output:
# mathematica
# Copy code
# Task for number 1 completed. Total sum: 49999995000000
# Task for number 2 completed. Total sum: 49999995000000
# Task for number 3 completed. Total sum: 49999995000000
# All tasks completed
# Key Points:
# Parallelism: Each process runs independently on a separate CPU core, achieving true parallelism.
# No GIL Limitation: Unlike multithreading, multiprocessing bypasses Python's Global Interpreter Lock (GIL), so this method is suitable for CPU-bound tasks where heavy computations need to be spread across multiple cores.
# Memory: Each process has its own memory space, so they don't share memory like threads. This makes it harder to share data but avoids the complexities of multithreading (e.g., race conditions).
# This example shows how to use multiprocessing for parallel execution of CPU-intensive tasks.
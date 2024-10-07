# Here's an example of multithreading in Python that demonstrates how to run multiple tasks concurrently using the threading module. 
# In this example, two threads perform different tasks simultaneously: one thread sleeps for a while and prints a message, while the other does some computations.
# Example: Multithreading in Python
import threading
import time
# Task 1: A function that simulates an I/O-bound operation (sleeping)
def io_bound_task():
    print("IO-bound task started")
    time.sleep(5)  # Simulate an I/O operation
    print("IO-bound task finished after sleeping")
# Task 2: A function that simulates a CPU-bound operation (computations)
def cpu_bound_task():
    print("CPU-bound task started")
    total = 0
    for i in range(1_000_000):  # Simulate a heavy computation task
        total += i
    print(f"CPU-bound task finished. Total sum: {total}")
# Creating threads for each task
thread1 = threading.Thread(target=io_bound_task)
thread2 = threading.Thread(target=cpu_bound_task)
# Starting the threads
thread1.start()
thread2.start()
# Waiting for both threads to complete
thread1.join()
thread2.join()

print("Both tasks completed")
# Explanation:
# Thread 1 (thread1) executes io_bound_task, which simulates an I/O-bound task by sleeping for 5 seconds. 
# This would represent tasks like file reading, waiting for network responses, etc.
# Thread 2 (thread2) executes cpu_bound_task, which simulates a CPU-bound task by performing a heavy computation (summing numbers from 1 to 1,000,000).
# Both threads run concurrently, so the CPU-bound task can progress while the I/O-bound task is waiting.
# Output:
# IO-bound task started
# CPU-bound task started
# CPU-bound task finished. Total sum: 499999500000
# IO-bound task finished after sleeping
# Both tasks completed
# This demonstrates how multithreading allows for the overlap of tasks, like running the CPU-intensive code while waiting for I/O operations to complete.
# Here's an example of asynchronous programming in Python using the asyncio module. 
# This example demonstrates how to run multiple asynchronous tasks concurrently, specifically focusing on I/O-bound tasks like network operations or file I/O.

# Example: Asynchronous Programming in Python with asyncio
import asyncio
# Simulate an I/O-bound task using asyncio (e.g., network request or file read)
async def io_bound_task(name, delay):
    print(f"Task {name} started, will take {delay} seconds...")
    await asyncio.sleep(delay)  # Simulates an I/O wait using non-blocking sleep
    print(f"Task {name} finished after {delay} seconds")

# Main function to run multiple asynchronous tasks concurrently
async def main():
    # Create multiple tasks that will run concurrently
    task1 = asyncio.create_task(io_bound_task("A", 3))
    task2 = asyncio.create_task(io_bound_task("B", 2))
    task3 = asyncio.create_task(io_bound_task("C", 1))
    
    # Wait for all tasks to complete
    await task1
    await task2
    await task3

# Run the main function using asyncio event loop
asyncio.run(main())

# Explanation:
# io_bound_task: This simulates an I/O-bound operation that takes a specific number of seconds to complete. The asyncio.sleep() function is used to simulate non-blocking waiting, which means the program can run other tasks while waiting for this one to complete.
# main function: Three asynchronous tasks (task1, task2, task3) are created and started concurrently. Instead of blocking the program (like time.sleep() would do), asyncio.sleep() allows the event loop to switch to another task while waiting.
# asyncio.run(): The entry point for running the main function, which sets up and manages the event loop.
# Output:
# arduino
# Copy code
# Task A started, will take 3 seconds...
# Task B started, will take 2 seconds...
# Task C started, will take 1 second...
# Task C finished after 1 seconds
# Task B finished after 2 seconds
# Task A finished after 3 seconds
# Key Points:
# Concurrency with Asynchronous Programming: Tasks are run concurrently in a non-blocking fashion, meaning the tasks don’t block the main program while waiting for external operations (e.g., I/O).
# Efficient for I/O-bound Tasks: This approach is best suited for tasks like web scraping, file I/O, database queries, and handling many connections in networking apps.
# async and await keywords: These enable asynchronous programming. You define a function as async and use await to pause execution while waiting for an asynchronous operation (like asyncio.sleep()).
# In this example, the tasks run concurrently, meaning the program switches between tasks when one is waiting for an I/O operation to complete. This makes asyncio great for high-performance I/O-bound applications that need to handle many tasks at once.
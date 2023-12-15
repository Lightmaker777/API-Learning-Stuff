import asyncio

async def process(name, duration):
    print(f"Process {name} started")
    await asyncio.sleep(duration)
    print(f"Process {name} completed after {duration} seconds")

async def main():
    # Define durations for each process
    durations = [3, 2, 1]
    # Create a list to hold the task objects
    tasks = []
    # Start the processes asynchronously
    for i, duration in enumerate(durations):
        task = asyncio.create_task(process(f"#{i + 1}", duration))
        tasks.append(task)
    # Wait for all processes to complete
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    # Run the main asynchronous program
    asyncio.run(main())

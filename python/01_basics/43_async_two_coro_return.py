import asyncio
from time import time

async def fetch_data_1():
    await asyncio.sleep(2) # Simulate an IO-bound task
    return "Data from coroutine 1"

async def fetch_data_2():
    await asyncio.sleep(1) # Simulate an IO-bound task
    return "Data from coroutine 2"

async def main():
    # Run fetch_data_1 and fetch_data_2 concurrently
    result1, result2 = await asyncio.gather(fetch_data_1(), fetch_data_2())
    
    # Retrieve and print the results
    print(result1)  # Output: Data from coroutine 1
    print(result2)  # Output: Data from coroutine 2

# Run the main coroutine
print(time())
asyncio.run(main())
print(time())

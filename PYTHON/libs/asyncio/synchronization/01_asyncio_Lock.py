lock = asyncio.Lock()

# ... later
async with lock:
    # access shared state
    pass

from loguru import logger

# just console
a = 1
logger.debug(f"Hello, World (debug)! a={a}")
logger.info("Hello, World (info)!")
logger.error("Hello, World (error)!")

# write log to file
logger.add("logs/debug.log", format="{time} {level} {message}", level="DEBUG")
logger.debug("Hello, World (debug)!")
logger.info("Hello, World (info)!")
logger.error("Hello, World (error)!")

# log rotation
logger.add("debug.log", format="{time} {level} {message}", level="DEBUG", rotation="10 KB")
logger.debug("Hello, World (debug)!")
logger.info("Hello, World (info)!")
logger.error("Hello, World (error)!")

# log rotation with compression
logger.add("info.log", format="{time} {level} {message}", level="DEBUG", rotation="10 KB", compression="zip")
for _ in range(1000):
    logger.info("Hello, World (info)!")

# log rotation not by size, but by time. Once in week
logger.add("info.log", format="{time} {level} {message}", level="DEBUG", rotation="1 week", compression="zip")
for _ in range(1000):
    logger.info("Hello, World (info)!")

# log rotation not by size, but by time. Every day at 10:00
logger.add("info.log", format="{time} {level} {message}", level="DEBUG", rotation="1 week", compression="zip")
for _ in range(1000):
    logger.info("Hello, World (info)!")

# catch exceptions
@logger.catch
def foo():
    pass

# save logs in JSON format (to parse in future)
logger.add("info.log", format="{time} {level} {message}", level="DEBUG", rotation="1 week", compression="zip", serialize=True)
for _ in range(1000):
    logger.info("Hello, World (info)!")


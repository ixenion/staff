from loguru import logger

# log to file
# logger.add("debug.log", format="{time} {level} {message}", level="DEBUG")
# logging with rotation. When log gets > 10 KB it moved and new log started. But it pointless without compression.
# logger.add("debug.log", format="{time} {level} {message}", level="DEBUG", rotation="10 KB")
# rotation with compression
logger.add("debug.log", format="{time} {level} {message}", level="DEBUG", rotation="10 KB", compression="zip")
# possible rotations: 10 MB, 1 week (rotate once a week), 10:00 (rotation every morning at 10:00)

# main functions
logger.debug("Hello world (debug!)")
logger.info("Hello world (info!)")
logger.error("Hello world (error!)")

for _ in range(1000):
    logger.info("Hello world (info!)")

from loguru import logger

# just console
a = 1
logger.debug(f"Hello, World (debug)! a={a}")
logger.info("Hello, World (info)!")
logger.error("Hello, World (error)!")

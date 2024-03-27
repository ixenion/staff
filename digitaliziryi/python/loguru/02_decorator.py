from loguru import logger

logger.add("debug.log", format="{time} {level} {message}", level="DEBUG", rotation="10 KB", compression="zip")

def divide(a, b):
    return a / b

# use decorator
@logger.catch
def main():
    divide(a, b)

main()


from loguru import logger

# to save as json: add param "serialize=True"
logger.add("debug.log", format="{time} {level} {message}", level="DEBUG", rotation="10 KB", compression="zip", serialize=True)

def divide(a, b):
    return a / b

# use decorator
@logger.catch
def main():
    divide(1, 0)

main()


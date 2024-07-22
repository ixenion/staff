import time

def timer(func):
    def wrapper():
        before = time.time()
        func()
        print("Function took:", time.time() - before, "seconds")

    return wrapper

@timer
def main():
    time.sleep(2)
    
main()

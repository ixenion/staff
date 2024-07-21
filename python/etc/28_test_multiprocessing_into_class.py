import multiprocessing
from multiprocessing import Process
from time import sleep

class F:
    
    def __init__(self):
        self.count = 0

    def count_inc(self):
        while True:
            sleep(2)
            self.count += 1

    def count_print(self):
        while True:
            sleep(1)
            print(self.count)


    def start(self):

        self.proc = Process(target=self.count_inc)
        self.proc.start()

        self.count_print()

    def __enter__(self):
        print(f'Started')
        self.start()

    def __exit__(self, exc_type, exc_value, exc_tb):
        self.proc.close()
        print(f'Process closed')


# with F as foo:
#     foo.start()

# class HelloContextManager:
#     def __enter__(self):
#         print("Entering the context...")
#         return "Hello, World!"
#     def __exit__(self, exc_type, exc_value, exc_tb):
#         print("Leaving the context...")
#         print(exc_type, exc_value, exc_tb, sep="\n")
# with HelloContextManager() as hello:
#     print(hello)
class HelloContextManager:
    def __enter__(self):
        print("Entering the context...")
        self.start()
        return "Hello, World!"
    def __exit__(self, exc_type, exc_value, exc_tb):
        self.proc.close()
        print("Leaving the context...")
        print(exc_type, exc_value, exc_tb, sep="\n")

    def __init__(self):
        # self.count = 0
        # initialize an integer shared variable
        self.count = multiprocessing.Value('i', 0)

    def count_inc(self):
        while True:
            sleep(3)
            self.count.value += 1
            print(f'Procc: {self.count.value}')

    def count_print(self):
        while True:
            sleep(1)
            print(f'Main: {self.count.value}')
            a = self.proc.is_alive()
            print(f'{a}')


    def start(self):

        self.proc = Process(target=self.count_inc)
        self.proc.start()

        self.count_print()
with HelloContextManager() as hello:
    print(hello)

# Multithreaded status code reading
import time
import threading
import requests

def read_example(dl: int) -> None:
    time.sleep(dl)
    response = requests.get('https://www.example.com')
    print(response.status_code)

thread_1 = threading.Thread(target=read_example, args=(1,))
thread_2 = threading.Thread(target=read_example, args=(5,))
thread_start = time.time()
thread_1.start()
thread_2.start()
print('All threads running!')
# thread_1.join()
print(f'JOIN 1')
# thread_2.join()
print(f'JOIN 2')
thread_end = time.time()
print(f'Running with threads took {thread_end - thread_start:.4f} seconds.')

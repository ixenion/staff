from time import sleep

a = 1
b = 0
c = 2

while True:
    try:
        a/c
        print(f'No exception')
        break
    except:
        print(f'Exception')
        sleep(1)
print(f'Out of cycle')

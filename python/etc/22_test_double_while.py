from time import sleep

while True:
    print('outer')
    while True:
        print('inner')
        sleep(1)
        break

import os
import sys
from time import sleep

print(f"\nInitialised")
print(f"Python version: {sys.version}")
print(f"Script args: {sys.argv}")

i = 5
while i:
    print(i)
    sleep(1)
    i -= 1
    if i == 2:
        print(f"Restarting...")
        sleep(1)
        os.execv(sys.executable, ['python'] + [*sys.argv])


# print(f"Restarting...")
# sleep(1)
# run without args
# os.execv(sys.executable, ['python'] + [sys.argv[0]])
# with args
# os.execv(sys.executable, ['python'] + [*sys.argv])

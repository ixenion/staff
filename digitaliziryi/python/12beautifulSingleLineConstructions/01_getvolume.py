# usage:
# python3 getvolume.py <<< "10 20 30"

sizes = input()
sizes = sizes.strip()
sizes = sizes.split()   # by default splits by "space"
x = sizes[0]
y = sizes[1]
z = sizes[2]

x = int(x)
y = int(y)
z = int(z)
volume = x * y * z

# simplier
x, y, z = input().strip().split()
x, y, z = map(int, (x, y, z))
volume = x * y * z

# more simplier
x, y, z = map(int, (input().strip().split()))
volume = x * y * z

# MORE simplier
from functools import reduce

volume = reduce(
        lambda x, y: x * y,
        map(int, (input().strip().split()))
        )




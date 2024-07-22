def f():
    x = 20
    y = 20

    def g():
        global x
        nonlocal y
        x = 40
        y = 40
    g()
    print(f"x: {x}")
    print(f"y: {y}")

f()
print(f"x: {x}")
print(f"y: {y}")

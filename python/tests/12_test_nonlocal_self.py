def foo():
    nonlocal var1
    var1 = 2
    print(var1)
    pass

class P:
    def __init__(self):
        self.var1 = 1
        pass
    def bar(self):
        foo()


p = P
p.bar()
print(f"###\n{p.var1}")

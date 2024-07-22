class F:
    A = 123
    def foo(self):
        # Can get 'A', but not set
        print(f'foo: {self.A}')
        # local variable A
        self.A = 321
        print(f'foo: {self.A}')

    @classmethod
    def bar(cls):
        print(f'bar: {cls.A}')
        cls.A = 456
        print(f'bar: {cls.A}')

f = F()
a = F()
f.foo()
f.bar()
f.bar()
print(a.A)

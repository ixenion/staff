

class A:

    abc = '123'

    def foo(self):
        print(f'foo0')
        pass

def bar():
    abc = '321'
    print(f'barr')
    print(f'{abc}')

setattr(A, 'bar', bar)
A.bar()
print(A.abc)

# try:
#     getattr(A, 'foo')
#     print(f'True')
# except AttributeError:
#     print(f'False')

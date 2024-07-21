
def foo(a:float, /, b:int, g:str|None=None):
    print(foo.__globals__)

foo(1, 2, '1.7')
foo(1, 2, g='1.7')

def bar(a:float, *, b:int, g:str|None=None):
    print(foo.__globals__)

bar(a=1, b=2, g='1.7')
bar(1, b=2, g='1.7')

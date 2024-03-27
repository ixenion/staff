from time import sleep, time

# axiluary decorator method

def timeit(method):
    def timed(*args, **kw):
        ts = time()
        result = method(*args, **kw)
        te = time()
        delta = (te - ts) * 1000
        print(f'{method.__name__} took {delta:2.2f} ms')
        return result
    return timed

def timeit_all_methods(cls):
    class NewCls:
        def __init__(self, *args, **kwargs):
            # proxy class creating
            self._obj = cls(*args, **kwargs)

        def __getattribute__(self, s:str):
            print(f'NEW attribute:')
            print(f'{s}')
            try:
                # Is there attibute "s"?
                x = super().__getattribute__(s)
                # x = self.__getattribute__(s)
                print(f'Attribute {s} exists in decorator class.')
            except AttributeError:
                # there is no such attribute
                print(f'There is NO such attribute:\n{s}')
                pass
            else:
                # There is attibute "s"
                print(f'There IS attibute:\n{s}\nsuper x:\n{x}')
                return x

            # If "object" - must be attribute "s"
            attr = self._obj.__getattribute__(s)

            # Is it a method?
            if isinstance(attr, type(self.__init__)):
                # Yes - wrap it to timeit decorator
                print(f'This IS class method:\n{s}')
                return timeit(attr)
            else:
                # Not method, but something else
                print(f'This is NOT class method:\n{s}')
                return attr

        def a(self):
            print(f'Im existing in class decorator!')
    
    return NewCls


@timeit_all_methods
class Foo:
    def a(self):
        print('Method a started.')
        sleep(0.088)
        print('Method a stopped.')
    def b(self):
        print('Method b started.')
        sleep(0.088)
        print('Method b stopped.')

f = Foo()
f.b()
f.a()

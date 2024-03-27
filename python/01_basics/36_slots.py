# check
# https://habr.com/ru/post/686220/

# slots reduces RAM usage when creating class objects;
# also reduces time consumption when access property.

class Foo(object): 
  __slots__ = ('foo',)

  
class Bar(object): 
  pass


def get_set_delete(obj):
  obj.foo = 'foo'
  obj.foo
  del obj.foo
  
def test_foo():  
  get_set_delete(Foo())
  
def test_bar():
  get_set_delete(Bar())

import timeit

result1 = min(timeit.repeat(test_foo))
# 0.2567792439949699

result2 = min(timeit.repeat(test_bar))
# 0.34515008199377917


# example 2

class BaseOne:
  __slots__ = ('param1',)

  
class BaseTwo:
  __slots__ = ('param2',)

class BaseThree:
  __slots__ = ()

# class Child(BaseOne, BaseTwo): __slots__ = ()
# TypeError: multiple bases have instance lay-out conflict

class Child(BaseOne, BaseThree): __slots__ = ()
# OK
# One parent class might have slots,
# other parents must have empty slots

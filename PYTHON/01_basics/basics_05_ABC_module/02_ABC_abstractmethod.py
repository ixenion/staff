# tutorial
# https://tirinox.ru/abstract-class-abc/


from abc import ABC, abstractmethod

class Hero(ABC):
    @abstractmethod
    def attack(self):
        """ Defines attack type """
    
class Archer(Hero):
    def attack(self):
        print('выстрел из лука')

Archer().attack()

# Supports 'classmethod' & 'staticmethod' decorators.
# Also check:
# staff/python/basics/basics_02_decorators/06_classmethodANDstatickmethod_decorator.py
class C(ABC):
   @classmethod
   @abstractmethod
   def my_abstract_classmethod(cls):
       ...
   @staticmethod
   @abstractmethod
   def my_abstract_staticmethod():
       ...
   @property
   @abstractmethod
   def my_abstract_property(self):
       ...
   @my_abstract_property.setter
   @abstractmethod
   def my_abstract_property(self, val):
       ...



# Lets have a look at simple class
# from which we want inherit to

class MontyPython:
    def joke(self):
        raise NotImplementedError()

    def punchline(self):
        raise NotImplementedError()

class ArgumentClinic(MontyPython):
    def joke(self):
        return "Hahahahahah"

# When we create object from 'ArgumentClinic'
# and try to use 'punchline' method
# error raised
sketch = ArgumentClinic() 
sketch.punchline()
# AttributeError: 'ArgumentClinic' object has no attribute 'punchline'

# But it would be cool to catch error
# On object creation part.


# so use ABCMeta & abstractmethod

from abc import ABCMeta, abstractmethod
class MontyPython(metaclass=ABCMeta):
    @abstractmethod
    def joke(self):
        pass
    @abstractmethod
    def punchline(self):
        pass

class ArgumentClinic(MontyPython):
    def joke(self):
        return "Hahahaha"

c = ArgumentClinic()
# TypeError: "Can't instantiate abstract class ArgumentClinic with abstract methods punchline"



from abc import ABC, ABCMeta
# for Python 3.4+
class Hero(ABC):
    ...
# for Python 3.0+
class Hero(metaclass=ABCMeta):
    ...

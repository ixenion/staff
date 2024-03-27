from typing import final, Final

# FOO is marked final, can't assign another value to it
FOO: Final[int] = 42

class Foo:
    @final
    def spam(self) -> int:
        """A final method can't be overridden in a subclass"""
        return 42

@final
class Bar:
    """A final class can't be subclassed"""

# Rule breaking section
FOO = 81

class Spam(Foo, Bar):
    def spam(self) -> int:
        return 17

if __name__ == '__main__':
    print("FOO:", FOO)
    print("Spam().spam():", Spam().spam())


# $ python3.8 demo.py   # Python will not throw errors here
# FOO: 81
# Spam().spam(): 17
# $ mypy demo.py        # only a type checker will
# demo.py:17: error: Cannot assign to final name "FOO"
# demo.py:19: error: Cannot inherit from final class "Bar"
# demo.py:20: error: Cannot override final attribute "spam" (previously declared in base class "Foo")

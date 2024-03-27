# tutorial
# https://habr.com/ru/post/415829/


# PROBLEM (too long)
class RegularBook:
    def __init__(self, title, author):
        self.title = title
        self.author = author

# DATA CLASS USAGE

from dataclasses import dataclass

@dataclass
class Book:
    title: str
    author: str

book = Book(title="Fahrenheit 451", author="Bradbury")
print(book.author)

# immutable data classes
@dataclass(frozen=True)
class Book2:
    title: str
    author: str
book = Book("Fahrenheit 451", "Bradbury")
# book.title = "1984"   # throws an error
# dataclasses.FrozenInstanceError: cannot assign to field 'title'

from dataclasses import field
from typing import List

@dataclass
class Bookshelf:
    books: List[Book] = field(default_factory=list)

book2 = Book("Fahrenheit 451", "Bradbury")
book3 = Book("1984", "Oruel")
bsh = Bookshelf([book2, book3])
print(bsh.books[0].title)

# post_init
@dataclass
class Book3:
    title: str
    author: str
    desc: str = ''

    def __post_init__(self):
        self.desc = self.desc or "`%s` by %s" % (self.title, self.author)
book4 = Book3("Fareneheit 481", "Bradbury")
print(book4)

# params only for initialisation
@dataclass
class Book4:
    title: str
    author: str
    gen_desc: InitVar[bool] = True
    desc: str = None

    def __post_init__(self, gen_desc: str):
        if gen_desc and self.desc is None:
            self.desc = "`%s` by %s" % (self.title, self.author)
book5 = Book("Fareneheit 481", "Bradbury")
# Book(title='Fareneheit 481', author='Bradbury', desc='`Fareneheit 481` by Bradbury')
book6 = Book("Fareneheit 481", "Bradbury", gen_desc=False)
# Book(title='Fareneheit 481', author='Bradbury', desc=None)

# inheritance
@dataclass
class BaseBook:
    title: Any = None
    author: str = None

@dataclass
class Book5(BaseBook):
    desc: str = None
    title: str = "Unknown"

book7 = Book5
# def __init__(self, title: str="Unknown", author: str=None, desc: str=None)


# alternatives

# namedTuple
from collections import namedtuple 
NamedTupleBook = namedtuple("NamedTupleBook", ["title", "author"])
book = NamedTupleBook("Fahrenheit 451", "Bradbury")
print(book.author)

# tuples and dictionaries
book = ("Fahrenheit 451", "Bradbury")
other = {'title': 'Fahrenheit 451', 'author': 'Bradbury'}

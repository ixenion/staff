from collections import namedtuple

# Create namedtuple type, Point
Point = namedtuple("Point", "x y")
issubclass(Point, tuple)    # True

# Instantiate the new type
point = Point(2, 4)
print(point)    # Point(x=2, y=4)

# Dot notation to access coordinates
print(point.x)
print(point.y)

# Indexing to access coordinates
print(point[0])
print(point[1])

# Named tuples are immutable
#point.x = 100
# Traceback (most recent call last): AttributeError: can't set attribute


# Tho namedtuple is immutable, we can append walue to it:
Person = namedtuple("Person", "name children")
john = Person("John Doe", ["Timmy", "Jimmy"])
# john = Person("John Doe", "Timmy")    # AttributeError: 'str' object has no attribute 'append'
print(john)
john.children.append("Tina")
print(john)


# defaults
# Note that the default values are applied to the rightmost fields.
Developer = namedtuple(
        "Developer",
        "name level language",
        defaults=["Junior", "Python"]
        )
print(Developer("John"))


# The last argument to namedtuple() is module.
# without 'module'
Point1 = namedtuple("Point", "x y")
print(Point1)   # <class '__main__.Point'>
# with 'module'
Point2 = namedtuple("Point", "x y", module="custom")
print(Point2)   # <class 'custom.Point'>


# Creating namedtuple Instances From Iterables
Person = namedtuple("Person", "name age height")
Person._make(["Jane", 25, 1.75])    # Person(name='Jane', age=25, height=1.75)

# Converting namedtuple Instances Into Dictionaries
Person = namedtuple("Person", "name age height")
jane = Person("Jane", 25, 1.75)
jane._asdict()      # {'name': 'Jane', 'age': 25, 'height': 1.75}

# Replacing Fields in Existing namedtuple Instances
Person = namedtuple("Person", "name age height")
jane = Person("Jane", 25, 1.75)
# After Jane's birthday
jane = jane._replace(age=26)
print(jane)


# Exploring Additional namedtuple Attributes
# ._fields and ._field_defaults
Person = namedtuple("Person", "name age height")
ExtendedPerson = namedtuple(
        "ExtendedPerson",
        [*Person._fields, "weight"]
    )
Jane = ExtendedPerson("Jane", 26, 1.75, 67)
print(Jane.weight)
# You can also use ._fields to iterate over the fields and the values in a
# given namedtuple instance using Python’s zip():
Person = namedtuple("Person", "name age height weight")
jane = Person("Jane", 26, 1.75, 67)
for field, value in zip(jane._fields, jane):
    print(field, "->", value)

# OUTPUT
# name -> Jane
# age -> 26
# height -> 1.75
# weight -> 67

# With ._field_defaults, you can introspect namedtuple classes and instances
# to find out what fields provide default values.
Person = namedtuple(
        "Person",
        "name age height weight country",
        defaults=["Canada"]
    )
print(Person._field_defaults)   # {'country': 'Canada'}

# If your namedtuple doesn’t provide default values,
# then .field_defaults holds an empty dictionary:
Person = namedtuple("Person", "name age height weight country")
print(Person._field_defaults)   # {}

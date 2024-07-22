# lesson
# https://www.youtube.com/watch?v=rZY9CJn1y2E&ab_channel=selfedu

class Vector:
    MIN_COORD = 0
    MAX_COORD = 100

    # works with class attributes(min_coord & max_coord)
    # works with classmethod "validate"
    # works with staticmethod "norm2"
    def setCoord(self, x, y):
        # if Vector.validate(x) and Vector.validate(y):
        if self.validate(x) and self.validate(y):
            self.x = x
            self.y = y

    # works with class attributes(MIN_COORD & MAX_COORD), and able modify them
    # works with staticmethod "norm2"
    @classmethod
    def validate(cls, arg):
        if arg >= cls.MIN_COORD and arg <= cls.MAX_COORD:
            return True
        return False

    # works only with given params
    # works both "Vector.norm2(1, 2)"
    # and "v = Vector()" "v.norm2(1, 2)"
    @staticmethod
    def norm2(x, y):
        return x*x + y*y


# USAGE
# $ python3.10
# >>> from 06_statickmethod_decorator.py import Vector
# >>> Vector.validate(5)
# >>> Vector.validate(500)
# >>> Vector.norm2(1, 2)
# BUT this will not work, first need to create class object
# >>> Vector.setCoord(1, 2)
# SO
# >>> v = Vector()
# >>> v.setCoord(1, 2)
# THEN THIS ALSO WORKS
# >>> Vector.setCoord(v, 1, 2)

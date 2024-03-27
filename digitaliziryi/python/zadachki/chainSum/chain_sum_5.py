# whithout IF and
# without TRY-EXCEPT and
# without () and
# result is int object, not chain_sum object

class chain_sum(int):
    def __call__(self, addition = 0):
        return chain_sum(self + addition)

print(1 + chain_sum(5))
print(1 + chain_sum(5)(2))
print(1 + chain_sum(5)(100)(-10))

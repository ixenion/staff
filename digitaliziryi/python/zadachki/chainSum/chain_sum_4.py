# whithout IF and
# without TRY-EXCEPT and
# without ()

class chain_sum:
    def __init__(self, number):
        self._number = number

    def __call__(self, value=0):
        return chain_sum(self._number + value)

    def __str__(self):
        return str(self._number)

print(chain_sum(5))
print(chain_sum(5)(2))
print(chain_sum(5)(100)(-10))

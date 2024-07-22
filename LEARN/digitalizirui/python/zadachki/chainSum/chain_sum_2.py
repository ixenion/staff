# whithout IF

def chain_sum(number):
    result = number
    def wrapper(number2=None):
        nonlocal result
        try:
            number2 = int(number2)
        except TypeError:
            return result
        result += number2
        return wrapper
    return wrapper

print(chain_sum(5)())
print(chain_sum(5)(2)())
print(chain_sum(5)(100)(-10)())

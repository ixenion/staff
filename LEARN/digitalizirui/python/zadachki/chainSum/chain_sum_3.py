# whithout IF and
# without TRY-EXCEPT

def chain_sum(number):
    def wrapper(number2=None):
        def inner():
            wrapper.result += number2
            return wrapper
        logic = {
                type(None) : lambda: wrapper.result,
                int: inner
                }
        return logic[type(number2)]()
    wrapper.result = number
    return wrapper

print(chain_sum(5)())
print(chain_sum(5)(2)())
print(chain_sum(5)(100)(-10)())

import ast

a = {'a':1, 'b':2}
b = str(a)
print(b)
c = ast.literal_eval(b)
print(a==c)

b_empty = '{}'
c = ast.literal_eval(b_empty)
print(c)

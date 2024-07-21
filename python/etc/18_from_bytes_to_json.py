import json

a = {'a':1, 'b':2}
# a = {"a":1, "b":2}
a_str = str(a)
a_bytes = bytes(a_str, 'utf-8')
print(a_bytes)

a_str2 = a_bytes.decode('utf8').replace("'", '"')
# print(a_str2[0])
a_dict = json.loads(a_str2)

print(a_dict['a'])


import repeatedTest_pb2

message = repeatedTest_pb2.SomeWrapper()
submessage = repeatedTest_pb2.SomeInner()
submessage1 = repeatedTest_pb2.SomeInner()

submessage.name = 'John'
submessage.age = 32
submessage1.name = 'Cate'
submessage1.age = 23

# As per the documentation, you aren't able to directly assign to a repeated field.
# In this case, you can call extend to add all of the elements in the list to the field.
message.items.extend([submessage])
message.items.extend([submessage1])

# If you don't want to extend but overwrite it completely, you can do:
# message.items[:] = ['John', 32]
# This approach will also work to clear the field entirely:
# del message.items[:]

# iterate through 'repeated'
print(message.items[0])

message.Clear()
print(f"cleared. {message}")


print(message.items)

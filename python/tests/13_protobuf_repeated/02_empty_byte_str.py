import repeatedTest_pb2

message = repeatedTest_pb2.SomeWrapper()
submessage = repeatedTest_pb2.SomeInner()
submessage1 = repeatedTest_pb2.SomeInner()

# check that empty byte string returns zero at ParseFromString
msg = bytes('', 'utf8')
parsed = message.ParseFromString(msg)
print(parsed)

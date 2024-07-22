import addressbook_pb2
message = addressbook_pb2.Person()
message.id = 1234
message.name = "John Doe"
message.email = "jdoe@example.com"
phone = message.phones.add()
phone.number = "555-4321"
# non existing fields rises error
# phone.number2 = "555-4321"
phone.type = addressbook_pb2.Person.HOME


directive_args = {"enable": "1", "delay": "3"}
message.directive_args.update(directive_args)



print(message)
message.Clear()
print("Person2:\n", message)

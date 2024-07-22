from uuid import uuid4
import time
import protocol_pb2


# message = protocol_pb2.Directive()
message = protocol_pb2.Protocol()

message.version = '123'
message.timestamp = str(time.time())

message.directive.msg_id = str(uuid4())
message.directive.directive = 'MODEM_SEND_SMS'
print(message)

# [working] map
message.directive.directive_args['target_imsi'] = '25007ХХХХХХХХХХ'
message.directive.directive_args['text'] = 'Penguins are so cute'
message.directive.directive_args['repeat'] = '1'
print(message)
print(message.directive.directive_args)



# [not working] load dict
# directive_args = {}
# directive_args['target_imsi'] = '25007ХХХХХХХХХХ'
# directive_args['text'] = 'Penguins are so cute'
# directive_args['repeat'] = '1'
# message.directive_args = directive_args
# print(message)
# print(message.directive_args)


# [working] load dict 2
# directive_args = {}
# directive_args['target_imsi'] = '25007ХХХХХХХХХХ'
# directive_args['text'] = 'Penguins are so cute'
# directive_args['repeat'] = '1'
# message.directive_args.update(directive_args)
# print(message)
# print(message.directive_args)

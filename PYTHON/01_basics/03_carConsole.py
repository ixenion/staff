print('Type "help" for ... help')
started = False
while True:
    command = input('> ')
    if command.upper() == "HELP":
        print('''
start - to start car
stop  - to stop car
exit  - to quit
            ''')
    elif command.upper() == "START":
        if not started:
            print('Car started ...')
            started = True
        else:
            print('You crazzzy ...')
    elif command.upper() == "STOP":
        if started:
            print('Car stopped ...')
            started = False
        else:
            print('Car not started.')
    elif command.upper() == "EXIT":
        break
    else:
        print('Unknown command. Type "help" ')




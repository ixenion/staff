from python_shell import Shell
from python_shell.util.streaming import decode_stream


command = Shell.rm('link.txt')
print(command.return_code)
command = Shell.ln('-s','orig.txt','link.txt')
print(command.return_code)




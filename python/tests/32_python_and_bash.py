import os
from subprocess import run, STDOUT, PIPE, check_output, call, Popen


service = 'cron'

# stdout and error code, NO PIPE
# cmd = f"sudo systemctl status {service}"
cmd = ['sh', '-c', f'systemctl status cron | grep PID']
cmd2 = f"grep PID"

# shell = run(cmd, stdout=PIPE, stderr=STDOUT, text=True, shell=True)

# return_code = shell.returncode
# output = shell.stdout
# print(return_code)
# print(output)


# PIPE, only output
cmd = 'systemctl status astcv2 | grep PID'
# result = check_output(cmd, shell=True, stderr=STDOUT).decode('utf-8')
# result = check_output(cmd, shell=True, stderr=STDOUT)
result = check_output(cmd, shell=True, stderr=STDOUT)
# print(f'stdout:\n{result}')
# print(type(result))


# PIPE, error in format of string
cmd = ['sh', '-c', 'systemctl status astcv2 | grep PID']
res = Popen(cmd, stdout=PIPE, stderr=PIPE)
out, err = [val.decode('utf-8') for val in res.communicate()]
print(f'OUT: {out}')
print(f'ERR: {err}')



# PIPE, error in format of code, cant redirrect stdout
cmd = 'systemctl status astcv2 | grep PID'
# result = os.system(cmd)
# print(result)

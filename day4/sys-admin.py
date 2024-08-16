import os
import subprocess

# Try ls with os and subprocess
# os.system("ls")
# subprocess.run(["ls"])
# subprocess.run(["ls","-l"])

# Try uname
# command="uname"
# commandArgument="-a"
# print(f'Gathering system information with command: {command} {commandArgument}')
# subprocess.run([command,commandArgument])

# Try ps
command="ps"
commandArgument="-x"
print(f'Gathering active process information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])

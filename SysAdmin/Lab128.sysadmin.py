import os
import subprocess
print()
print("--------------------")
print()
os.system("ls")
print()
subprocess.run(["ls"])
print()
print("--------------------")
print()
subprocess.run(["ls","-l"])
print()
subprocess.run(["ls","-l","sysadmin.py"])
print()
print("--------------------")
print()
command="uname"
commandArgument="-a"
print(f'Gathering system information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])
print()
print("--------------------")
print()
command="ps"
commandArgument="-x"
print(f'Gathering active process information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])
print()
print("--------------------")
print()
import os
import subprocess
from time import sleep

counter = 0
def fib(n):
		global counter
		counter += 1
		print(counter)
		if n in [0, 1]:
				return 1
		return fib(n - 1) + fib(n - 2)

def main():
	with open('status', 'w') as f:
		f.write('processing')
	cmd = 'python3 l_chika.py'
	subprocess.Popen(cmd.split())
	fib(24)
	with open('status', 'w') as f:
		f.write('red')
	sleep(3)
	with open('status', 'w') as f:
		f.write('stop')
	
if __name__=='__main__':
	try:
		main()
	except KeyboardInterrupt:
		with open('status', 'w') as f:
			f.write('stop')
		exit(0)

import RPi.GPIO as GPIO
from time import sleep

# Lチカのセットアップ
color_list = {'red': 4, 'yellow':17, 'green':27}
GPIO.setmode(GPIO.BCM)
GPIO.setup(color_list['red'], GPIO.OUT)
GPIO.setup(color_list['yellow'], GPIO.OUT)
GPIO.setup(color_list['green'], GPIO.OUT)
GPIO.output(color_list['red'], False)
GPIO.output(color_list['yellow'], False)
GPIO.output(color_list['green'], False)

# Lチカの状態遷移用 0→消灯 1→点灯

def led(status):
	if status == 'stop':
		GPIO.cleanup()
		exit(0)
	if status == 'black':
		return
	elif status == 'processing':
		GPIO.output(color_list['red'], True)
		sleep(0.05)
		GPIO.output(color_list['red'], False)
		GPIO.output(color_list['yellow'], True)
		sleep(0.05)
		GPIO.output(color_list['yellow'], False)
		GPIO.output(color_list['green'], True)
		sleep(0.05)
		GPIO.output(color_list['green'], False)
	elif status == 'red':
		GPIO.output(color_list['red'], True)
		sleep(0.05)
		GPIO.output(color_list['red'], False)
		sleep(0.05)
	elif status == 'yellow':
		GPIO.output(color_list['yellow'], True)
		sleep(0.05)
		GPIO.output(color_list['yellow'], False)
		sleep(0.05)
	elif status == 'green':
		GPIO.output(color_list['green'], True)
		sleep(0.05)
		GPIO.output(color_list['green'], False)
		sleep(0.05)
		
if __name__=='__main__':
	while True:
		try:
			with open('status','r') as status_file:
				status = status_file.read()
			led(status)
		except KeyboardInterrupt:
			GPIO.cleanup()
			exit(0)
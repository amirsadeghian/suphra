import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)
#GPIO.setwarnings(False)


#set GPIO direction (IN / OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.output(23, True)    
time.sleep(10)    
GPIO.output(23, False)    

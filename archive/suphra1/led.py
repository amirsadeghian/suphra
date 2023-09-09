import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(17,GPIO.OUT) ##LED1
GPIO.setup(27,GPIO.OUT) ##LED2

def blink(led,rep,speed):
   ## for i in range(0,rep):
    while True:
        print str(led)+ "LED ON"
        GPIO.output(led,GPIO.HIGH)
        time.sleep(speed)
        print str(led)+ "LED OFF"
        GPIO.output(led,GPIO.LOW)
        time.sleep(speed)

def blink2(led,rep,speed):
   ## for i in range(0,rep):
    while True:
        print str(led)+ "LED ON"
        GPIO.output(led,GPIO.HIGH)
        time.sleep(speed)
        print str(led)+ "LED OFF"
        GPIO.output(led,GPIO.LOW)
        time.sleep(speed)


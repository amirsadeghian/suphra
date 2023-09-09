import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(18,GPIO.OUT) ##ENGINE BACKWARD
GPIO.setup(23,GPIO.OUT) ##ENGINE FORWARD
GPIO.setup(24,GPIO.OUT) ##STEER LEFT
GPIO.setup(25,GPIO.OUT) ##STEER RIGHT

def forward(delay):
    GPIO.output(18,GPIO.LOW)
    GPIO.output(23,GPIO.HIGH)
    GPIO.output(24,GPIO.LOW)
    GPIO.output(25,GPIO.LOW)
    time.sleep(delay)

def backward(delay): 
    GPIO.output(18,GPIO.HIGH)
    GPIO.output(23,GPIO.LOW)
    GPIO.output(24,GPIO.LOW)
    GPIO.output(25,GPIO.LOW)
    time.sleep(delay)

def left(delay):
    GPIO.output(18,GPIO.LOW)
    GPIO.output(23,GPIO.LOW)
    GPIO.output(24,GPIO.HIGH)
    GPIO.output(25,GPIO.LOW)
    time.sleep(delay)

def right(delay):
    GPIO.output(18,GPIO.LOW)
    GPIO.output(23,GPIO.LOW)
    GPIO.output(24,GPIO.LOW)
    GPIO.output(25,GPIO.HIGH)
    time.sleep(delay)

def stop():
    GPIO.output(18,GPIO.LOW)
    GPIO.output(23,GPIO.LOW)
    GPIO.output(24,GPIO.LOW)
    GPIO.output(25,GPIO.LOW)


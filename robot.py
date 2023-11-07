
#!/usr/bin/env python3
#Libraries
import RPi.GPIO as GPIO
import time
import subprocess
from gpiozero import PWMOutputDevice
from pygame import display, joystick, event
from pygame import QUIT, JOYAXISMOTION, JOYBALLMOTION, JOYHATMOTION, JOYBUTTONUP, JOYBUTTONDOWN

 
#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)


#set GPIO Pins
GPIO_CENTER_SENSOR_TRIGGER = 23
GPIO_CENTER_SENSOR_ECHO = 24
GPIO_LEFT_SENSOR_TRIGGER = 4
GPIO_LEFT_SENSOR_ECHO = 25
GPIO_RIGHT_SENSOR_TRIGGER = 17
GPIO_RIGHT_SENSOR_ECHO = 16
GPIO_MOTOR_FORWARD = 13
GPIO_MOTOR_BACKWARD = 26
GPIO_MOTOR_PWM = 12
GPIO_STEER_LEFT= 6
GPIO_STEER_RIGHT= 5

#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_MOTOR_FORWARD, GPIO.OUT)
GPIO.setup(GPIO_MOTOR_BACKWARD, GPIO.OUT)
GPIO.setup(GPIO_MOTOR_PWM, GPIO.OUT)
GPIO.setup(GPIO_STEER_LEFT, GPIO.OUT)
GPIO.setup(GPIO_STEER_RIGHT, GPIO.OUT)
GPIO.setup(GPIO_CENTER_SENSOR_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_CENTER_SENSOR_ECHO, GPIO.IN)
GPIO.setup(GPIO_LEFT_SENSOR_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_LEFT_SENSOR_ECHO, GPIO.IN)
GPIO.setup(GPIO_RIGHT_SENSOR_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_RIGHT_SENSOR_ECHO, GPIO.IN)

#Reset Pins
GPIO.output(GPIO_MOTOR_FORWARD, False)
GPIO.output(GPIO_MOTOR_BACKWARD, False)
GPIO.output(GPIO_STEER_LEFT, False)
GPIO.output(GPIO_STEER_RIGHT, False)
GPIO.output(GPIO_FRONT_SENSOR_TRIGGER, False)
GPIO.output(GPIO_LEFT_SENSOR_TRIGGER, False)
GPIO.output(GPIO_RIGHT_SENSOR_TRIGGER, False)
#GPIO.cleanup()


#Global Variables
isAuto = False
autoForwardSpeed = 50
autoBackwardSpeed = 60


#Set PWM Setting
motorPWM = GPIO.PWM(GPIO_MOTOR_PWM,100)
motorPWM.start(autoForwardSpeed)

#Run Camera
#subprocess.run('python3 stream.py',shell=True)

#joystick setting
h = {
    (0,0):  'c',
    (1,0):  'E', (1,1):   'NE', (0,1):  'N', (-1,1): 'NW',
    (-1,0): 'W', (-1,-1): 'SW', (0,-1): 'S', (1,-1): 'SE'
}
P = 2 # precision

#calculate the distance
def distance():
    # set Trigger to HIGH
    GPIO.output(GPIO_FRONT_SENSOR_TRIGGER, True)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)    
    GPIO.output(GPIO_FRONT_SENSOR_TRIGGER, False)
 
    StartTime = time.time()
    StopTime = time.time()
 
    # save StartTime
    while GPIO.input(GPIO_FRONT_SENSOR_ECHO) == 0:
        StartTime = time.time()
 
    # save time of arrival
    while GPIO.input(GPIO_FRONT_SENSOR_ECHO) == 1:
        StopTime = time.time()
 
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2 
    return distance

def autonomous():
    while True:
        dist = distance()
        print(dist)
        if dist > 35:
            print('Forward')
            GPIO.output(GPIO_MOTOR_BACKWARD, False)
            GPIO.output(GPIO_MOTOR_FORWARD, True)
        else:
            print('Backward')
            GPIO.output(GPIO_MOTOR_FORWARD, False)
            GPIO.output(GPIO_MOTOR_BACKWARD, True)
            GPIO.output(GPIO_STEER_RIGHT, True)
            time.sleep(0.01)
            GPIO.output(GPIO_STEER_RIGHT, False)
            GPIO.output(GPIO_MOTOR_BACKWARD, False)

def main(argv=[]):
    global isAuto
    display.init()
    joystick.init()

    if len(argv) > 1:
        for sz in argv[1:]:
            try:
                joystick.Joystick(int(sz)).init()
            except:
                pass
    else:
        for i in range(joystick.get_count()):
            joystick.Joystick(i).init()

    e = event.wait()
    while isAuto:
        print('Auto')
        autonomous()
    while e.type != QUIT:
        print('A')
        dist = distance()
        if e.type == JOYAXISMOTION:   
            print('axis', e.axis, round(e.value, P))
        elif e.type == JOYBALLMOTION: 
            print('ball', e.ball, round(e.rel, P))
        elif e.type == JOYHATMOTION:  
            print('hat', e.hat, h[e.value])
        elif e.type == JOYBUTTONUP:   
            print('button', e.button, 'up')
        elif e.type == JOYBUTTONDOWN: 
            print('button', e.button, 'down')
        try:
            e = event.wait()
        except KeyboardInterrupt:
            break
            
        if e.type == JOYBUTTONUP and e.button==9:
            #Autonomous
            isAuto = not isAuto
            while isAuto:
                print('Auto')
                autonomous()
        


if __name__ == "__main__":
    from sys import argv
    #main(argv)
    autonomous()

import RPi.GPIO as GPIO
import time
import threading
from threading import Thread
from multiprocessing import Process

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

import engine
import led
#if __name__=="__main__":
    #Thread(target = backward(2)).start()
    #Thread(target = right(1)).start()
    #Thread(target = engine.forward(0.3)).start()
    #Thread(target = left(1)).start()
    #Thread(target = backward(1)).start()   
    #p1 = Process(target=led.blink(27,10,0.6)).start()
    #p2 = Process(target=led.blink2(17,10,0.5)).start()
    #p1.join()
    #p2.join()

#while 1:
#led.blink(27,1,4)
#led.blink(17,1,0.1)
engine.forward(0.3)
GPIO.cleanup()

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
#GPIO 22
pin = 15


def on():
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, 1)

def off():
        GPIO.setup(pin, GPIO.IN)


def activate():
        on()
        time.sleep(5)
        off()
        time.sleep(1)

#activate() #For manual actuation


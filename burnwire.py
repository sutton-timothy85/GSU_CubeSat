import RPi.GPIO as GPIO
import time
#GPIO 22
pin = 36
#GPIO.setmode(GPIO.BOARD)

def on():
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, 1)

def off():
        GPIO.setup(pin, GPIO.IN)


def activate():
        on()
        time.sleep(10)
        off()
        time.sleep(1)
#activate() #For manual actuation


import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

pin = 18


def on():
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, 1)

def off():
        GPIO.setup(pin, GPIO.IN)


while (1):
        on()
        time.sleep(1)
        off()
        time.sleep(1)


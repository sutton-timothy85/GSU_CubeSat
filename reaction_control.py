import RPi.GPIO as GPIO  # Imports the standard Raspberry Pi GPIO library
from time import sleep   # Imports sleep (aka wait or pause) into the program

def cw(servo):

    servo.ChangeDutyCycle(0.9)
    sleep(5)
    servo.stop(0)

def ccw(servo):
    servo.ChangeDutyCycle(40)
    sleep(5)
    servo.stop(0)



# GPIO.setmode(GPIO.BOARD) # Sets the pin numbering system to use the physical layout

# GPIO.setup(18, GPIO.OUT)
# GPIO.setup(13, GPIO.OUT) 

# X_servo = GPIO.PWM(18, 50)
# Z_servo = GPIO.PWM(13, 50)

# X_servo.start(0)
# Z_servo.start(0)
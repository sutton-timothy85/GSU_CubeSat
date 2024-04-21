# Set up libraries and overall settings
import RPi.GPIO as GPIO  # Imports the standard Raspberry Pi GPIO library
from time import sleep   # Imports sleep (aka wait or pause) into the program
GPIO.setmode(GPIO.BCM) # Sets the pin numbering system to use the physical layout

# Set up pin 11 for PWM
GPIO.setup(18, GPIO.OUT)  # Sets up pin 11 to an output (instead of an input)
GPIO.setup(13, GPIO.OUT)  # Sets up pin 11 to an output (instead of an input)
p1 = GPIO.PWM(13, 50)     # Sets up pin 11 as a PWM pin
p1.start(0)               # Starts running PWM on the pin an sets it to 0
p1.ChangeDutyCycle(0.9)     # Changes the pulse width to 3 (so moves the servo)


p2 = GPIO.PWM(18, 50)     # Sets up pin 11 as a PWM pin
p2.start(0)               # Starts running PWM on the pin an sets it to 0
p2.ChangeDutyCycle(17.5)     # Changes the pulse width to 3 (so moves the servo)
sleep(18)   

# Clean up everything

p1.stop()                 # At the end of the program, stop the PWM
p2.stop() 
GPIO.cleanup()           # Resets the GPIO pins back to defaults
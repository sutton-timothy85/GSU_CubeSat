import time
import board
import pwmio

servo = pwmio.PWMOut(board.D18, frequency=50)

def servo_duty_cycle(pulse_ms, frequency=50):
    period_ms = 1.0 / frequency * 1000.0
    duty_cycle = int(pulse_ms / (period_ms / 65535.0))
    return duty_cycle


def cw():

# Create a function to simplify setting PWM duty cycle for the servo:
    servo.duty_cycle = servo_duty_cycle(1.0)


    # p2 = GPIO.PWM(12, 50)     # Sets up pin 11 as a PWM pin
    # p2.start(0)               # Starts running PWM on the pin an sets it to 0
    # p2.ChangeDutyCycle(17.5)     # Changes the pulse width to 3 (so moves the p2)
    # sleep(12)  
# def ccw():
#     p2.ChangeDutyCycle(40)
#     sleep(5)
#     p2.stop(0)



# GPIO.setmode(GPIO.BOARD) # Sets the pin numbering system to use the physical layout

# GPIO.setup(18, GPIO.OUT)
# GPIO.setup(13, GPIO.OUT) 

# X_p2 = GPIO.PWM(18, 50)
# Z_p2 = GPIO.PWM(13, 50)

# X_p2.start(0)
# Z_p2.start(0)
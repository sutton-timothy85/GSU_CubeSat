import time
import board
import burnwire
import reaction_control as RC
import adafruit_mpl3115a2
import adafruit_icm20x
import adafruit_mcp9808
import RPi.GPIO as GPIO  # Imports the standard Raspberry Pi GPIO library
from time import sleep   # Imports sleep (aka wait or pause) into the program
from picamera2 import Picamera2, Preview
from digi.xbee.devices import XBeeDevice

#GPIO.setmode(GPIO.BOARD)

PORT = "/dev/ttyUSB0"
BAUD_RATE = 9600
xbee = XBeeDevice(PORT,BAUD_RATE)
xbee.open()
xbee.set_sync_ops_timeout(10)

GPIO.setup(18, GPIO.OUT)
GPIO.setup(13, GPIO.OUT) 

X_servo = GPIO.PWM(18, 50)
Z_servo = GPIO.PWM(13, 50)

X_servo.start(0)
Z_servo.start(0)

activated = False



i2c = board.I2C()
#picam = Picamera2()
altimeter = adafruit_mpl3115a2.MPL3115A2(i2c)
imu = adafruit_icm20x.ICM20948(i2c)
temp = adafruit_mcp9808.MCP9808(i2c)
#picam.start()



#Set parameters for operation

Norm_AT = [0, 0, 0] #Placeholders
altimeter.sealevel_pressure = 1022.5

def reaction_control():

    #For each command run reaction control sequence for 10 seconds
    t_end = time.time() + 0
    while time.time() < t_end:
        current_atitude = list(imu.gyro)
        X = float(current_atitude[0])
        Y = float(current_atitude[1])
        Z = float(current_atitude[2])  # Extracting the third value (index 2) and converting to float
    
        

def receive(xbee_message):

    address = xbee_message.remote_device.get_64bit_addr()
    data = xbee_message.data.decode("utf8")
    print("Received data from %s: %s" % (address, data))
    return data

def system_health():

    temp_RW = temp.temperature

    
def collect_data():
    temp_RW = temp.temperature
    acceleration = imu.acceleration
    atitude = imu.gyro
    altitude = altimeter.altitude

    data = str([temp_RW, acceleration, atitude, altitude])
    print(data)
    deliver(data)


def capture_image():
    f = 0 #comented to test other systems
    #picam.capture_file("image")
    #code for sending image here

def deliver(data):

    xbee.send_data_broadcast(data)

def activate_burnwire():

    burnwire.activate()
    activated == True

def main():
    deliver("System Running!")
    try:
        #Xbee listen for message
        while True:
            message = xbee.read_data()
            if message is not None:
                    message = message.data.decode()
                    print(message)
                    if (message == "collect data"):
                        deliver("Collecting Data")
                        collect_data()
                        capture_image()
                    elif (message == "burn wire"):
                        if (activated == True):
                            #Notify of previous actuation. confirm choice
                            bw_warning = "Burn wire already actuated"
                            deliver(bw_warning)
                        else:
                            activate_burnwire()
                    elif message == "status":
                        system_health()
                    elif message == "reaction control":
                        RC.reaction_contol()
                    else:
                        UE_warning = "Unknown Command"
                        deliver(UE_warning)
    except KeyboardInterrupt:
        #picam.close()
        xbee.close()
        print("Shutting Down")

if __name__ == '__main__':
    main()
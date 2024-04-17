import time
import board
import burnwire
import reaction_control as RC
import adafruit_mpl3115a2
import adafruit_icm20x
import adafruit_mcp9808
from picamera2 import Picamera2, Preview
from digi.xbee.devices import XBeeDevice
activated = False

PORT = "/dev/ttyUSB0"
BAUD_RATE = 9600
xbee = XBeeDevice(PORT,BAUD_RATE)
xbee.open()
i2c = board.I2C()
picam = Picamera2()
altimeter = adafruit_mpl3115a2.MPL3115A2(i2c)
imu = adafruit_icm20x.ICM20948(i2c)
temp = adafruit_mcp9808.MCP9808(i2c)
picam.start()

#Set parameters for operation
Norm_AT = [0, 0, 0] #Placeholders
altimeter.sealevel_pressure = 1022.5

def reaction_control():

    #For each command run reaction control sequence for 10 seconds
    t_end = time.time() + 0
    while time.time() < t_end:
        current_atitude = list(imu.gyro)
        Z = float(current_atitude[2])  # Extracting the third value (index 2) and converting to float
        print(Z)
    
    


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

    data = [temp_RW, acceleration, atitude, altitude]
    deliver(data)
    print(str(data))

def capture_image():
    picam.capture_file("image")
    #code for sending image here

def deliver(data):

    xbee.send_data_broadcast(data)

def activate_burnwire():

    burnwire.activate()
    activated == True

def main():

    try:
        #Xbee listen for message
        message = receive()

        if (message == "collect data"):
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
        picam.close()
        xbee.close()
        print("Shutting Down")

collect_data()
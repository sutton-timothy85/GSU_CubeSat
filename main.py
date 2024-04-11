import time
import board
import burnwire
import adafruit_mpl3115a2
import adafruit_icm20x
import adafruit_mcp9808

activated = False

i2c = board.I2C()

altimeter = adafruit_mpl3115a2.MPL3115A2(i2c)
imu = adafruit_icm20x.ICM20948(i2c)
temp = adafruit_mcp9808.MCP9808(i2c)


altimeter.sealevel_pressure = 1022.5

def collect_data():
    temp_RW = temp.temperature
    acceleration = imu.acceleration
    atitude = imu.gyro
    altitude = altimeter.altitude

    data = [temp_RW, acceleration, atitude, altitude]
    deliver(data)




def deliver(data):
    xbee = 0
    #send data to xbee

    ##if image file exisit:
    #Perform undetermined logic

def burnwire():

    
    burnwire.activate()
    activated == True

def main():

    try:
        #Xbee listen for message
        message = "placeholder"




    except KeyboardInterrupt:
        print("Shutting Down")

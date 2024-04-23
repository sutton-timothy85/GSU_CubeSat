import time
import board
import adafruit_mpl3115a2
import adafruit_icm20x
import adafruit_mcp9808


i2c = board.I2C()
altimeter = adafruit_mpl3115a2.MPL3115A2(i2c)
imu = adafruit_icm20x.ICM20948(i2c)
temp = adafruit_mcp9808.MCP9808(i2c)

altimeter.sealevel_pressure = 1022.5
temp_RW = temp.temperature
acceleration = imu.acceleration
atitude = imu.gyro
mag = imu.magnetic
altitude = altimeter.altitude


data = [temp_RW, acceleration, atitude, altitude]


current_atitude = list(imu.gyro)
Z = float(current_atitude[2])  # Extracting the third value (index 2) and converting to float
print(Z)
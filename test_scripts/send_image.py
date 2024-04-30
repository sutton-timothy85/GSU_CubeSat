import serial
import time
from digi.xbee.devices import XBeeDevice

PORT = "/dev/ttyUSB0"
BAUD_RATE = 57600
xbee = XBeeDevice(PORT,BAUD_RATE)
xbee.open()
xbee.set_sync_ops_timeout(20)

# Read the picture
with open('test-python.jpg', 'rb') as f:
    picture_data = f.read()

# Chunk size (adjust according to your requirements)
chunk_size = 100  # Example chunk size

# Transmit chunks
for i in range(0, len(picture_data), chunk_size):
    chunk = picture_data[i:i + chunk_size]
    xbee.send_data_broadcast(chunk)
    time.sleep(0.2)  # Add a delay between transmissions

# Close serial connection
xbee.close()

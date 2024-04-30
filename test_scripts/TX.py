import time
from digi.xbee.devices import XBeeDevice
import os
import math
BAUD_RATE = 57600
PORT = "/dev/ttyUSB0"
xbee = XBeeDevice(PORT, BAUD_RATE)
xbee.open()
xbee.set_sync_ops_timeout(10)

image_filename = 'test-python.jpg'
chunk_size = 100  # Example chunk size
def send_image(image_filename, chunk_size):
    # Read the picture
    with open(image_filename, 'rb') as f:
        picture_data = f.read()
    image_size = os.path.getsize(image_filename) 
    total_chunks = math.ceil(image_size/chunk_size)
    print("image: " + str(total_chunks))
    xbee.send_data_broadcast("image: " + str(total_chunks))
    time.sleep(2)
    # Transmit chunks
    for i in range(0, len(picture_data), chunk_size):
        chunk = picture_data[i:i + chunk_size]
        xbee.send_data_broadcast(chunk)
        print("Chunk Sent")
        time.sleep(0.1)  # Optional: add a delay between transmissions


send_image(image_filename, chunk_size)

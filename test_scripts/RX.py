from digi.xbee.devices import XBeeDevice
import time
#hi
# XBee settings
PORT = "COM5"  # Change this to your serial port
BAUD_RATE = 115200
xbee = XBeeDevice(PORT, BAUD_RATE)
xbee.open()
xbee.set_sync_ops_timeout(10)



def receive_image(received_filename):
    # Open the file in append mode
    with open(received_filename, 'wb') as f:
        while True:
            xbee_message = xbee.read_data()
            if xbee_message is not None:
                chunk = xbee_message.data
                f.write(chunk)
            else:
                break

# Example usage
if __name__ == "__main__":
    received_filename = "received_image.jpg"
    receive_image(received_filename)

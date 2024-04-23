from digi.xbee.devices import XBeeDevice
import time

# XBee settings
PORT = "/dev/ttyUSB0"
xbee = XBeeDevice(PORT, BAUD_RATE)
xbee.open()
xbee.set_sync_ops_timeout(10)

# Function to send image
def send_image(xbee_device, image_path):
    # Read image file
    with open(image_path, 'rb') as f:
        image_data = f.read()

    # Send image data
    xbee_device.send_data_broadcast(image_data)

    print("Image sent successfully!")

# Main function
if __name__ == "__main__":
    try:


        image_path = "test-python.jpg"  # Change this to your image path
        send_image(xbee, image_path)

    except Exception as e:
        print("Error:", e)

    finally:
        if xbee is not None and xbee.is_open():
            xbee.close()

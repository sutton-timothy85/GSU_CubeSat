import time
from digi.xbee.devices import XBeeDevice

BAUD_RATE = 9600
PORT = "/dev/ttyUSB0"
xbee = XBeeDevice(PORT, BAUD_RATE)
xbee.open()
xbee.set_sync_ops_timeout(10)

def send_image(image_filename, chunk_size):
    # Read the picture
    with open(image_filename, 'rb') as f:
        picture_data = f.read()

    # Transmit chunks
    for i in range(0, len(picture_data), chunk_size):
        chunk = picture_data[i:i + chunk_size]
        xbee.send_data_broadcast(chunk)
        print("Chunk Sent")
        time.sleep(1)  # Optional: add a delay between transmissions

# Example usage
if __name__ == "__main__":
    image_filename = 'test-python.jpg'
    chunk_size = 100  # Example chunk size
    send_image(image_filename, chunk_size)

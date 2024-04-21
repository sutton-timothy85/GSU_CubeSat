from digi.xbee.devices import XBeeDevice

# TODO: Replace with the serial port where your local module is connected to.
PORT = "/dev/ttyUSB0"
# TODO: Replace with the baud rate of your local module.
BAUD_RATE = 9600

def main():
    print(" +-----------------------------------------+")
    print(" | XBee Python Library Receive Data Sample |")
    print(" +-----------------------------------------+\n")

    device = XBeeDevice(PORT, BAUD_RATE)

    try:
        device.open()

        print("Waiting for data...\n")
        
        while True:
            xbee_message = device.read_data()
            if xbee_message is not None:
                received_message = xbee_message.data.decode()
                print(received_message)
                if received_message == 'message':
                    print("success")

    finally:
        if device is not None and device.is_open():
            device.close()

if __name__ == '__main__':
    main()

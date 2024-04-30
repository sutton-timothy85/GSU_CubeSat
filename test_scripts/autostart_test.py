import time

from digi.xbee.devices import XBeeDevice

PORT = "/dev/ttyUSB0"
BAUD_RATE = 57600
xbee = XBeeDevice(PORT,BAUD_RATE)
xbee.open()
xbee.set_sync_ops_timeout(20)


def deliver(data):

    xbee.send_data_broadcast(data)

t_end = time.time() + 60
while time.time() < t_end:
    deliver("Running!")
    time.sleep(5)


print("Closing Script")
deliver("DIe")
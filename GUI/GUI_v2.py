import tkinter as tk
from digi.xbee.devices import XBeeDevice
import threading
from datetime import datetime
import time
from PIL import Image, ImageTk

PORT = "COM18"
BAUD_RATE = 57600
xbee = XBeeDevice(PORT, BAUD_RATE)
xbee.open()
xbee.set_sync_ops_timeout(10)



def deliver(data):
    xbee.send_data_broadcast(data)

def update_text(text):
    text_display.config(state=tk.NORMAL)
    text_display.insert(tk.END, text + "\n")  # Append new text with a newline character
    text_display.config(state=tk.DISABLED)

def read_xbee_data():
    while True:
        message = xbee.read_data()
        if message:
            stamp = (datetime.now().strftime('%H_%M_%S.%f')[:-3])
            filename = f'{stamp}.jpg'
            data = message.data
            update_text("Received message: {}".format(message.data.decode()))
                    
        

def collect_data():
    update_text("Command Sent: Collect Data")
    deliver("collect data")

def burn_wire():
    update_text("Command Sent: Burn Wire")
    deliver("burn wire")

def reaction_control():
    update_text("Command Sent: Reaction Control Mode")
    deliver("reaction control")

def system_check():
    update_text("Command Sent: Requesting System Status")
    deliver("check")

def reboot():
    update_text("Command Sent: Rebooting Pi")
    deliver("reboot")

def death():
    update_text("Command Sent: Killing CubeSat Script")
    deliver("shutdown")

def servo_test():
    update_text("Command Sent: Testing Servos")
    deliver("test servo")

# Create main window
root = tk.Tk()
root.title("CubeSat Ground Station GUI")

# Load logo image
logo_image = Image.open("GUI_pic.png")  # Change "logo.png" to the path of your logo image
logo_image = logo_image.resize((500, 500))
logo_photo = ImageTk.PhotoImage(logo_image)

# Create label for logo
logo_label = tk.Label(root, image=logo_photo)
logo_label.pack(side=tk.RIGHT, padx=2, pady=2)

# Create frame for buttons
button_frame = tk.Frame(root)
button_frame.pack(side=tk.BOTTOM, padx=10, pady=10)

# Create buttons
button1 = tk.Button(button_frame, text="Collect Data", command=collect_data, width=10, height=2)
button1.pack(side=tk.LEFT, padx=5, pady=5)

button2 = tk.Button(button_frame, text= "Burn wire", command=burn_wire, width=10, height=2)
button2.pack(side=tk.LEFT, padx=5, pady=5)

button3 = tk.Button(button_frame, text="Reaction Control", command=reaction_control, width=20, height=2)
button3.pack(side=tk.LEFT, padx=5, pady=5)

button4 = tk.Button(button_frame, text="System Check", command=system_check, width=20, height=2)
button4.pack(side=tk.LEFT, padx=5, pady=5)

button5 = tk.Button(button_frame, text="Reboot", command=reboot, width=10, height=2)
button5.pack(side=tk.LEFT, padx=5, pady=5)

button6 = tk.Button(button_frame, text="Test Servos", command=servo_test, width=10, height=2)
button6.pack(side=tk.LEFT, padx=5, pady=5)

button7 = tk.Button(button_frame, text="Shutdown", command=death, width=10, height=2, bg="red")
button7.pack(side=tk.LEFT, padx=5, pady=5)

# Create text display
text_display = tk.Text(root, height=40, width=100)
text_display.pack(side=tk.LEFT, padx=10, pady=10)
text_display.config(state=tk.DISABLED)

xbee_thread = threading.Thread(target=read_xbee_data, daemon=True)
xbee_thread.start()



root.mainloop()

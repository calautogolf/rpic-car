try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO, try running with 'sudo'")

import signal
import sys
import time

# Cleanup GPIO on Ctrl-C (SIGINT)
def signal_handler(signal, frame):
    print("\nReceived SIGINT, cleaning up GPIO and exiting...")
    GPIO.cleanup()
    sys.exit(0)

def pin_toggle(channel):
    GPIO.output(channel, not GPIO.input(channel))

def pin_high(channel):
    if not GPIO.input(channel):
        GPIO.output(channel, GPIO.HIGH)

def pin_low(channel):
    if GPIO.input(channel):
        GPIO.output(channel, GPIO.LOW)

# Register SIGINT handler for GPIO cleanup
signal.signal(signal.SIGINT, signal_handler)
# print("SIGINT registered")

# Initialize GPIO
GPIO.setmode(GPIO.BOARD)
# print("GPIO mode set")

# Set output pins for each controller direction
controller_chan_list = [35, 36, 37, 38]
GPIO.setup(controller_chan_list, GPIO.OUT, initial=GPIO.LOW)
# print("Output pins set")

# Pin demo
while True:
    for chan in controller_chan_list:
        pin_toggle(chan)
        time.sleep(1)
        pin_toggle(chan)

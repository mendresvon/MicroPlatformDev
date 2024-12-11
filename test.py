"""
For thonny editor
For testing if all LEDS (RYG) function as expected 
"""

import machine
import utime

# Define pins for the first set of LEDs
red_led1 = machine.Pin(2, machine.Pin.OUT)
yellow_led1 = machine.Pin(3, machine.Pin.OUT)
green_led1 = machine.Pin(4, machine.Pin.OUT)

# Define pins for the second set of LEDs
red_led2 = machine.Pin(6, machine.Pin.OUT)
yellow_led2 = machine.Pin(7, machine.Pin.OUT)
green_led2 = machine.Pin(8, machine.Pin.OUT)


# Function to set the LED states for both sets simultaneously
def set_lights(r, y, g):
    red_led1.value(r)
    yellow_led1.value(y)
    green_led1.value(g)
    red_led2.value(r)
    yellow_led2.value(y)
    green_led2.value(g)


try:
    while True:
        # Red
        set_lights(0, 0, 1)  # Red on, yellow and green off
        utime.sleep(0.5)  # Wait for 0.5 seconds

        # Yellow
        set_lights(0, 1, 0)  # Yellow on, red and green off
        utime.sleep(0.5)  # Wait for 0.5 seconds

        # Green
        set_lights(1, 0, 0)  # Green on, red and yellow off
        utime.sleep(0.5)  # Wait for 0.5 seconds

except KeyboardInterrupt:
    print("Program stopped.")
    #Turn off all LEDs before exiting
    set_lights(0,0,0)

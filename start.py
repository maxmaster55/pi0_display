#!/bin/python3
import digitalio
import board
from adafruit_rgb_display.rgb import color565
from adafruit_rgb_display import st7789
from utils.internet import get_public_ip
from utils import screenadd
import time

# Configuration for CS and DC pins for Raspberry Pi
print("Display started")
cs_pin = digitalio.DigitalInOut(board.CE0)
dc_pin = digitalio.DigitalInOut(board.D25)
reset_pin = None
BAUDRATE = 64000000  # The pi can be very fast!
# Create the ST7789 display:
display = st7789.ST7789(
    board.SPI(),
    cs=cs_pin,
    dc=dc_pin,
    rst=reset_pin,
    baudrate=BAUDRATE,
    width=135,
    height=240,
    x_offset=53,
    y_offset=40,
)

backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True
buttonA = digitalio.DigitalInOut(board.D23)
buttonB = digitalio.DigitalInOut(board.D24)
buttonA.switch_to_input()
buttonB.switch_to_input()


screenadd.text(display, "test 1")

# Main loop:
while True:
    time.sleep(1)

#!/bin/python3
import digitalio
import board
import signal
from core.handlers import exit_handler
from adafruit_rgb_display.rgb import color565
from adafruit_rgb_display import st7789
from core.internet import get_public_ip
from core.screen import Screen
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
    rotation=90,
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

screen = Screen(display)
# registring the exit handler
signal.signal(signal.SIGINT, exit_handler(screen, backlight))

screen.show_text_centered("0_pi\ntest2")
time.sleep(.5)


i = 0
while True:

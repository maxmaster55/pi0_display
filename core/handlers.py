import sys
import time
from .screen import show_text_centered
def exit_signal_handler(sig, frame, display ,backlight):
    # turning off the display 
    show_text_centered(display, "Goodbye :(", 26)
    time.sleep(1)
    backlight.value = False
    sys.exit(0)



def exit_handler(display ,backlight):
    return lambda sig, frame: exit_signal_handler(sig, frame, display, backlight)

import sys
import time


def exit_signal_handler(sig, frame, screen, backlight):
    # turning off the display
    screen.show_text_centered("Goodbye! :(")
    time.sleep(1)
    backlight.value = False
    sys.exit(0)


def exit_handler(display, backlight):
    return lambda sig, frame: exit_signal_handler(sig, frame, display, backlight)

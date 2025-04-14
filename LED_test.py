from machine import Pin
from time import sleep

# GPIO pin numbers:
red = Pin(18, Pin.OUT)
green = Pin(4, Pin.OUT)
blue = Pin(0, Pin.OUT)  # Blue is wired to GPIO0

def show_color(r, g, b):
    red.value(r)
    green.value(g)
    blue.value(b)

while True:
    show_color(0, 1, 1)  # Red on
    sleep(1)
    show_color(1, 0, 1)  # Green on
    sleep(1)
    show_color(1, 1, 0)  # Blue on
    sleep(1)
    show_color(1, 1, 1)  # All off
    sleep(1)
#!/usr/bin/python3

import json, requests, time
from neopixel import *

# LED strip configuration:
LED_COUNT      = 300      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 96      # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
strip.begin()

while True:
    try:
        r = requests.get("http://dogspluspl.us/bin/ledcontrol.py")
    except:
        print("Failed connection.")
        continue

    colors = json.loads(r.text)
    print("GET: " + str(colors))

    for i in range(0, 300):
        strip.setPixelColor(i, Color(int(colors['green']), int(colors['red']), int(colors['blue'])))

    strip.show()
    time.sleep(3)

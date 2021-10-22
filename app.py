# NeoPixel library strandtest example
# Author: Tony DiCola (tony@tonydicola.com)
#
# Direct port of the Arduino NeoPixel library strandtest example.  Showcases
# various animations on a strip of NeoPixels.
import time

from ledStripAbstractionLayer import begin, setPixelColor, show, createLedStrip, Color

def multiColorWipe(color1, color2, wait_ms=5):
    """Wipe color across multiple LED strips a pixel at a time."""
    global strip1

    # for i in range(ledStripAbstractionLayer.numPixels(strip1)):
    for i in range(30):
        if i % 2:
            # even number
            setPixelColor(strip1, i, color1)
            show(strip1)
            time.sleep(wait_ms / 1000.0)
        else:
            # odd number
            setPixelColor(strip1, i, color1)
            show(strip1)
            time.sleep(wait_ms / 1000.0)

    time.sleep(1)


def blackout(strip):
    # for i in range(max(strip.numPixels(), strip.numPixels())):
    for i in range(30):
        setPixelColor(strip, i, Color(0, 0, 0))
        show(strip)


# Main program logic follows:
if __name__ == '__main__':
    # # Create NeoPixel objects with appropriate configuration for each strip.
    strip1 = createLedStrip()

    # # Intialize the library (must be called once before other functions).
    begin(strip1)

    # # Black out any LEDs that may be still on for the last run
    blackout(strip1)

    while True:
        # Multi Color wipe animations.
        multiColorWipe(Color(255, 0, 0), Color(255, 0, 0))  # Red wipe
        multiColorWipe(Color(0, 255, 0), Color(0, 255, 0))  # Blue wipe
        multiColorWipe(Color(0, 0, 255), Color(0, 0, 255))  # Green wipe


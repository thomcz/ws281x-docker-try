
from rpi_ws281x import PixelStrip

LED_1_COUNT = 110        # Number of LED pixels.
LED_1_PIN = 18          # GPIO pin connected to the pixels (must support PWM! GPIO 13 and 18 on RPi 3).
LED_1_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_1_DMA = 10          # DMA channel to use for generating signal (Between 1 and 14)
LED_1_BRIGHTNESS = 255  # Set to 0 for darkest and 255 for brightest
LED_1_INVERT = False    # True to invert the signal (when using NPN transistor level shift)
LED_1_CHANNEL = 0       # 0 or 1

class LedStrip:
    def __init__(self):
        self.strip = PixelStrip(LED_1_COUNT, LED_1_PIN, LED_1_FREQ_HZ,
                            LED_1_DMA, LED_1_INVERT, LED_1_BRIGHTNESS,
                            LED_1_CHANNEL)
        self.ledState = []
        self.strip.begin()
        self.resetLeds()

    def setLeds(self, ledList, color):
        if (self.ledState == ledList):
            return
        self.ledState = ledList

        self.resetLeds()
        for led in self.ledState:
            self.strip.setPixelColor(led, color)
        self.strip.show()

    def resetLeds(self):
        for led in range(self.strip.numPixels()):
            self.strip.setPixelColor(led, 0)
            self.strip.show()

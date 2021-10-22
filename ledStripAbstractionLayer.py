from rpi_ws281x_mock import Color as ws281xColor, PixelStrip

LED_1_COUNT = 30        # Number of LED pixels.
LED_1_PIN = 18          # GPIO pin connected to the pixels (must support PWM! GPIO 13 and 18 on RPi 3).
LED_1_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_1_DMA = 10          # DMA channel to use for generating signal (Between 1 and 14)
LED_1_BRIGHTNESS = 128  # Set to 0 for darkest and 255 for brightest
LED_1_INVERT = False    # True to invert the signal (when using NPN transistor level shift)
LED_1_CHANNEL = 0       # 0 or 1

# class LedStripAbstractionLayer:
def createLedStrip(): 
    return PixelStrip(LED_1_COUNT, LED_1_PIN, LED_1_FREQ_HZ,
                            LED_1_DMA, LED_1_INVERT, LED_1_BRIGHTNESS,
                            LED_1_CHANNEL)

def begin(strip: PixelStrip):
    strip.begin()

def setPixelColor(strip: PixelStrip, i, color):
    strip.setPixelColor(i, color)

def show(strip: PixelStrip):
    strip.show()

def numPixels(strip: PixelStrip):
    strip.numPixels()

def Color(red, green, blue, white=0):
    return ws281xColor(red, green, blue, white=0)

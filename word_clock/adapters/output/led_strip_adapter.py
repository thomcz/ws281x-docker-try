from typing import List

from rpi_ws281x import PixelStrip

from word_clock.ports.output_ports.display_port import DisplayPort


# LED strip configuration
LED_COUNT = 110        # Number of LED pixels
LED_PIN = 18           # GPIO pin connected to the pixels (must support PWM!)
LED_FREQ_HZ = 800000   # LED signal frequency in hertz (usually 800khz)
LED_DMA = 10           # DMA channel to use for generating signal (Between 1 and 14)
LED_BRIGHTNESS = 255   # Set to 0 for darkest and 255 for brightest
LED_INVERT = False     # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL = 0        # 0 or 1


class LedStripAdapter(DisplayPort):
    """
    Adapter that implements the DisplayPort interface using the WS281x library.
    This adapter encapsulates all LED strip hardware interactions.
    """
    
    def __init__(self):
        """
        Initialize the LED strip adapter.
        """
        self.strip = PixelStrip(
            LED_COUNT, 
            LED_PIN, 
            LED_FREQ_HZ,
            LED_DMA, 
            LED_INVERT, 
            LED_BRIGHTNESS,
            LED_CHANNEL
        )
        self.led_state = []
        self.strip.begin()
        self.reset_leds()
    
    def set_leds(self, led_list: List[int], color: int) -> None:
        """
        Set the specified LEDs to the given color.
        
        Args:
            led_list: List of LED indices to set
            color: Color value to set the LEDs to
        """
        if self.led_state == led_list:
            return
        self.led_state = led_list

        self.reset_leds()
        for led in self.led_state:
            self.strip.setPixelColor(led, color)
        self.strip.show()
    
    def reset_leds(self) -> None:
        """
        Turn off all LEDs.
        """
        for led in range(self.strip.numPixels()):
            self.strip.setPixelColor(led, 0)
        self.strip.show()
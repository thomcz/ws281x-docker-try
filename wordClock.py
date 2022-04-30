from wordClockState import WordClockState
from rpi_ws281x import Color

class WordClock:
    def __init__(self, ledStrip, color = Color(255, 255, 255)):
        self.ledStrip = ledStrip
        self.color = color
        self.state = WordClockState()

    def run(self):
        newLeds = self.state.getActualState()

        self.__updateTime(newLeds)

    def __updateTime(self, newLeds):
        self.ledStrip.setLeds(newLeds, self.color)

from ledStrip import LedStrip
from wordClock import WordClock
from time import sleep

def wordClock():
    wordClock = WordClock(ledStrip)
    wordClock.run()

if __name__ == '__main__':
    ledStrip = LedStrip()
    # TODO use scheduling
    while(True):
        wordClock()
        sleep(30)

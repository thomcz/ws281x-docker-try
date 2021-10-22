import requests
class PixelStrip(object):
    def __init__(
        self,
        num,
        pin,
        freq_hz=800000,
        dma=10,
        invert=False,
        brightness=255,
        channel=0,
        strip_type=None,
        gamma=None,):
        self.started = False

    def begin(self):
        requests.post('http://host.docker.internal:4000/begin/')

    def show(self):
        requests.post('http://host.docker.internal:4000/show/')

    def setPixelColor(self, i, color):
        requests.post('http://host.docker.internal:4000/setPixelColor/', data = {
            'ledId': i, 
            'color': color
            }
        )

    def numPixels(self):
        requests.get('http://host.docker.internal:4000/numPixels/')

def Color(red, green, blue, white=0):
    return '#%02x%02x%02x' % (red, green, blue)

from datetime import datetime
from pytz import timezone

class WordClockState:

    _ES_IST = [9,10,30,49,50]
    _EIN = [24,35,44]
    _EINS = _EIN + [55]
    _ZWEI = [4,15,24,35]
    _DREI = [16,23,36,43]
    _VIER = [77,82,97,102]
    _FUENF = [76,83,96,103]
    _SECHS = [19,20,39,40,59]
    _SIEBEN = [55,64,75,84,95,104]
    _ACHT = [18,21,38,41]
    _NEUN = [37,42,57,62]
    _ZEHN = [58,61,78,81]
    _ELF = [2,17,22]
    _ZWOELF = [54,65,74,85,94]
    _STUNDE = [_ZWOELF, _EINS, _ZWEI, _DREI, _VIER, _FUENF, _SECHS, _SIEBEN, _ACHT, _NEUN, _ZEHN, _ELF, _ZWOELF]

    #X nach/vor
    _NACH = [26,33,46,53]
    _VOR = [66,73,86]

    _FUENF_MINUTE = [70,89,90,109]
    _ZEHN_MINUTE = [8,11,28,31]
    _VIERTEL = [47,52,67,72,87,92,107]
    _ZWANZIG = [48,51,68,71,88,91,108]
    _HALB = [5,14,25,34]
    

    #X nach
    _FUENF_NACH = _FUENF_MINUTE + _NACH
    _ZEHN_NACH = _ZEHN_MINUTE + _NACH
    _VIERTEL_NACH = _VIERTEL + _NACH
    _ZWANZIG_NACH = _ZWANZIG + _NACH


    #X vor
    _FUENF_VOR = _FUENF_MINUTE + _VOR
    _ZEHN_VOR = _ZEHN_MINUTE + _VOR
    _VIERTEL_VOR = _VIERTEL + _VOR
    _ZWANZIG_VOR = _ZWANZIG + _VOR


    _MINUTE = [[], _FUENF_NACH, _ZEHN_NACH, _VIERTEL_NACH, _ZWANZIG_NACH, _FUENF_VOR + _HALB, _HALB, _FUENF_NACH + _HALB, _ZWANZIG_VOR, _VIERTEL_VOR, _ZEHN_VOR, _FUENF_VOR]
    
    _UHR = [80,99,100]

    def getActualState(self):
        localDatetime = datetime.now(timezone('Europe/Berlin'))

        minute = int(localDatetime.minute / 5)
        hour = localDatetime.hour % 12 + (1 if minute > 4 else 0)

        return self.getPrefix() + \
            self.getMinute()[minute] + \
            self.getHour()[hour] + \
            (self.getPostfix() if(minute == 0) else [])

    def calculateOffset(self, minute):
        if minute > 4:
            return minute
        return 0

    def getPrefix(self):
        return self._ES_IST

    def getPostfix(self):
        return self._UHR

    def getHour(self):
        return self._STUNDE

    def getMinute(self):
        return self._MINUTE




class Record():


    _sepalLength = 0.0
    _sepalWidth = 0.0
    _pedalLength = 0.0
    _pedalWidth = 0.0
    _classification = ""

    def __init__(self, sepalLength, sepalWidth, pedalLength, pedalWidth, classification):
        self._sepalLength = sepalLength
        self._sepalWidth = sepalWidth
        self._pedalLength = pedalLength
        self._pedalWidth = pedalWidth
        self._classification = classification

    def getSepalLength(self):
        return self._sepalLength

    def getSepalWidth(self):
        return self._sepalWidth

    def getPedalLength(self):
        return self._pedalLength

    def getPedalWidth(self):
        return self._pedalWidth
    
    def getClassification(self):
        return self._classification

    
        
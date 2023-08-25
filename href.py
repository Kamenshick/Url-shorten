from hex import Hex
from shortsting import shortString

class Href:
    def __init__(self):
        self.href = ''
        self.hexHref = ''

    def setHref(self,href):
        self.href = href
    def setHexHref(self):
        self.hexHref = shortString.cutStringToEleven(Hex.hrefToString(self.href))

    def getHref(self):
        return self.href
    def getHexHref(self):
        return self.hexHref
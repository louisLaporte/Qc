import curses

from Qc.Core import CObject
from Qc.Extra import *

class CLayout(CObject):

    def __init__(self):
        super().__init__()

    def width(self):
        raise NotImplemented

    def height(self):
        raise NotImplemented

    def setWidth(self):
        raise NotImplemented

    def setHeight(self):
        raise NotImplemented

    def addWidget(self, widget):
        raise NotImplemented

    def removeWidget(self, widget):
        raise NotImplemented

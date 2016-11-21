from Qc.Extra import *

class CObject(object):

    def __init__(self, *args):
        super().__init__()

        self.args = args

    def setObjectName(self, name):
        """ """
        self.name = name

    def objectName(self):
        """ """
        return self.name

    def children(self):
        """ """
        raise NotImplemented

    def parent(self):
        """ """
        raise NotImplemented

    def setParent(self):
        """ """
        raise NotImplemented

    def connect(self, observer):
        """ connect CSignal and CSlot"""
        self.observer = observer

    def disconnect(self, observer):
        """ """
        raise NotImplemented

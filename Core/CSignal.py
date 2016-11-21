from Qc.Core import CObject

class CSignal(CObject):

    def __init__(self, *args):
        super().__init__()

    def emit(self, *args):
        """ signal emition """
        for i, a in enumerate(args):
            if not isinstance(a, self.args[i]):
                raise TypeError

        self.observer(self, *args)

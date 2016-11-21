import curses
from collections import OrderedDict
from Qc.Widgets import CLayout

from Qc.Extra import *
#from log import *

class CGridLayout(CLayout):

    def __init__(self):
        super().__init__()

        self.widgets = []
        self.widget  = OrderedDict()
        self.widget_keys = ["object", "row", "column"]
        self.widget.fromkeys(self.widget_keys)
        self.row    = -1
        self.column = -1

    def __call__(self):
        self.debug()

    def addWidget(self, widget, row, column):
        """ """
        # Import below is not on the top beacause it cause conflict with CWidget
        from Qc.Widgets import CWidget

        if isinstance(widget, CWidget):
            self.widget["object"] = widget
            self.widget["row"]    = row
            self.widget["column"] = column

            self.widgets.append(self.widget)

            if row > self.row:
                self.row = row

            if column > self.column:
                self.column = column
        else:
            raise TypeError(widget, "must be a CWidget")

    def rowCount(self):
        return self.row

    def columnCount(self):
        return self.column

    def getItemPosition(self, row, column):
        # Must be improve --> actual test Fail
        raise NotImplemented
        return next(item["object"] for item in self.widgets
                            if item["row"] == row and item["column"] == column)

    def debug(self):
        INFO(self.widget["object"].objectName(), self.widget["object"].win.getmaxyx())


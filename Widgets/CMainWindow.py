import curses

from Qc.Gui import CWindow
from Qc.Widgets import CWidget
from Qc.Extra import *

class CMainWindow(CWindow, CWidget):

    def __init__(self):
        super().__init__()

        self.stdscr = self.get_stdscr()
        self.main = CWidget()
        self.setSize(self.height(), self.width())

    def width(self):
        return self.size()[1]

    def height(self):
        return self.size()[0]

    def size(self):
        return self.stdscr.getmaxyx()

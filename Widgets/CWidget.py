import curses
from collections import OrderedDict
from Qc.Core import CObject
from Qc.Extra import *

class CWidget(CObject):

    def __init__(self):
        super().__init__()

        self.h   = 50
        self.w   = 200
        self.win = curses.newwin(self.h, self.w)
        self.x = self.win.getbegyx()[1]
        self.y = self.win.getbegyx()[0]

    def __call__(self):
        pass

    def setWidth(self, width):
        self.w = width
        self.win.resize(self.h, self.w)

    def width(self):
        return self.w

    def setHeight(self, height):
        self.h = height
        self.win.resize(self.h, self.w)

    def height(self):
        return self.h

    def setSize(self, height, width):
        self.w = width
        self.h = height
        self.win.resize(self.h, self.w)

    def size(self):
        return self.h, self.w

    def addLayout(self, layout):
        # import lib when needed, if on top of file an error
        # is raised because CLayout need CWidget
        from Qc.Widgets import CLayout
        from Qc.Widgets import CGridLayout

        if isinstance(layout, CLayout):
            self.layout        = OrderedDict()
            self.layout_keys   = ["object", "window"]
            self.layout.fromkeys(self.layout_keys)

            self.layout["window"] = curses.newwin(self.height() - 2, self.width() - 2, 1, 1)
            self.layout["object"] = layout
        else:
            raise TypeError(layout, "must be a CLayout")

    def layout(self):
        return self.layout

    def update(self, x, y, h, w):
        self.x = x
        self.y = y
        self.h = h
        self.w = w

    def show(self, border=True):
        curses.init_pair(1, curses.COLOR_CYAN , curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_RED  , curses.COLOR_BLACK)
        curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)
        curses.init_pair(4, curses.COLOR_CYAN , curses.COLOR_BLACK)

        self.win.erase()
        self.win.resize(self.height(), self.width())
        self.win.mvwin(self.y, self.x)

        self.win.attron(curses.color_pair(1))
        self.win.box()
        self.win.attroff(curses.color_pair(1))

        curses.echo()
        self.win.addstr(self.height() - 1, 1, "{} | x: {} y: {} h: {} w: {}"
                .format(self.objectName(),self.x, self.y, self.height(), self.width()), curses.A_BOLD)
        curses.noecho()

        self.win.refresh()

        if hasattr(self, "layout"):
            diff_height = 2
            diff_width  = 2
            self.h_l = self.height() - diff_height
            self.w_l = self.width()  - diff_width
            self.layout["window"].erase()
            self.layout["window"].resize(self.h_l, self.w_l)

            self.layout["window"].attron(curses.color_pair(2))
            self.layout["window"].box()
            self.layout["window"].attroff(curses.color_pair(2))
            self.layout["window"].overlay(self.win)

            curses.echo()
            # Print Layout
            self.layout["window"].addstr(self.h_l - 1, 1, "{} | h: {} w: {}"
                    .format(self.layout["object"].objectName(), self.h_l, self.w_l), curses.A_BOLD)
            curses.noecho()
            self.layout["window"].refresh()

            for widget in list(self.layout["object"].widgets):
                self.h_w = (self.h_l - diff_height) // (self.layout["object"].row    + 1)
                self.w_w = (self.w_l - diff_width)  // (self.layout["object"].column + 1)
                self.x_w = diff_width   + (self.w_w) * widget["column"]
                self.y_w = diff_height  + (self.h_w) * widget["row"]

                widget["object"].update(self.x_w, self.y_w, self.h_w, self.w_w)

                try:
                    widget["object"].show()

                except TypeError as err:
                    # Handle this error when calling show() method <-- unsupscriptable
                    pass

    def debug(self):
        DEBUG("Widget: {} | size: {}".format(self.objectName(), self.size()))

    def print_size(self):
        try:
            curses.echo()
            self.win.addstr(self.height() - 3, 2, "h: {} w: {}"
                    .format(self.height(), self.width()), curses.A_BOLD)
            curses.noecho()

        except curses.error:
            pass

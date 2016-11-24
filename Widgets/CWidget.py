import curses
from collections import OrderedDict
from Qc.Core import CObject
from Qc.Extra import *

class CWidget(CObject):

    def __init__(self):
        super().__init__()

        self.height = 50
        self.width = 200
        self.win = curses.newwin(self.height, self.width)
        self.y, self.x = self.win.getbegyx()

        curses.init_color(curses.COLOR_GREEN, 0, 100, 0)
        curses.init_pair(1, curses.COLOR_CYAN , curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_RED  , curses.COLOR_BLACK)
        curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)
        curses.init_pair(4, curses.COLOR_CYAN , curses.COLOR_BLACK)

    def __call__(self):
        pass
    def __str__(self):
        _str = "{} | x: {} y: {} h: {} w: {}".format(self.objectName(), self.x, self.y, self.height, self.width)
        return _str

    def addLayout(self, layout):
        # import lib when needed, if on top of file an error
        # is raised because CLayout need CWidget
        from Qc.Widgets import CLayout
        from Qc.Widgets import CGridLayout

        if isinstance(layout, CLayout):
            self._layout        = OrderedDict()
            self._layout_keys   = ["object", "window"]
            self._layout.fromkeys(self._layout_keys)

            self._layout["window"] = CWidget()
            self._layout["object"] = layout
        else:
            raise TypeError(layout, "must be a CLayout")

    @property
    def layout(self):
        if hasattr(self, '_layout'):
            return self._layout
        else:
            raise AttributeError

    def update(self, x=None, y=None, h=None, w=None):
        # this function use key args because of readability
        self.x      = x
        self.y      = y
        self.height = h
        self.width  = w

    def show(self, border=True):
        #
        # It is implemented as 3 levels --> Must 2 levels

        self.win.erase()
        self.win.resize(self.height, self.width)
        self.win.mvwin(self.y, self.x)

        self.color_box(widget=self.win, color=1, box=border)

        self.window_info()

        #DEBUG("1) name {} | x: {} y: {} h: {} w: {}"
        #.format(self.objectName(),self.x, self.y, self.height, self.width) )

        self.win.refresh()

        if hasattr(self, '_layout'):
            lw = self._layout["window"]
            lo = self._layout["object"]
            #DEBUG("2) name {} --> add attribute layout"
            #    .format(self.objectName()) )

            diff_height = 1
            diff_width  = 1
            self.l_h = self.height - diff_height * 2
            self.l_w = self.width  - diff_width  * 2
            self.l_x = self.x      + diff_height
            self.l_y = self.y      + diff_width
            lw.update(x=self.l_x, y=self.l_y, h=self.l_h, w=self.l_w)

            lw.win.erase()
            lw.win.resize(self.l_h, self.l_w)
            lw.win.mvwin(self.l_y, self.l_x)
            self.color_box(widget=lw.win, color=2, box=border)

            #DEBUG("2.1) drawing {}" .format(lo.objectName()))


            try:
                lw.win.overlay(self.win)

            except curses.error:
                DEBUG("overlay problem")

            else:
                self.window_info(lw)
                #lw.addstr(self.h_l - 1, 1, "{} | h: {} w: {}"
                #        .format(lo.objectName(), self.h_l, self.w_l), curses.A_BOLD)
                #curses.noecho()

                lw.win.refresh()

                for widget in lo.widgets:

                    wo = widget["object"]
                    wc = widget["column"]
                    wr = widget["row"]
                    self.h_w = (self.l_h - diff_height * 2) // (lo.row    + 1)
                    self.w_w = (self.l_w - diff_width  * 2) // (lo.column + 1)
                    self.x_w = self.l_x  + 1 + (self.w_w) * wc
                    self.y_w = self.l_y  + 1 + (self.h_w) * wr

                    wo.update(x=self.x_w, y=self.y_w, h=self.h_w, w=self.w_w)

                    #DEBUG("3) name {} | x: {} y: {} h: {} w: {}"
                    #.format(wo.objectName(), wo.x(), wo.y(), wo.height(), wo.width()) )

                    try:
                        wo.show()

                    except TypeError as err:
                        # Handle this error when calling show() method <-- unsupscriptable
                        DEBUG("ERROR for widget: {}  try to exec {}.show() | Error: {}"
                            .format(self.objectName(), wo.objectName(), err))
        else:
            DEBUG("{} has not attribute layout".format(self.objectName()))

    def color_box(self, widget=None, color=None, box=False):
        if box:
            widget.attron(curses.color_pair(color))
            widget.box()
            widget.attroff(curses.color_pair(color))

    def window_info(self, widget=None):
        try:
            curses.echo()
            if not widget:
                self.win.addstr(self.height - 1, 2, str(self))
            #else:
            #    widget.win.addstr(widget.height - 1, 2, str(widget))

            curses.noecho()
        except curses.error:
            pass

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, val):
        self._x = val

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, val):
        self._y = val

    @property
    def width(self):
        return self._w

    @width.setter
    def width(self, width):
        self._w = width

    @property
    def height(self):
        return self._h

    @height.setter
    def height(self, height):
        self._h = height

    @property
    def size(self):
        return self._h, self._w

    @size.setter
    def size(self, height, width):
        self.height = height
        self.width  = width

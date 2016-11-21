import curses

class CWindow():

    def __init__(self):
        self.stdscr = curses.initscr()
        self.stdscr.immedok(True)    # any change refresh window
        self.stdscr.keypad(1)        # escape sequence
        curses.noecho()              # turn off echo mode
        curses.cbreak()              # do no affect tty when live
        curses.start_color()
        curses.curs_set(0)

    def get_stdscr(self):
        return self.stdscr

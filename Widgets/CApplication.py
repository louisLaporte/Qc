import curses

class CApplication():

    def __init__(self):
        """ Init curses """
        self.stdscr = curses.initscr()
        self.stdscr.immedok(True)    # any change refresh window
        self.stdscr.keypad(1)        # escape sequence
        curses.noecho()              # turn off echo mode
        curses.cbreak()              # do no affect tty when live
        curses.start_color()
        curses.curs_set(0)

    def exit(self):
        """ End curses """
        curses.nocbreak()
        self.stdscr.keypad(0)
        curses.echo()
        curses.endwin()

import curses, time, locale
from curses import textpad

locale.setlocale(locale.LC_ALL, "")
code = locale.getpreferredencoding()


class Input:
    def __init__(self,
                 stdscr,
                 starty=0,
                 startx=0,
                 endy=0,
                 endx=0,
                 handle_submit=None):
        self.stdscr = stdscr
        self.handle_submit = handle_submit
        self.starty = starty + 2
        self.startx = startx + 2
        self.endy = endy - 1
        self.endx = endx - 2
        self.active = True
        scry, scrx = self.stdscr.getmaxyx()
        self.available_space = self.endx - self.startx
        self.win = None

    def render(self, status=None):
        curses.echo()
        curses.nocbreak()
        if self.win:
            del self.win
        self.win = curses.newwin(2, self.available_space - 2, self.starty,
                                 self.startx)
        self.box = textpad.Textbox(self.win, insert_mode=True)
        self.stdscr.refresh()
        self.contents = self.box.edit(self.__enter_is_terminate)
        del self.win
        self.win = None
        self.handle_submit(self.contents)
        curses.noecho()
        curses.cbreak()

    def receive_input(self, key):
        pass

    def __enter_is_terminate(self, x):
        if x == 10 or x == 13 or x == curses.KEY_ENTER:
            return 7

    def __printString(self, y, x, text, color):
        if color:
            self.stdscr.attron(curses.color_pair(color))
        self.stdscr.addstr(y, x, text)
        if color:
            self.stdscr.attroff(curses.color_pair(color))

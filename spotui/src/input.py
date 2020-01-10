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

    def render(self, status=None):
        win = curses.newwin(2, self.available_space - 2, self.starty,
                            self.startx)
        box = textpad.Textbox(win, insert_mode=True)
        curses.echo()
        curses.nocbreak()
        self.stdscr.refresh()
        contents = box.edit(self.__enter_is_terminate)
        win.clrtoeol()
        del box
        del win
        self.handle_submit(contents)
        curses.noecho()
        curses.cbreak()

    def receive_input(self, key):
        pass

    def __enter_is_terminate(self, x):
        if x == 10 or x == 13 or x == curses.KEY_ENTER:
            self.stdscr.clear()
            return 7

    def __printString(self, y, x, text, color):
        if color:
            self.stdscr.attron(curses.color_pair(color))
        self.stdscr.addstr(y, x, text)
        if color:
            self.stdscr.attroff(curses.color_pair(color))

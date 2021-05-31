import curses


class Component:
    component = None
    startx = 0
    starty = 0
    endx = 0
    endy = 0
    title = None
    popup = False
    interactive = False

    def __init__(self, stdscr):
        self.stdscr = stdscr

    def activate(self):
        curses.curs_set(0)
        self.component.active = True

    def deactivate(self):
        curses.curs_set(1)
        self.component.active = False

    def create_border(self, color):
        self.stdscr.attron(curses.color_pair(color))

        # vertical borders
        for i in range(self.starty + 1, self.endy):
            self.stdscr.addstr(i, self.startx, "│") # symbol use
            self.stdscr.addstr(i, self.endx, "│") # symbol use

        # horizontal borders
        for i in range(self.startx + 1, self.endx):
            self.stdscr.addstr(self.starty, i, "─") # symbol use
            self.stdscr.addstr(self.endy, i, "─") # symbol use

        # top left corner
        self.stdscr.addstr(self.starty, self.startx, "╭") # symbol use

        # top right corner
        self.stdscr.addstr(self.starty, self.endx, "╮") # symbol use

        # bottom left corner
        self.stdscr.addstr(self.endy, self.startx, "╰") # symbol use

        # bottom right corner
        self.stdscr.addstr(self.endy, self.endx, "╯") # symbol use

        # title
        if self.title:
            self.stdscr.addstr(self.starty, self.startx + 2,
                               " " + self.title + " ")

        self.stdscr.attroff(curses.color_pair(color))

    def render(self, status=None):
        if self.popup:
            for x in range(self.startx, self.endx + 1):
                for y in range(self.starty, self.endy + 1):
                    self.stdscr.addstr(y, x, " ")
            self.create_border(10) # color use
        elif self.interactive:
            self.create_border(5 if self.component.active else 4) # color use
        self.component.render(status)

    def receive_input(self, key):
        pass

import curses
from spotui.src.util import truncate
from spotui.src.input import Input
from spotui.src.component import Component


class SearchInput(Component):
    def __init__(self, stdscr, api, handle_search, close):
        self.stdscr = stdscr
        self.api = api
        self.handle_search = handle_search
        self.close = close
        self.active = True
        self.popup = True
        self.title = "Search"
        self.interactive = False
        self.restart()

    def restart(self):
        scry, scrx = self.stdscr.getmaxyx()
        box_height = 4
        box_width = round(scrx / 3)
        self.startx = round((scrx / 2) - (box_width / 2))
        self.endx = self.startx + box_width
        self.starty = round((scry / 2) - (box_height / 2))
        self.endy = self.starty + box_height
        self.component = Input(
            self.stdscr,
            self.starty,
            self.startx,
            self.endy,
            self.endx,
            self.handle_search,
        )

    def activate(self):
        self.component.active = True

    def deactivate(self):
        self.component.active = False

    def receive_input(self, key):
        if key == curses.KEY_ENTER or key in [10, 13]:
            self.close()
        else:
            self.component.receive_input(key)

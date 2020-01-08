import curses
from spotui.src.menu import Menu
from spotui.src.component import Component


class LibraryMenu(Component):
    def __init__(self, stdscr, api, change_tracklist):
        self.stdscr = stdscr
        self.api = api
        self.change_tracklist = change_tracklist
        self.title = "Made For You"
        self.interactive = True
        self.items = [
            {
                "text": "Top Tracks",
                "handler": self.__select_top_tracks
            },
            {
                "text": "Recently Played",
                "handler": self.__select_recent_tracks
            },
            {
                "text": "Liked Songs",
                "handler": self.__select_liked_tracks
            },
        ]
        self.restart()

    def restart(self):
        scry, scrx = self.stdscr.getmaxyx()
        self.startx = 0
        self.endx = round(scrx / 4) - 2
        self.starty = 0
        self.endy = 5
        self.component = Menu(
            self.stdscr,
            self.items,
            self.starty,
            self.startx,
            self.endy,
            self.endx,
            self.component and self.component.active,
            self.component.selected
            if self.component and self.component.selected else 0,
            self.component.scroll_start
            if self.component and self.component.scroll_start else 0,
        )

    def __select_top_tracks(self):
        self.change_tracklist(self.api.get_top_tracks(), "Top Tracks")

    def __select_recent_tracks(self):
        self.change_tracklist(self.api.get_recently_played(),
                              "Recently Played")

    def __select_liked_tracks(self):
        self.change_tracklist(self.api.get_liked_tracks(), "Liked Songs")

    def receive_input(self, key):
        if key == curses.KEY_ENTER or key in [10, 13]:
            self.items[self.component.selected]["handler"]()
        else:
            self.component.receive_input(key)

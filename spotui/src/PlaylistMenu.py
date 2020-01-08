import curses
from spotui.src.util import truncate
from spotui.src.menu import Menu
from spotui.src.component import Component


class PlaylistMenu(Component):
    def __init__(self, stdscr, api, change_tracklist):
        self.stdscr = stdscr
        self.api = api
        self.change_tracklist = change_tracklist
        self.title = "Playlists"
        self.interactive = True
        self.items = self.api.get_playlists()
        self.restart()

    def restart(self):
        self.items = self.api.get_playlists()
        scry, scrx = self.stdscr.getmaxyx()
        self.startx = 0
        self.endx = round(scrx / 4) - 2
        self.starty = 6
        self.endy = scry - 5
        self.component = Menu(
            self.stdscr,
            list(map(self.__map_playlists, self.items)),
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

    def __select_playlist(self, playlist_name, playlist_id, playlist_uri):
        self.change_tracklist(self.api.get_playlist_tracks(playlist_id),
                              playlist_name, playlist_uri)

    def __map_playlists(self, item):
        available_space = self.endx - self.startx - 6
        item["text"] = truncate(item["text"], available_space)

        def handler():
            self.__select_playlist(item["text"], item["id"], item["uri"])

        item["handler"] = handler
        return item

    def receive_input(self, key):
        if key == curses.KEY_ENTER or key in [10, 13]:
            self.items[self.component.selected]["handler"]()
        else:
            self.component.receive_input(key)

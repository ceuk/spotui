import curses
from spotui.src.util import truncate
from spotui.src.menu import Menu
from spotui.src.component import Component


class TracksMenu(Component):
    def __init__(self, stdscr, api, play_track, status=None):
        self.stdscr = stdscr
        self.api = api
        self.currently_playing = None
        self.play_track = play_track
        self.title = "Top Tracks"
        self.interactive = True
        self.items = []
        self.tracks = []
        self.restart()
        self.refresh_now_playing(status)

    def restart(self):
        scry, scrx = self.stdscr.getmaxyx()
        self.startx = round(scrx / 4)
        self.endx = scrx - 2
        self.starty = 0
        self.endy = scry - 5
        self.update_tracks(self.tracks, self.title)

    def update_tracks(self, tracks, title):
        self.tracks = tracks
        self.items = list(map(self.__map_tracks, tracks)) if tracks else []
        self.title = title
        self.component = Menu(
            self.stdscr,
            self.items,
            self.starty,
            self.startx,
            self.endy,
            self.endx,
            self.component and self.component.active,
            self.component.selected if self.component
            and self.component.selected < len(self.items) else 0,
            self.component.scroll_start
            if self.component and self.component.scroll_start else 0,
        )

    def refresh_now_playing(self, status):
        currently_playing = (status["item"]["uri"]
                             if status and status["is_playing"] else None)
        if currently_playing and currently_playing != self.currently_playing:
            self.currently_playing = currently_playing
            self.restart()

    def receive_input(self, key):
        if ((key == curses.KEY_ENTER or key in [10, 13]) and self.items
                and len(self.items) > 0):
            self.items[self.component.selected]["handler"]()
        else:
            self.component.receive_input(key)

    def __map_tracks(self, track):
        available_space = self.endx - self.startx
        highlight = self.currently_playing and self.currently_playing == track[
            "uri"]
        max_word_length = round((available_space / 2) - 3)
        track_name = self.__pad_track_text(
            truncate(track["name"], max_word_length),
            max_word_length,
        )
        artist_name = self.__pad_track_text(
            truncate(track["artist"], max_word_length),
            max_word_length,
        )

        def handler():
            self.play_track(track["uri"])

        return {
            "text": track_name + " " + artist_name,
            "handler": handler,
            "highlight": highlight,
        }

    def __pad_track_text(self, text, max_word_length):
        spaces_needed = max_word_length - len(text)
        if spaces_needed > 0:
            for i in range(0, spaces_needed + 1):
                text += " "
        return text

import curses
from spotui.src.util import ms_to_hms, truncate
from spotui.src.menu import Menu
from spotui.src.component import Component


class NowPlaying(Component):
    def __init__(self, stdscr):
        self.stdscr = stdscr
        self.interactive = False
        self.restart()

    def restart(self):
        scry, scrx = self.stdscr.getmaxyx()
        self.startx = 0
        self.endx = scrx - 2
        self.starty = scry - 3
        self.endy = scry - 1
        self.component = NowPlayingComponent(
            self.stdscr,
            self.starty,
            self.startx,
            self.endy,
            self.endx,
        )

    def receive_input(self, key):
        pass


class NowPlayingComponent:
    def __init__(self, stdscr, starty, startx, endy, endx):
        self.stdscr = stdscr
        self.starty = starty
        self.startx = startx
        self.endy = endy
        self.endx = endx
        self.active = False
        self.playing = False
        self.track_name = "-"
        self.artist_name = "-"
        self.track_length = 0
        self.progress = 0
        self.progress_percent = 0

    def render(self, status):
        scry, scrx = self.stdscr.getmaxyx()
        if status:
            self.playing = status["is_playing"]
        if self.playing and status and status["item"]:
            current_track = status["item"]
            self.track_name = current_track["name"]
            self.artist_name = current_track["artists"][0]["name"]
            self.track_length = current_track["duration_ms"]
            self.progress = status["progress_ms"]
            self.progress_percent = ((self.progress / self.track_length) *
                                     100 if self.progress > 0
                                     and self.track_length > 0 else 0)
        shuffle = status["shuffle_state"] if status else False
        repeat = status["repeat_state"] if status else False
        shuffle_symbol = "咽" if shuffle else ""
        repeat_symbol = ""
        if repeat == "track":
            repeat_symbol = "綾"
        if repeat == "context":
            repeat_symbol = "凌"
        status_symbol = "契" if self.playing else " "
        timestamp = ms_to_hms(self.progress) + "/" + ms_to_hms(
            self.track_length)
        max_length = self.endx - self.startx - (len(timestamp) + 3)
        max_length = max_length if max_length > 0 else 0
        progress_length = round(
            ((self.endx - self.startx - 4) / 100) * self.progress_percent)
        track_info = truncate(
            ("Nothing is playing"
             if self.track_name == "-" else status_symbol + shuffle_symbol +
             repeat_symbol + " " + self.track_name + " - " + self.artist_name),
            max_length,
        )
        # Track + Artist
        self.stdscr.addstr(self.starty, self.startx + 1, track_info)

        # Progress text
        self.stdscr.addstr(self.starty, self.endx - len(timestamp), timestamp)

        # Progress bar
        for i in range(
                0,
                round(self.endx - self.startx - 4 - self.progress_percent) +
                1):
            self.stdscr.addstr(self.endy, self.endx - 2 - i, "░")
        self.stdscr.attron(curses.color_pair(11))
        self.stdscr.addstr(self.endy, self.startx + 1, "")
        for i in range(0, progress_length + 1):
            self.stdscr.addstr(self.endy, self.startx + 2 + i, "█")
        if self.progress_percent > 99.4:
            self.stdscr.addstr(self.endy, self.endx - 1, "")
        self.stdscr.attroff(curses.color_pair(11))
        if self.progress_percent < 99.5:
            self.stdscr.addstr(self.endy, self.endx - 1, "")

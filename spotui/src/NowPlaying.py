import curses
from spotui.src.util import ms_to_hms, truncate
from spotui.src.menu import Menu
from spotui.src.component import Component
from spotui.src.config import get_config

config = get_config() # symbol use
use_nerd_fonts = config.get("other", "use_nerd_fonts") == "yes"
play_icon = "契" if use_nerd_fonts else "▶"
pause_icon = " " if use_nerd_fonts else "⏸ "
shuffle_icon = "咽" if use_nerd_fonts else "🔀"
repeat_track_icon = "綾" if use_nerd_fonts else "🔁(t)"
repeat_icon = "凌" if use_nerd_fonts else "🔁"


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
        shuffle_symbol = shuffle_icon if shuffle else ""
        repeat_symbol = ""
        if repeat == "track":
            repeat_symbol = repeat_track_icon
        if repeat == "context":
            repeat_symbol = repeat_icon
        status_symbol = play_icon if self.playing else pause_icon
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
            self.stdscr.addstr(self.endy, self.endx - 2 - i, "░") # symbol use
        self.stdscr.attron(curses.color_pair(11)) # color use
        self.stdscr.addstr(self.endy, self.startx + 1, "") # symbol use
        for i in range(0, progress_length + 1):
            self.stdscr.addstr(self.endy, self.startx + 2 + i, "█") # symbol use
        if self.progress_percent > 99.4: #TODO: these endcaps don't make any sense and look weird like this
            self.stdscr.addstr(self.endy, self.endx - 1, "") # symbol use
        self.stdscr.attroff(curses.color_pair(11)) # color use
        if self.progress_percent < 99.5:
            self.stdscr.addstr(self.endy, self.endx - 1, "") # symbol use

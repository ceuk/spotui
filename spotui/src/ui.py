from spotui.src.MainForm import MainForm
from spotui.src.colors import init_colors


class App:
    def __init__(self, stdscr):
        init_colors()
        self.main_form = MainForm(stdscr)

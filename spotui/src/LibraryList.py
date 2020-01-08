import curses
from spotui.src.menu import Menu
from spotui.src.component import Component


class Lib(Component):
    def __init__(self, stdscr):
        self.stdscr = stdscr
        scry, scrx = stdscr.getmaxyx()
        self.interactive = True
        self.startx = round(scrx / 4)
        self.endx = scrx - 2
        self.starty = 0
        self.endy = scry - 10
        self.items = [
            "Baby one more time",
            "Baby one more time",
            "Baby one more time",
            "Oops, I did it again",
            "Toxic",
            "Baby one more time",
            "Oops, I did it again",
            "Toxic",
            "Baby one more time",
            "Oops, I did it again",
            "Toxic",
            "Baby one more time",
            "Oops, I did it again",
            "Oops, I did it again",
            "Toxic",
            "Baby one more time",
            "Oops, I did it again",
            "Toxic",
            "Baby one more time",
            "Oops, I did it again",
            "Toxic",
            "Baby one more time",
            "Oops, I did it again",
            "Oops, I did it again",
            "Toxic",
            "Baby one more time",
            "Oops, I did it again",
            "Toxic",
            "Baby one more time",
            "Oops, I did it again",
            "Toxic",
            "Baby one more time",
            "Oops, I did it again",
            "Toxic",
            "Slave4u",
        ]
        self.component = Menu(
            stdscr,
            self.items,
            self.starty + 1,
            self.startx + 2,
            self.endy - 1,
            self.endx - 2,
        )

    def receive_input(self, key):
        self.component.receive_input(key)

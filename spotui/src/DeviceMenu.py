import curses
from spotui.src.util import truncate
from spotui.src.menu import Menu
from spotui.src.component import Component


class DeviceMenu(Component):
    def __init__(self, stdscr, api, select_device, close):
        self.stdscr = stdscr
        self.api = api
        self.select_device = select_device
        self.close = close
        self.active = True
        self.popup = True
        self.title = "Select a Device"
        self.interactive = True
        self.items = api.get_devices()
        self.restart()

    def restart(self):
        self.items = self.api.get_devices()
        scry, scrx = self.stdscr.getmaxyx()
        box_height = round(scry / 2)
        box_width = round(scrx / 2.5)
        self.startx = round((scrx / 2) - (box_width / 2))
        self.endx = self.startx + box_width
        self.starty = round((scry / 2) - (box_height / 2))
        self.endy = self.starty + box_height
        self.component = Menu(
            self.stdscr,
            list(map(self.__map_devices, self.items))
            if self.items and len(self.items) > 0 else [],
            self.starty,
            self.startx,
            self.endy,
            self.endx,
        )

    def __map_devices(self, item):
        available_space = self.endx - self.startx - 6
        item["text"] = truncate(item["text"], available_space)

        def handler():
            if item and "id" in item:
                self.select_device(item["id"])

        item["handler"] = handler
        return item

    def receive_input(self, key):
        if ((key == curses.KEY_ENTER or key in [10, 13]) and self.items
                and len(self.items) > 0):
            self.items[self.component.selected]["handler"]()
            self.close()
        else:
            self.component.receive_input(key)

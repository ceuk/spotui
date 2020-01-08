import curses


class Menu:
    def __init__(
        self,
        stdscr,
        items=[],
        starty=0,
        startx=0,
        endy=0,
        endx=0,
        active=False,
        selected=0,
        scroll_start=0,
    ):
        self.stdscr = stdscr
        self.starty = starty + 2
        self.startx = startx + 2
        self.endy = endy - 1
        self.endx = endx - 2
        self.items = items
        self.selected = selected
        self.active = active
        scry, scrx = self.stdscr.getmaxyx()
        self.available_space = self.endy - self.starty + 1
        self.scroll_start = scroll_start
        self.scroll_end = (len(items) -
                           1 if len(items) <= self.available_space +
                           self.scroll_start else self.available_space +
                           self.scroll_start - 1)

    def select(self, index):
        if index >= 0 and index <= len(self.items) - 1:
            self.selected = index

    def render(self, status=None):
        scry, scrx = self.stdscr.getmaxyx()
        for i, itemIndex in enumerate(
                range(self.scroll_start, self.scroll_end + 1)):
            item = self.items[itemIndex]
            x = self.startx
            y = self.starty + i
            selected = itemIndex == self.selected and self.active
            if y >= 0 and y <= scry and x >= 0 and x <= scrx:
                color = None
                if "highlight" in item and item["highlight"]:
                    color = 12
                if selected:
                    color = 6
                self.__printString(y, x, item["text"], color)

    def receive_input(self, key):
        if (key == curses.KEY_UP or key == ord("k")) and self.selected > 0:
            self.select(self.selected - 1)
        if (key == curses.KEY_DOWN
                or key == ord("j")) and self.selected < len(self.items) - 1:
            self.select(self.selected + 1)
        if self.selected < self.scroll_start:
            self.scroll_up()
        if self.selected > self.scroll_end:
            self.scroll_down()

    def scroll_up(self):
        self.scroll_start -= 1
        self.scroll_end -= 1

    def scroll_down(self):
        self.scroll_start += 1
        self.scroll_end += 1

    def __printString(self, y, x, text, color):
        if color:
            self.stdscr.attron(curses.color_pair(color))
        self.stdscr.addstr(y, x, text)
        if color:
            self.stdscr.attroff(curses.color_pair(color))

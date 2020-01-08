import curses


def init_colors():
    # Default text
    curses.init_pair(1, curses.COLOR_WHITE, 0)
    # White text
    curses.init_pair(4, curses.COLOR_WHITE, curses.COLOR_BLACK)
    # Yellow text
    curses.init_pair(5, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    # Magenta text
    curses.init_pair(10, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
    # Green text
    curses.init_pair(11, curses.COLOR_GREEN, curses.COLOR_BLACK)
    # Cyan text
    curses.init_pair(12, curses.COLOR_CYAN, curses.COLOR_BLACK)
    # Selected item
    curses.init_pair(6, curses.COLOR_BLACK, curses.COLOR_WHITE)
    # Highlighted (no bg)
    curses.init_pair(7, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
    # Highlighted (bg)
    curses.init_pair(8, curses.COLOR_WHITE, curses.COLOR_MAGENTA)

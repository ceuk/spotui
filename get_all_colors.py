
import curses


def main(stdscr):
    curses.start_color()
    curses.use_default_colors()

    count = 1

    for i in range(0, curses.COLORS):
        curses.init_pair(i + 1, i, -1)

    # try:
    for i2 in range(0, 255):
        pad = "{:>3}".format(str(i2 - 1))
        stdscr.addstr(pad, curses.color_pair(i2))
        stdscr.addstr( "  ")

        if i2 is 0:
            y, x = stdscr.getyx()
            maxy, maxx = stdscr.getmaxyx()
            stdscr.move((y + 1) %maxy, 0)
            pass

        if i2 is 16 or i2 is 8:
            y, x = stdscr.getyx()
            maxy, maxx = stdscr.getmaxyx()
            stdscr.move((y + 1) %maxy, 0)
            pass

        if i2 > 16:
            count = count + 1 
            if count % 6 is 1:
                y, x = stdscr.getyx()
                maxy, maxx = stdscr.getmaxyx()
                stdscr.move((y + 1) %maxy, 0)
  
    stdscr.getch()

curses.wrapper(main)
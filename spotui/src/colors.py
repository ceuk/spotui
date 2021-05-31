import curses
from spotui.src.config import get_config


def init_colors():


    config = get_config() # symbol use
    use_default_bg = config.get("colors", "use_default_background") == "yes"
    use_256_colors = config.get("colors", "use_256_colors") == "yes"

    if use_default_bg:
        curses.use_default_colors() # from: https://linux.die.net/man/3/use_default_colors


    curses.setupterm()
    if use_256_colors and curses.tigetnum("colors") == 256:
        
    #     # set up individual colors. run get_all_colors.py to see them all
        purple      = 64
        cyan        = 40
        green       = 47
        yellow      = 215
        orange      = 203
        magenta     = 197
        gray_light  = 250
        gray_dark   = 238
        light       = 254
        dark        = 234
        transparent = 0


        # set up pairs
        # Default text
        curses.init_pair(1, light, transparent)
        # White text
        curses.init_pair(4, light, dark)
        # Yellow text
        curses.init_pair(5, yellow, dark)
        # Magenta text
        curses.init_pair(10, magenta, dark)
        # Green text
        curses.init_pair(11, green, dark)
        # Cyan text
        curses.init_pair(12, cyan, dark)
        # Selected item
        curses.init_pair(6, dark, light)
        # Highlighted (no bg)
        curses.init_pair(7, magenta, dark)
        # Highlighted (bg)
        curses.init_pair(8, light, magenta)
    
    else:
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

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
        purple      = 63
        cyan        = 39
        green       = 35
        yellow      = 214
        orange      = 202
        magenta     = 196
        gray_light  = 249
        gray_dark   = 237
        light       = 253
        dark        = 233
        transparent = -1


        # set up pairs
        # Default text
        curses.init_pair(1, light, transparent)
        # White text - background to inactive component border
        curses.init_pair(4, light, dark)
        # Yellow text - background to active component border
        curses.init_pair(5, yellow, dark)
        # Magenta text - background to popup components, overrides above
        curses.init_pair(10, magenta, dark)
        # Green text - now playing seekbar
        curses.init_pair(11, green, dark)
        # Cyan text - currently playing song, in lists
        curses.init_pair(12, purple, dark)
        # Selected item - cursor line highlight
        curses.init_pair(6, dark, light)
        # Highlighted (no bg) - no use that I can see
        curses.init_pair(7, magenta, dark)
        # Highlighted (bg) - no use that I can see
        curses.init_pair(8, light, magenta)
    
    else:
        curses.init_pair(1, curses.COLOR_WHITE, 0)
        # White text - background to inactive component border
        curses.init_pair(4, curses.COLOR_WHITE, curses.COLOR_BLACK)
        # Yellow text - background to active component border
        curses.init_pair(5, curses.COLOR_YELLOW, curses.COLOR_BLACK)
        # Magenta text - background to popup components, overrides above
        curses.init_pair(10, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
        # Green text - no use that I can see
        curses.init_pair(11, curses.COLOR_GREEN, curses.COLOR_BLACK)
        # Cyan text - currently playing song, in lists
        curses.init_pair(12, curses.COLOR_CYAN, curses.COLOR_BLACK)
        # Selected item - cursor line highlight
        curses.init_pair(6, curses.COLOR_BLACK, curses.COLOR_WHITE)
        # Highlighted (no bg) - no use that I can see
        curses.init_pair(7, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
        # Highlighted (bg) - no use that I can see
        curses.init_pair(8, curses.COLOR_WHITE, curses.COLOR_MAGENTA)

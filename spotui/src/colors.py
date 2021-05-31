import curses


def init_colors():
    curses.use_default_colors() # from: https://linux.die.net/man/3/use_default_colors
    # Default text 1
    curses.init_pair(1, 254, 235)
    # White text 4
    #background to inactive component border
    curses.init_pair(4, 254, 234)
    # Yellow text 5
    #background to active component border
    curses.init_pair(5, 215, 234)
    # Magenta text
    #background to popup components, overrides above
    curses.init_pair(10, 197, 234)
    # Green text    
    #no use that I can see
    curses.init_pair(11, 47, 234)
    # Cyan text
    #currently playing song, in lists
    curses.init_pair(12, 40, 234)
    # Selected item
    #cursor line highlight
    curses.init_pair(6, 234, 254)
    # Highlighted (no bg)
    #no use that I can see
    curses.init_pair(7, 197, 47)
    # Highlighted (bg)
    #no use that I can see
    curses.init_pair(8, 254, 197)

    ## testing xterm-256

    # curses.setupterm()

    # # check config value instead of checking here
    # if curses.tigetnum("colors") == 256:
        
    #     # set up individual colors. run get_all_colors.py to see them all
    #     purple      = 64
    #     cyan        = 40
    #     green       = 47
    #     yellow      = 215
    #     orange      = 203
    #     magenta     = 197
    #     gray_light  = 250
    #     gray_dark   = 238
    #     light       = 254
    #     dark        = 234
    #     transparent = 0


    #     # set up pairs
    #     # Default text
    #     curses.init_pair(1, light, transparent)
    #     # White text
    #     curses.init_pair(4, light, dark)
    #     # Yellow text
    #     curses.init_pair(5, yellow, dark)
    #     # Magenta text
    #     curses.init_pair(10, magenta, dark)
    #     # Green text
    #     curses.init_pair(11, green, dark)
    #     # Cyan text
    #     curses.init_pair(12, cyan, dark)
    #     # Selected item
    #     curses.init_pair(6, dark, light)
    #     # Highlighted (no bg)
    #     curses.init_pair(7, magenta, dark)
    #     # Highlighted (bg)
    #     curses.init_pair(8, light, magenta)

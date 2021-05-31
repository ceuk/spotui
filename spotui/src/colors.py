import curses
from spotui.src.config import get_config


def init_colors():


    config = get_config() # symbol use
    use_256_colors = config.get("colors", "use_256_colors") == "yes"
    transp = config.get("colors", "override_bg_with_transparent") == "yes"

    curses.use_default_colors() # from: https://linux.die.net/man/3/use_default_colors

    curses.setupterm()

    #TODO: refactor this into a cleaner if/else where  only vars are iffed, and the init_pair doesn't get repeated
    if use_256_colors and curses.tigetnum("colors") == 256:
        
    #     # set up individual colors. run get_all_colors.py to see them all

        df_fg = int(config.get("custom_colors_256", "default_text_fg"))
        df_bg = int(config.get("custom_colors_256", "default_text_bg")) if not transp else -1
  
        ib_fg = int(config.get("custom_colors_256", "inactive_border_fg"))
        ib_bg = int(config.get("custom_colors_256", "inactive_border_bg")) if not transp else -1
  
        ab_fg = int(config.get("custom_colors_256", "active_border_fg"))
        ab_bg = int(config.get("custom_colors_256", "active_border_bg")) if not transp else -1
  
        pb_fg = int(config.get("custom_colors_256", "popup_border_fg"))
        pb_bg = int(config.get("custom_colors_256", "popup_border_bg")) if not transp else -1
  
        sb_fg = int(config.get("custom_colors_256", "seekbar_fg"))
        sb_bg = int(config.get("custom_colors_256", "seekbar_bg")) if not transp else -1
  
        lp_fg = int(config.get("custom_colors_256", "list_now_playing_fg"))
        lp_bg = int(config.get("custom_colors_256", "list_now_playing_bg")) if not transp else -1
  
        cs_fg = int(config.get("custom_colors_256", "cursor_fg"))
        cs_bg = int(config.get("custom_colors_256", "cursor_bg"))
    
        cp_fg = int(config.get("custom_colors_256", "cursor_now_playing_fg"))
        cp_bg = int(config.get("custom_colors_256", "cursor_now_playing_bg"))

        ### set up pairs
        # Default text
        curses.init_pair(1, df_fg, df_bg)
        
        # background to inactive component border
        curses.init_pair(4, ib_fg, ib_bg)
        
        # background to active component border
        curses.init_pair(5, ab_fg, ab_bg)
        
        # background to popup components, overrides above
        curses.init_pair(10, pb_fg, pb_bg)
        
        # now playing seekbar
        curses.init_pair(11, sb_fg, sb_bg)
        
        # currently playing song, in lists
        curses.init_pair(12, lp_fg, lp_bg)
        
        # cursor line highlight
        curses.init_pair(6, cs_fg, cs_bg)

        # cursor line highlight, list item selected
        curses.init_pair(7, cp_fg, cp_bg)

        # Highlighted (bg) - no use that I can see
        #curses.init_pair(8, light, magenta)
    
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

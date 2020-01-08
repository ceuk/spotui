import curses
from spotui.src.ui import App


def main():
    SpoTUI = curses.wrapper(App)


if __name__ == "__main__":
    main()

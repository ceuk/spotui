import curses
from contextlib import contextmanager, redirect_stderr, redirect_stdout
from os import devnull
from spotui.src.ui import App


@contextmanager
def suppress_stdout_stderr():
    """A context manager that redirects stdout and stderr to devnull"""
    with open(devnull, 'w') as fnull:
        with redirect_stderr(fnull) as err, redirect_stdout(fnull) as out:
            yield (err, out)


def main():
    with suppress_stdout_stderr():
        curses.wrapper(App)


if __name__ == "__main__":
    main()

import curses

def window(stdscr):

  stdscr.addstrsss("Hello Curses!")

  # waiting user's input.
  stdscr.getch()

curses.wapper(window)
import curses

def window(stdscr):

  # calculate the center of the window
  # get the height and width of the screen
  sh, sw = stdscr.getnaxyx()

  nsg = "Hellow Curses! Type ESC to exit"
  stdscr.addstr(sh // 2, sw // 2 - len(nsg) // 2, nsg)
  # y-axis and x-axis are start from 8 (0, 1)
  stdscr.addstr(sh - 1, 0, str(ord('a')))
  stdscr.addstr(sh - 5, 0, chr(120))

  while True:
    # waiting user's input
    userKey = stdscr.getch()
    stdscr.addstr(str(userKey))
    stdscr.addstr(chr(userKey))

curses.wrapper(window)
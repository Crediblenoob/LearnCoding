import curses

def window(stdscr):

  curses.start_color()
  curses.use_default_colors()
  chr(9608)

  for i in range(0, curses.COLORS):
    curses.init_pair(i +1, i, -1)
    stdscr.addstr("<{0}>".format(i + 1), curses.color_pair(i + 1))

  while True:
    userKey = stdscr.getch()
    stdscr.addstr(str(userKey))
    stdscr.addstr(chr(userKey))
    if userKey == 27:
      break

  stdscr.getch()

curses.wrapper(window)
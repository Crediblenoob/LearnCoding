import curses

def window(stdscr):

  sh, sw = stdscr.getmaxyx()

  msg = "Hello Curses! Type ESC to exit!"
  stdscr.addstr(sh // 4, sw // 2 - len(msg) // 2, msg)
  stdscr.addstr(sh - 10, 47, str(ord('a')))
  stdscr.addstr(sh - 10, 47, chr(120))

  while True:
    userKey = stdscr.getch()
    stdscr.addstr(str(userKey))
    stdscr.addstr(chr(userKey))
    if userKey == 27:
      break

curses.wrapper(window)
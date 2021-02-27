import curses
from curses import textpad
import random

def main(stdscr):

    curses.start_color()
    curses.use_default_colors()
    curses.init_pair(1, 46, -1)
    curses.init_pair(2, 196, -1)

    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(50)

    sh, sw = stdscr.getmaxyx()
    center = [sh // 2, sw // 2]

    box = [
        [3, 3],
        [sh - 3, sw - 3]
    ]
    textpad.rectangle( stdscr, box[0][0], box[0][1], box[1][0], box[1][1])

    snake = [
        [center[0], center[1] + 1],
        center,
        [center[0], center[1] - 1],
    ]

    for point in snake:
        stdscr.addstr(point[0], point[1], chr(9724), curses.color_pair(1))

    direction = curses.KEY_RIGHT

    food = [
        random.randint(box[0][0] + 1, box[1][0] - 1),
        random.randint(box[0][1] + 1, box[1][1] - 1)
    ]
    stdscr.addstr(food[0], food[1], "*", curses.color_pair(2))

    score = 0

    while 1:
        key = stdscr.getch()

        if key == 27:
           break;

        if key == curses.KEY_UP:
          direction = curses.KEY_UP
        elif key == curses.KEY_RIGHT:
          direction = curses.KEY_RIGHT
        elif key == curses.KEY_DOWN:
          direction = key
        elif key == curses.KEY_LEFT:
          direction = key

        head = snake[0]

        #if head[0] < food[0]:
         #   direction = curses.KEY_DOWN
       # elif head[0] > food[0]:
       #     direction = curses.KEY_UP
        #elif head[1] < food[1]:
       #     direction = curses.KEY_RIGHT
       # elif head[1] > food[1]:
       #     direction = curses.KEY_LEFT

        if direction == curses.KEY_UP:
            newHead = [head[0] - 1, head[1]]
        elif direction == curses.KEY_DOWN:
            newHead = [head[0] + 1, head[1]]
        elif direction == curses.KEY_RIGHT:
            newHead = [head[0], head[1] + 1]
        elif direction == curses.KEY_LEFT:
            newHead = [head[0], head[1] - 1]

        stdscr.addstr(newHead[0], newHead[1], chr(9724), curses.color_pair(1))
        snake.insert(0, newHead)

        if snake[0] == food:
            score += 1
            food = [
                random.randint(box[0][0] + 1, box[1][0] - 1),
                random.randint(box[0][1] + 1, box[1][1] - 1)
            ]
            stdscr.addstr(food[0], food[1], "*", curses.color_pair(2))
        else:
            stdscr.addstr(snake[-1][0], snake[-1][1], " ")
            snake.pop()

        if (snake[0][0] in [box[0][0], box[1][0]] or
            snake[0][1] in [box[0][1], box[1][1]]):

            msg = "Game Over! Press any key to exit!"
            stdscr.addstr(center[0], center[1] - len(msg)//2, msg)
            stdscr.nodelay(0)
            stdscr.getch()
            break

curses.wrapper(main)
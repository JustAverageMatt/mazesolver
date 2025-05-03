import sys

from maze import Maze
from window import Window


def main():
    num_rows = 12
    num_cols = 16
    margin = 50
    screen_x = 800
    screen_y = 600
    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows
    win = Window(screen_x, screen_y)

    sys.setrecursionlimit(10000)

    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win, 10)
    print("maze created")
    is_solvable = maze.solve()
    if not is_solvable:
        print("maze can not be solved!")
    else:
        print("maze solved!")
    win.wait_for_close()


main()

# seed = None
#
# maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win)

# c1 = Cell(win)
# c1.has_right_wall = False
# c1.draw(50, 50, 100, 100)
#
# c2 = Cell(win)
# c2.has_left_wall = False
# c2.has_bottom_wall = False
# c2.draw(100, 50, 150, 100)
#
# c1.draw_move(c2)
#
# c3 = Cell(win)
# c3.has_top_wall = False
# c3.has_right_wall = False
# c3.draw(100, 100, 150, 150)
#
# c2.draw_move(c3):
#
# c4 = Cell(win)
# c4.has_left_wall = False
# c4.draw(150, 100, 200, 150)
#
# c3.draw_move(c4, True)

# p1 = Point(100, 100)
# p2 = Point(200, 300)
# line1 = Line(p1, p2)
# win.draw_line(line1, "blue")
#
# p3 = Point(200, 125)
# p4 = Point(340, 500)
# line2 = Line(p3, p4)
# win.draw_line(line2, "red")

# cell1 = Cell(win, 50, 50, 100, 100)
# cell1.draw()
#
# cell2 = Cell(win, 200, 50, 300, 150)
# cell2.has_left_wall = False
# cell2.draw("red")
#
# cell3 = Cell(win, 100, 100, 150, 150)
# cell3.has_bottom_wall = False
# cell3.draw("blue")
#
# cell4 = Cell(win, 50, 200, 150, 300)
# cell4.has_top_wall = False
# cell4.draw("green")
#
# cell5 = Cell(win, 200, 200, 300, 300)
# cell5.has_bottom_wall = False
# cell5.draw("purple")
#
# cell6 = Cell(win, 350, 200, 450, 300)
# cell6.has_top_wall = False
# cell6.has_bottom_wall = False
# cell6.draw("orange")
#
# cell7 = Cell(win, 50, 350, 150, 450)
# cell7.has_left_wall = False
# cell7.has_right_wall = False
# cell7.draw("brown")
#
# cell8 = Cell(win, 200, 350, 300, 450)
# cell8.has_right_wall = False
# cell8.has_top_wall = False
# cell8.has_bottom_wall = False
# cell8.draw("magenta")
#
# cell9 = Cell(win, 350, 350, 450, 450)
# cell9.has_left_wall = False
# cell9.has_right_wall = False
# cell9.has_top_wall = False
# cell9.has_bottom_wall = False
# cell9.draw("cyan")

# win.redraw()
#
# win.wait_for_close()


# if __name__ == "__main__":
main()

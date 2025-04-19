from window import Line, Point, Window


def main():
    win = Window(800, 600)
    p1 = Point(100, 100)
    p2 = Point(200, 300)
    line1 = Line(p1, p2)
    win.draw_line(line1, "blue")

    p3 = Point(200, 125)
    p4 = Point(340, 500)
    line2 = Line(p3, p4)
    win.draw_line(line2, "red")

    win.wait_for_close()


if __name__ == "__main__":
    main()

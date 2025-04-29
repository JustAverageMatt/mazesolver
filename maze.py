import random
import time

from cell import Cell


class Maze:
    def __init__(
        self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None
    ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = []

        if seed is not None:
            random.seed(seed)

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls()

    def _create_cells(self):
        for i in range(self._num_cols):
            col_cells = []
            for j in range(self._num_rows):
                col_cells.append(Cell(self._win))
            self._cells.append(col_cells)
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cells(i, j)

    def _draw_cells(self, i, j):
        if self._win is None:
            return
        x1 = self._x1 + i * self._cell_size_x
        y1 = self._y1 + j * self._cell_size_y
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.06)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cells(0, 0)
        self._cells[self._num_cols - 1][self._num_rows - 1].has_bottom_wall = False
        self._draw_cells(self._num_cols - 1, self._num_rows - 1)

    def _break_walls(self):
        # Start the recursive algorithm at the top-left cell
        self._break_walls_r(0, 0)

    def _break_walls_r(self, i, j):
        # 1. Mark the current cell as visited
        self._cells[i][j].visited = True

        # 2. Infinite loop until we backtrack
        while True:
            # 2.1 Create a list to hold possible directions
            possible_directions = []

            # 2.2 Check adjacent cells
            # Check left
            if i > 0 and not self._cells[i - 1][j].visited:
                possible_directions.append((i - 1, j, "left"))

            # Check right
            if i < self._num_cols - 1 and not self._cells[i + 1][j].visited:
                possible_directions.append((i + 1, j, "right"))

            # Check up
            if j > 0 and not self._cells[i][j - 1].visited:
                possible_directions.append((i, j - 1, "up"))

            # Check down
            if j < self._num_rows - 1 and not self._cells[i][j + 1].visited:
                possible_directions.append((i, j + 1, "down"))

            # 2.3 If no directions available, draw the cell and return
            if len(possible_directions) == 0:
                self._draw_cells(i, j)
                return

            # 2.4 Pick a random direction
            direction = random.choice(possible_directions)
            next_i, next_j, dir_name = direction

            # 2.5 Knock down the walls between current cell and chosen cell
            if dir_name == "left":
                self._cells[i][j].has_left_wall = False
                self._cells[next_i][next_j].has_right_wall = False
            elif dir_name == "right":
                self._cells[i][j].has_right_wall = False
                self._cells[next_i][next_j].has_left_wall = False
            elif dir_name == "up":
                self._cells[i][j].has_top_wall = False
                self._cells[next_i][next_j].has_bottom_wall = False
            elif dir_name == "down":
                self._cells[i][j].has_bottom_wall = False
                self._cells[next_i][next_j].has_top_wall = False

            # Update the display
            self._draw_cells(i, j)
            self._draw_cells(next_i, next_j)

            # 2.6 Recursively call _break_walls_r on the chosen cell
            self._break_walls_r(next_i, next_j)

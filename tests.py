import unittest

from maze import Maze


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_break_entrance_and_exit(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            m1._cells[0][0].has_top_wall,
            False,
        )
        self.assertEqual(
            m1._cells[num_cols - 1][num_rows - 1].has_bottom_wall,
            False,
        )

    def test_break_walls(self):
    # Use a fixed seed for reproducible testing
    num_cols = 5
    num_rows = 5
    m = Maze(0, 0, num_rows, num_cols, 10, 10, seed=42)
    
    # Check that all cells are marked as visited
    for i in range(num_cols):
        for j in range(num_rows):
            self.assertTrue(m._cells[i][j].visited)
    
    # Check that there is a path from start to end
    # This is a bit complex to test in a unit test but we could verify
    # that not all cells have all walls
    has_broken_walls = False
    for i in range(num_cols):
        for j in range(num_rows):
            cell = m._cells[i][j]
            if (not cell.has_left_wall or not cell.has_right_wall or 
                not cell.has_top_wall or not cell.has_bottom_wall):
                has_broken_walls = True
                break
    
    self.assertTrue(has_broken_walls)

    #     # Test 2: Very small maze (1x1)
    #
    # def test_small_maze(self):
    #     num_cols = 1
    #     num_rows = 1
    #     m2 = Maze(0, 0, num_rows, num_cols, 10, 10)
    #     self.assertEqual(
    #         len(m2._cells),
    #         num_cols,
    #     )
    #     self.assertEqual(
    #         len(m2._cells[0]),
    #         num_rows,
    #     )
    #
    # # Test 3: Large maze
    # def test_large_maze(self):
    #     num_cols = 50
    #     num_rows = 40
    #     m3 = Maze(0, 0, num_rows, num_cols, 5, 5)
    #     self.assertEqual(
    #         len(m3._cells),
    #         num_cols,
    #     )
    #     self.assertEqual(
    #         len(m3._cells[0]),
    #         num_rows,
    #     )
    #
    # # Test 4: Rectangular maze (not square)
    # def test_rectangular_maze(self):
    #     num_cols = 30
    #     num_rows = 10
    #     m4 = Maze(
    #         10, 10, num_rows, num_cols, 8, 12
    #     )  # Different starting position and cell sizes
    #     self.assertEqual(
    #         len(m4._cells),
    #         num_cols,
    #     )
    #     self.assertEqual(
    #         len(m4._cells[0]),
    #         num_rows,
    #     )


if __name__ == "__main__":
    unittest.main()

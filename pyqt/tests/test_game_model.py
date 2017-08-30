import random
import unittest

import game_model as t
from auxiliary_classes.cell import Cell


class TestGameModel(unittest.TestCase):
    def test_revival_cell(self):
        living_cells = [Cell(10, 3), Cell(10, 4), Cell(11, 3)]
        game = t.GameModel(living_cells)
        expected_result = [Cell(10, 3), Cell(10, 4), Cell(11, 3), Cell(11, 4)]
        self.assertListEqual(game.do_step(), expected_result)

    def test_slaying_cell(self):
        game = t.GameModel([Cell(3, 5)])
        self.assertEqual(len(game.do_step()), 0)

    def test_save_stable_state(self):
        living_cells = [Cell(0, 0), Cell(0, 1), Cell(1, 0), Cell(1, 1)]
        game = t.GameModel(living_cells)
        self.assertListEqual(game.do_step(), living_cells)

    def test_blinker(self):
        start_state = [Cell(1, 0), Cell(1, 1), Cell(1, 2)]
        game = t.GameModel(start_state)
        expected_result = [Cell(0, 1), Cell(1, 1), Cell(2, 1)]
        self.assertListEqual(game.do_step(), expected_result)

    def test_glider(self):
        start_state = [Cell(123, 123), Cell(124, 124), Cell(125, 124), Cell(123, 125), Cell(124, 125)]
        game = t.GameModel(start_state)

        expected_result = [Cell(124, 123), Cell(125, 124), Cell(123, 125), Cell(124, 125), Cell(125, 125)]
        self.do_test(expected_result, game.do_step())

        expected_result = [Cell(123, 124), Cell(125, 124), Cell(124, 125), Cell(124, 126), Cell(125, 125)]
        self.do_test(expected_result, game.do_step())

    def test_wrong_arguments(self):
        self.assertRaises(TypeError, lambda: t.GameModel("hello"))
        self.assertRaises(TypeError, lambda: t.GameModel([1, 2, 3]))

    def test_random_data_not_crash(self):
        for i in range(0, 100):
            cell = Cell(random.randint(-1000000, 1000000), random.randint(-1000000, 1000000))
            game = t.GameModel([cell])
            game.do_step()

    def do_test(self, expected, real):
        for element in expected:
            self.assertTrue(element in real)


if __name__ == "main":
    unittest.main()

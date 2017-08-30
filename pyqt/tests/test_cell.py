import unittest

from auxiliary_classes import cell as t


class TestCell(unittest.TestCase):
    def test_wrong_argument(self):
        t.Cell(567, 8176)
        self.assertRaises(TypeError, lambda: t.Cell(1.5, 2))
        self.assertRaises(TypeError, lambda: t.Cell("hello"))
        self.assertRaises(TypeError, lambda: t.Cell(1, 2.3))


if __name__ == "main":
    unittest.main()

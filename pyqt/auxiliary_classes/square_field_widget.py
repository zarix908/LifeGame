from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget
from auxiliary_classes.cell_widget import CellWidget
from auxiliary_classes.cell import Cell
import math


class SquareFieldWidget(QWidget):
    def __init__(self, cells_count, spacing_between_cells=1):
        super().__init__()
        if not (is_int(cells_count) and is_int(spacing_between_cells)):
            raise TypeError("arguments should be integer type")

        self.clicked = None
        self.view_horizontal_offset = 0
        self.view_vertical_offset = 0

        self.__cells_count = cells_count
        self.setGeometry(0, 0, super().width(), super().height())

        self.__grid_layout = QtWidgets.QGridLayout()
        self.__grid_layout.setHorizontalSpacing(spacing_between_cells)
        self.__grid_layout.setVerticalSpacing(spacing_between_cells)

        self.add_cells()

        self.setLayout(self.__grid_layout)

    def add_cells(self):
        for x in range(self.__cells_count):
            for y in range(self.__cells_count):
                cell_widget = CellWidget(Cell(x, y))
                cell_widget.clicked = self.child_cell_widget_clicked
                self.__grid_layout.addWidget(cell_widget, x, y)

    def child_cell_widget_clicked(self, coordinates):
        if self.clicked is not None:
            self.clicked(coordinates)

    def set_cells_state(self, cells, state):
        self.check_type(cells)
        for cell in cells:
            if 0 <= cell.x < self.__cells_count and 0 <= cell.y < self.__cells_count:
                self.__grid_layout.itemAtPosition(cell.x + self.view_horizontal_offset,
                                                  cell.y + self.view_vertical_offset).widget().set(state)

    def clear(self):
        for i in range(self.__grid_layout.count()):
            self.__grid_layout.itemAt(i).widget().set(state=False)

    def check_type(self, input_data):
        if not isinstance(input_data, list):
            raise TypeError("1st argument should be list type")
        for cell in input_data:
            if not isinstance(cell, Cell):
                raise TypeError("elements of list should be 'Cell' type")


def is_int(value):
    try:
        return math.modf(value)[1] == value
    except Exception:
        return False

from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPainter, QColor
from auxiliary_classes.cell import Cell


class CellWidget(QWidget):
    def __init__(self, coordinates):
        super().__init__()
        self.__is_active = False
        self.__color = QColor(0, 0, 0)

        self.check_type(coordinates)
        self.clicked = None
        self.__coordinates = coordinates

    def check_type(self, input_data):
        if not isinstance(input_data, Cell):
            raise TypeError("argument should be 'Cell' type")

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.fill_rectangles(qp)
        qp.end()

    def fill_rectangles(self, qp):
        qp.fillRect(0, 0, super().width(), super().height(), self.__color)

    def mouseReleaseEvent(self, arg):
        if self.clicked is not None:
            self.clicked(self.__coordinates)

    def set(self, state):
        if not isinstance(state, bool):
            raise TypeError("argument should have bool type")

        if state != self.__is_active:
            self.change_color()

    def change_color(self):
        active_color = QColor(0, 0, 0)
        inactive_color = QColor(0, 127, 0)
        self.__color = active_color if self.__is_active else inactive_color
        self.update()

        self.__is_active = not self.__is_active

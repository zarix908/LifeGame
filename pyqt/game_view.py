from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QWidget
from auxiliary_classes.square_field_widget import SquareFieldWidget

from game_controller import GameController
from game_model import GameModel


class GameView(QWidget):
    def __init__(self, game_controller, game_model, field_size):
        super().__init__()

        if not isinstance(game_controller, GameController) or not isinstance(game_model, GameModel):
            raise TypeError("1st argument should be GameModel type, 2nd argument should be GameController type")

        self.__game_controller = game_controller
        game_model.model_changed = self.redraw

        self.__main_layout = None
        self.__field_widget = None
        self.__steps_count_widget = None
        self.__animation_speed_widget = None
        self.init_ui(field_size)

    def init_ui(self, field_size):
        self.resize(600, 300)
        self.setWindowTitle("Game of Life")

        self.__main_layout = QtWidgets.QHBoxLayout()
        self.__field_widget = SquareFieldWidget(field_size)
        self.__field_widget.clicked = self.field_widget_clicked

        self.__main_layout.addWidget(self.__field_widget)

        controls_layout = QtWidgets.QVBoxLayout()

        self.__steps_count_widget = QtWidgets.QSpinBox()
        self.__steps_count_widget.setMaximum(100000)
        self.__steps_count_widget.setMinimum(0)

        self.__animation_speed_widget = QtWidgets.QSpinBox()
        self.__animation_speed_widget.setMaximum(10)
        self.__animation_speed_widget.setMinimum(1)

        next_steps_button = QtWidgets.QPushButton("Do steps")
        next_steps_button.clicked.connect(self.next_steps_button_clicked)

        previous_button_steps = QtWidgets.QPushButton("Undo steps")
        previous_button_steps.clicked.connect(self.previous_button_clicked)

        controls_layout.setAlignment(QtCore.Qt.AlignTop)

        controls_layout.addWidget(QtWidgets.QLabel("Steps count:"))
        controls_layout.addWidget(self.__steps_count_widget)
        controls_layout.addWidget(QtWidgets.QLabel("Animation speed"))
        controls_layout.addWidget(self.__animation_speed_widget)
        controls_layout.addWidget(next_steps_button)
        controls_layout.addWidget(previous_button_steps)

        self.__main_layout.addLayout(controls_layout)

        self.setLayout(self.__main_layout)

    def next_steps_button_clicked(self):
        self.__game_controller.do_steps(self.__steps_count_widget.value(),
                                        1000 // self.__animation_speed_widget.value())

    def previous_button_clicked(self):
        self.__game_controller.undo_steps(self.__steps_count_widget.value(),
                                          1000 // self.__animation_speed_widget.value())

    def field_widget_clicked(self, coordinates):
        self.__game_controller.change_cell_state(coordinates)

    def redraw(self, game_state):
        self.__field_widget.clear()
        self.__field_widget.set_cells_state(game_state, state=True)

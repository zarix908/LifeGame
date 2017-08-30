import sys

from PyQt5 import QtGui
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication

from game_controller import GameController
from game_model import GameModel
from game_view import GameView

choose_size_spin_box = None
choose_size_dialog = None


def start():
    model = GameModel([])
    view = GameView(GameController(model), model, choose_size_spin_box.value())
    choose_size_dialog.close()
    view.show()

if __name__ == '__main__':
    application = QApplication(sys.argv)
    application.setWindowIcon(QtGui.QIcon("resources/icon.png"))

    choose_size_dialog = QtWidgets.QDialog()
    layout = QtWidgets.QVBoxLayout()
    choose_size_spin_box = QtWidgets.QSpinBox()
    choose_size_spin_box.setMinimum(1)
    choose_size_spin_box.setMaximum(100)
    ok_button = QtWidgets.QPushButton("OK")
    ok_button.clicked.connect(start)
    layout.addWidget(QtWidgets.QLabel("Выберите размер поля:"))
    layout.addWidget(choose_size_spin_box)
    layout.addWidget(ok_button)
    choose_size_dialog.setLayout(layout)
    choose_size_dialog.show()

    sys.exit(application.exec_())
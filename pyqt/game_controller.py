from PyQt5.QtCore import QTimer


class GameController:
    def __init__(self, game_model):
        self.__game_model = game_model
        self.__animation_timer = None
        self.__previous_steps = []
        self.__steps_count = None

    def do_steps(self, steps_count, interval):
        self.__steps_count = steps_count
        self.__animation_timer = QTimer()
        self.__animation_timer.timeout.connect(self.do_step)
        self.__animation_timer.start(interval)

    def do_step(self):
        if self.__steps_count == 0:
            self.__animation_timer.stop()
        else:
            self.__previous_steps.append(self.__game_model.get_living_cells())
            self.__game_model.do_step()
            self.__steps_count -= 1

    def undo_steps(self, steps_count, interval):
        self.__steps_count = steps_count
        self.__animation_timer = QTimer()
        self.__animation_timer.timeout.connect(self.undo_step)
        self.__animation_timer.start(interval)

    def undo_step(self):
        if self.__steps_count == 0:
            self.__animation_timer.stop()
        else:
            self.__game_model.clear()
            for cell in self.__previous_steps.pop():
                self.change_cell_state(cell)
            self.__steps_count -= 1

    def change_cell_state(self, coordinates):
        cell = coordinates.copy()
        self.__game_model.change_cell_state(cell)

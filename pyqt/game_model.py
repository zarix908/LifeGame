from auxiliary_classes.cell import Cell
import copy


class GameModel:
    def __init__(self, living_cells):
        self.check_type(living_cells)
        self.__living_cells = living_cells
        self.model_changed = None

    def check_type(self, input_data):
        if not isinstance(input_data, list):
            raise TypeError("1st argument should be list type")
        for cell in input_data:
            if not isinstance(cell, Cell):
                raise TypeError("elements of list should be 'Cell' type")

    def do_step(self):
        next_step_living_cells = []

        for cell in self.__living_cells:
            if self.is_alive(cell) and cell not in next_step_living_cells:
                next_step_living_cells.append(cell)

            neighbors = self.get_neighbours(cell)
            for neighbor in neighbors:
                if self.is_alive(neighbor) and neighbor not in next_step_living_cells:
                    next_step_living_cells.append(neighbor)

        self.__living_cells = next_step_living_cells
        if self.model_changed is not None:
            self.model_changed(copy.copy(self.__living_cells))
        return self.__living_cells.copy()

    def change_cell_state(self, cell):
        if not isinstance(cell, Cell):
            raise TypeError("argument should be 'Cell' type")

        if cell in self.__living_cells:
            self.__living_cells.remove(cell)
        else:
            self.__living_cells.append(cell)
        if self.model_changed is not None:
            self.model_changed(copy.copy(self.__living_cells))

    def is_alive(self, cell):
        count = 0
        for neighbor in self.get_neighbours(cell):
            if neighbor in self.__living_cells:
                count += 1

        return (cell in self.__living_cells) if count == 2 else (count == 3)

    def get_living_cells(self):
        return self.__living_cells.copy()

    def clear(self):
        self.__living_cells.clear()

    def get_neighbours(self, cell):
        for x in range(-1, 2):
            for y in range(-1, 2):
                if x != 0 or y != 0:
                    yield Cell(cell.x + x, cell.y + y)

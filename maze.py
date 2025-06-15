from cell import Cell
import random
import time


class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win,
    ):
        self.cells_ = []
        self.x1_ = x1
        self.y1_ = y1
        self.num_rows_ = num_rows
        self.num_cols_ = num_cols
        self.cell_size_x_ = cell_size_x
        self.cell_size_y_ = cell_size_y
        self.win_ = win

        self.__create_cells()

    def __create_cells(self):
        for i in range(self.num_cols_):
            col_cells = []
        
            for j in range(self.__num_rows):
                col_cells.append(Cell(self.__win))
            
            self.__cells.append(col_cells)
        
        for i in range(self.__num_cols):
            for j in range(self.__num_rows):
                self.__draw_cell(i, j)
    
    def __draw_cell(self, i, j):
        if self.__win is None:
            return
        x1 = self.__x1 + i * self.__cell_size_x
        y1 = self.__y1 + j * self.__cell_size_y
        x2 = x1 + self.__cell_size_x
        y2 = y1 + self.__cell_size_y
        self.__cells[i][j].draw(x1, y1, x2, y2)
        self.__animate()

    def __animate(self):
        if self.__win is None:
            return
        self.__win.redraw()
        time.sleep(0.05)

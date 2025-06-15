from graphics import *
from tkinter import Tk, BOTH, Canvas


class Cell:
    def __init__(self,window):
        self.has_left_wall = True;
        self.has_right_wall = True;
        self.has_top_wall = True;
        self.has_bottom_wall = True;
        self.x1_ = -1
        self.y1_ = -1
        self.x2_ = -1
        self.y2_ = -1
        self.win_ = window
    
    def draw(self, x1, y1, x2, y2):
        
        if self.win_ is None:
            return

        x1_ = x1
        y1_ = y1
        y2_ = y2
        x2_ = x2

        if self.has_left_wall:
            line = Line(Point(x1, y1), Point(x1, y2))
            self.win_.draw_line(line)
        
        if self.has_right_wall:
            line = Line(Point(x2_, y1_), Point(x2_, y2_))
            self.win_.draw_line(line)
        
        if self.has_top_wall:
            line = Line(Point(x1_, y2_), Point(x2_, y2_))
            self.win_.draw_line(line)

        if self.has_bottom_wall:
            line = Line(Point(x1_, y1_), Point(x2_, y1_))
            self.win_.draw_line(line)

    def draw_move(self, to_cell, undo=False):
        x1 = to_cell.x1_
        x2 = to_cell.x2_
        y1 = to_cell.y1_
        y2 = to_cell.y2_

        half_length = abs(self.x1_ - self.x2_) // 2
        x_center = half_length + self.x1_
        y_center = half_length + self.y1_

        half_length2 = abs(to_cell.x2_ - to_cell.x1_) // 2
        x_center2 = half_length2 + to_cell.x1_
        y_center2 = half_length2 + to_cell.y1_

        fill_color = "red"
        if undo:
            fill_color = "gray"

        line = Line(Point(x_center, y_center), Point(x_center2, y_center2))
        self.win_.draw_line(line, fill_color)
    

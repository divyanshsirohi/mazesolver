from graphics import *
from tkinter import Tk, BOTH, Canvas


class Cell:
    def __init__(self,window):
        self.has_left_wall = True;
        self.has_right_wall = True;
        self.has_top_wall = True;
        self.has_bottom_wall = True;
        self.x1_=-1
        self.y1_=-1
        self.x2_=-1
        self.y2_=-1
        self.win_=window
    
    def draw(self,x1,y1,x2,y2):
        x1_=x1
        y1_=y1
        y2_=y2
        x2_=x2

        if self.has_left_wall:
            line = Line(Point(x1, y1), Point(x1, y2))
            self.win_.draw_line(line)
        
        if self.has_right_wall:
            line = Line(Point(x2_,y1_),Point(x2_,y2_))
            self.win_.draw_line(line)
        
        if self.has_top_wall:
            line = Line(Point(x1_,y2_),Point(x2_,y2_))
            self.win_.draw_line(line)

        if self.has_bottom_wall:
            line = Line(Point(x1_,y1_),Point(x2_,y1_))
            self.win_.draw_line(line)

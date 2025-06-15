from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self,width,height):
        self.__root=Tk()
        self.__root.title("Maze Solver")
        self.__canvas = Canvas(self.__root, bg="white", height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
        print("window closed!")
    
    def draw_line(self,line,fill_color="black"):
        line.draw(self.__canvas, fill_color)
    def close(self):
        self.__running = False

class Point:
    
    def __init__(self,x,y):
        self.x_=x
        self.y_=y

class Line:
    
    def __init__(
            self,
            p1,
            p2
    ):
        self.p1_=p1
        self.p2_=p2
    
    def draw(self,canvas,fill_color):
        canvas.create_line(
            self.p1_.x_,self.p1_.y_,self.p2_.x_,self.p2_.y_,fill=fill_color,width=2
        )   





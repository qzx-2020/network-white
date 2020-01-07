import math
from tkinter import *

class Whiteboard:
    drawing_tool = ""
    # Colors = {'b': 'blue', 'r': 'red', 'g': 'green', 'o': 'orange', 'y': 'yellow', 'c': 'cyan', 'p': 'purple1',
    #           'd': 'black', 's': 'snow'}
    line_width =2

    def draw_Pencil(self,msgLst):#画线
        startX,startY,endX,endY = int(msgLst[1]),int(msgLst[2]),int(msgLst[3]),int(msgLst[4]),
        color = msgLst[5]
        self.drawing_area.create_line(startX,startY,endX,endY,fill=color,width =self.line_width)

    def draw_Rectangle(self, msgLst):#矩形
        startX, startY, endX, endY = int(msgLst[1]), int(msgLst[2]), int(msgLst[3]), int(msgLst[4])
        color = msgLst[5]
        self.drawing_area.create_rectangle(startX, startY, endX, endY, fill=color, width=0)

    def draw_Line(self, msgLst):#直线
        startX, startY, endX, endY = int(msgLst[1]), int(msgLst[2]), int(msgLst[3]), int(msgLst[4])
        color = msgLst[5]
        self.drawing_area.create_line(startX, startY, endX, endY, fill=color, width=0)

    def draw_Square(self, msgLst):#正方形
        startX, startY, endX, endY = int(msgLst[1]), int(msgLst[2]), int(msgLst[3]), int(msgLst[4])
        color = msgLst[5]
        edge_size = ((endX - startX) + (endY - startY)) / 2
        self.drawing_area.create_rectangle(startX, startY, startX + edge_size, startY + edge_size, fill=color, width=0)

    def draw_Oval(self, msgLst):#椭圆
        startX, startY, endX, endY = int(msgLst[1]), int(msgLst[2]), int(msgLst[3]), int(msgLst[4])
        color = msgLst[5]
        self.drawing_area.create_oval(startX, startY, endX, endY , fill=color, width=0)

    def draw_Circle(self, msgLst):#圆
        startX, startY, endX, endY = int(msgLst[1]), int(msgLst[2]), int(msgLst[3]), int(msgLst[4])
        color = msgLst[5]
        The_contre_X = (startX + endX)/2
        The_contre_Y = (startY + endY)/2
        The_radius =math.math.sqrt((endX - startX)**2 + (endY - startY)**2) / 2
        self.drawing_area.create_oval(The_contre_X - The_radius, The_contre_Y -The_radius,
                                      The_contre_X +The_radius, The_contre_Y+The_radius , fill=color, width=0)

    def draw_from_msg(self,msg):#接收画图类型
        msgLst = msg.split()
        draw_type =msgLst[0]
        if draw_type == 'D':
            self.draw_Pencil(msgLst)
        if draw_type == 'R':
            self.draw_Rectangle(msgLst)
        if draw_type == 'L':
            self.draw_Line(msgLst)
        if draw_type == 'S':
            self.draw_Square(msgLst)
        if draw_type == 'O':
            self.draw_Oval(msgLst)
        if draw_type == 'C':
            self.draw_Circle(msgLst)
        else:
            pass



    def __init__(self):
        self.init_whiteboard()
        self._init_item_button()
        self._init_color_button()
        self.init_drawing_area()
        self.color = 'b'


    def show_window(self):
        self.myWhiteBoard.mainloop()

    def init_drawing_area(self):
        self.drawing_area = Canvas(self.myWhiteBoard,width =1000,heigh =700,bg ='white')
        self.drawing_area.place(y=50)

    def init_whiteboard(self):
        self.myWhiteBoard = Tk()
        self.myWhiteBoard.geometry('1280x720')


    def set_drawing_tool(self,tool):
        Whiteboard.drawing_tool = tool
        print(tool)

    def set_color(self, color):
        print(color)
        self.color = color


    def _init_item_button(self):
        Button(self.myWhiteBoard, text='line', height=1, width=5, bg='dark goldenrod', font='Arial',
               command=lambda: self.set_drawing_tool('line')).place(x=70, y=0)
        Button(self.myWhiteBoard, text='rect', height=1, width=5, bg='saddle brown', font='Arial',
               command=lambda: self.set_drawing_tool('rectangle')).place(x=140, y=0)
        Button(self.myWhiteBoard, text='oval', height=1, width=5, bg='NavajoWhite4', font='Arial',
               command=lambda: self.set_drawing_tool('oval')).place(x=210, y=0)
        # Button(self.myWhiteBoard, text='text', height=1, width=5, bg='SteelBlue4', font='Arial',
        #        command=self.get_text_from_user).place(x=280, y=0)
        Button(self.myWhiteBoard, text='pencil', height=1, width=5, bg='DeepSkyBlue2', font='Arial',
               command=lambda: self.set_drawing_tool('pencil')).place(x=350, y=0)
        Button(self.myWhiteBoard, text='circle', height=1, width=5, bg='Turquoise2', font='Arial',
               command=lambda: self.set_drawing_tool('circle')).place(x=420, y=0)
        Button(self.myWhiteBoard, text='square', height=1, width=5, bg='CadetBlue1', font='Arial',
               command=lambda: self.set_drawing_tool('square')).place(x=490, y=0)
        Button(self.myWhiteBoard, text='eraser', height=1, width=5, bg='purple1', font='Arial',
               command=lambda: self.set_drawing_tool('eraser')).place(x=560, y=0)
        Button(self.myWhiteBoard, text='drag', height=1, width=5, bg='green', font='Arial',
               command=lambda: self.set_drawing_tool('drag')).place(x=630, y=0)

    def _init_color_button(self):
        Button(self.myWhiteBoard, height=1, width=5, bg='red',
               command=lambda: self.set_color('r')).place(x=1010, y=50)
        Button(self.myWhiteBoard, height=1, width=5, bg='orange',
               command=lambda: self.set_color('o')).place(x=1010, y=100)
        Button(self.myWhiteBoard, height=1, width=5, bg='yellow',
               command=lambda: self.set_color('y')).place(x=1010, y=150)
        Button(self.myWhiteBoard, height=1, width=5, bg='green',
               command=lambda: self.set_color('g')).place(x=1010, y=200)
        Button(self.myWhiteBoard, height=1, width=5, bg='cyan',
               command=lambda: self.set_color('c')).place(x=1010, y=250)
        Button(self.myWhiteBoard, height=1, width=5, bg='blue',
               command=lambda: self.set_color('b')).place(x=1010, y=300)
        Button(self.myWhiteBoard, height=1, width=5, bg='purple1',
               command=lambda: self.set_color('p')).place(x=1010, y=350)
        Button(self.myWhiteBoard, height=1, width=5, bg='black',
               command=lambda: self.set_color('d')).place(x=1010, y=400)
        Button(self.myWhiteBoard, height=1, width=5, bg='snow',
               command=lambda: self.set_color('s')).place(x=1010, y=450)







if __name__ == '__main__':
    wb =Whiteboard()
from threading import Thread

from connection import Connection
from whiteboard import Whiteboard

class Client(Thread,Whiteboard):

    def __init__(self):
        self.conn = Connection()
        Thread.__init__(self)
        Whiteboard.__init__(self)
        self._init_mouse_event(self)
        self.setDaemon(True) #守护线程
        self.isMouseDown = False
        self.x_pos=None
        self.y_pos=None


    def _init_mouse_event(self):
        self.drawing_area.bind("<Motion>", self.motion)
        self.drawing_area.bind("<ButtonPress-1>", self.left_but_down)
        self.drawing_area.bind("<ButtonRelease-1>", self.left_but_up)

    #(type,startx,starty,endx,endy,color)
    #('D',startx,starty,endx,endy,'red')

    def left_but_down(self,event=None):
        self.isMouseDown = True
        # print(event.x,event.y)
        self.x_pos = event.x
        self.y_pos = event.y

    def left_but_up(self,event=None):
        self.isMouseDown = False
        print(event.x,event.y)

    def motion(self, event=None):
        if self.isMouseDown == True:
            msg = ('D',self.x_pos,self.y_pos,event.x,event.y,'red')
            self.x_pos=event.x
            self.y_pos=event.y
        print(event.x, event.y)




    def run(self):
        print("run")
        while True:
            msg = self.conn.receive_msg()
            if msg == '...':
                pass
    #wait

if __name__ == '__main__':
    client = Client()
    client.start()
    client.show_window()
from tkinter import *


class UserDialog:
    _Ip = ''
    _port = 0
    _nickname = ''
    def __init__(self):
        pass
    @classmethod
    def show_error_box(cls,msg):
        master = Tk()
        Label(master,text = msg).grid(row =0)
        Button(master,text ='ok',command =master.destroy()).grid(row =1,pady =4)
        master.mainloop()

    @classmethod
    def getUserInputIP(cls):
        ClientWindow = Tk()

        def getUserIPAndPort():
            print('getUserIPAndPort')
            cls._Ip = e1.get()
            cls._port =int(e2.get())
            ClientWindow.destroy()


        Label(ClientWindow,text = '请输入id及port').grid(row = 0)
        Label(ClientWindow, text='id').grid(row = 1)
        Label(ClientWindow, text='port').grid(row=2)

        e1 = Entry(ClientWindow)
        e2 = Entry(ClientWindow)

        e1.grid(row = 1,column =1)
        e2.grid(row = 2,column =1)

        buttom = Button(ClientWindow)
        buttom.grid(row =3,column =1)
        buttom.config(text ='ok',command = getUserIPAndPort)

        ClientWindow.mainloop()


    @classmethod
    def getUserNickName(cls):
        def getUserNickNameInner():
            cls._nickname = e1.get()

            ClentWindow.destroy()
        ClentWindow = Tk()
        Label(ClentWindow,text ='请输入昵称').grid(row =0)
        Label(ClentWindow, text='昵称').grid(row=1)

        e1 = Entry(ClentWindow)
        e1.grid(row =1,column =1)

        buttom = Button(ClentWindow)
        buttom.grid(row =2,column =1)
        buttom.config(text ='ok',command =getUserNickNameInner)

        ClentWindow.mainloop()

if __name__ == '__main__':
    UserDialog.getUserInputIP()
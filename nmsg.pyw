
from tkinter import *
from time import sleep 
from subprocess import call

class link_support_gui():

    def __init__(self, master):
        
        try:
            self.master = master
            self.hostname_ = Entry(self.master, width=30, bd=3)
            self.hostname_.grid(row=1, column=1, pady=(30,0))
            self.msg_ = Entry(self.master, width=30,bd=3)
            self.msg_.grid(row=2, column=1)

            self.master.title("Network message")
            self.master.minsize(width=100, height=100)
            self.master.iconbitmap(default='united.ico')
            gui_title = 'United Airlines'
            united_color = '#00349A'
            united_color_background = '#FFFFFF'
            Message(self.master, width=200, text='Send message over the network', bg=united_color, fg='white').grid(row=0, column=1, ipadx=200, ipady=8)
            Label(self.master, text="Hostname", height=2).grid(row=1, column=1, sticky=W, pady=(30,0))
            Label(self.master, text="Message", height=2).grid(row=2, column=1, sticky=W)
            Button(self.master, text='SEND MESSAGE', width=15, bd=3, command=self.start_script).grid(row=6, column=1, ipadx=15, ipady=5, pady=(25,30))
        except:
            quit()


    def start_script(self):    # Test Entrys and checkboxes
        try:
            _1 = self.hostname_.get()
            _2 = self.msg_.get()

            call('msg * ' + '/server:' + str(_1) + ' /v /w /time:600 ' + str(_2))
            self.master.destroy()
        except:
            quit()

if __name__ == "__main__":

    root = Tk()
    my_gui = link_support_gui(root)
    root.mainloop()

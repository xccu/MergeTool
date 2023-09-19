#GUI扩展
from tkinter import *
from tkinter import ttk

def get_value(key,kw):
    if key in kw.keys():
        return kw[key]
    else:
        return None

#label控件，宽高单位：像素
class Label_PX():
    def __init__(self,root,**kw):
        self.width = get_value("width",kw)
        self.height = get_value("height",kw)

        if self.width is None : self.width=80
        if self.height is None : self.height=30

        self.frame = Frame(root)
        self.frame["width"] = self.width
        self.frame["height"] = self.height
        self.frame["bg"] = get_value("bg",kw)
        self.frame.pack_propagate(0)

        self.label = Label(self.frame)
        self.label["text"] = get_value("text",kw)
        self.label["bg"] = get_value("bg",kw)
        self.label["fg"] = get_value("fg",kw)
        self.label["font"] = get_value("font",kw)
        self.label["background"] =  get_value("background",kw)
        self.label.pack()

    def place(self,x,y):
         self.frame.place(x=x,y=y)

#text控件，宽高单位：像素
class Text_PX():
    def __init__(self,root,**kw):
        self.width = get_value("width",kw)
        self.height = get_value("height",kw)

        if self.width is None : self.width=80
        if self.height is None : self.height=30
        self.bd = int(get_value("bd",kw))

        #根Frame
        self.r_frame = Frame(root)
        self.r_frame["width"] = self.width
        self.r_frame["height"] = self.height
        self.r_frame["bg"] = get_value("bdcolor",kw)

        #子Frame
        self.frame = Frame(self.r_frame)
        self.frame["width"] = self.width-self.bd*2
        self.frame["height"] = self.height-self.bd*2
        self.frame["bg"] = get_value("bg",kw)
        self.frame.place(x=self.bd,y=self.bd)
        self.frame.pack_propagate(0)

        self.text = Text(self.frame)
        self.text["bd"] =0
        self.text["relief"] = get_value("relief",kw)
        self.text["background"] =  get_value("background",kw)
        self.text["width"] = self.width-self.bd*2
        self.text["height"] = self.height-self.bd*2
        self.text["bg"] = get_value("bg",kw)
        self.text["fg"] = get_value("fg",kw)
        self.text["font"] = get_value("font",kw)
        self.text.pack()

    def place(self,x,y):
         self.r_frame.place(x=x,y=y)
    
    def insert(self, index, chars, *args):
        self.text.insert(index, chars, *args)
    
    def delete(self, index1, index2=None):
        self.text.delete(index1, index2)

#button控件，宽高单位：像素
class Button_PX():
    def __init__(self,root,**kw):
        self.kw = kw
        self.width = get_value("width",kw)
        self.height = get_value("height",kw)
        self.img_path = get_value("image",kw)
        self.bd = get_value("bd",kw)

        if self.img_path is None:
            self.img = None
        else:
            self.img = PhotoImage(file=self.img_path)
            self.img.width=25
            self.img.height=25

        if self.width is None : self.width=80
        if self.height is None : self.height=25


        #根Frame
        self.r_frame = Frame(root)
        self.r_frame["width"] = self.width
        self.r_frame["height"] = self.height
        self.r_frame["bg"] = get_value("bdcolor",kw)

        #子Frame
        self.frame = Frame(self.r_frame)
        self.frame["width"] = self.width-self.bd*2
        self.frame["height"] = self.height-self.bd*2
        self.frame["bg"] = get_value("bg",kw)
        self.frame.place(x=self.bd,y=self.bd)
        self.frame.pack_propagate(0)

        self.button = Button(self.frame)
        self.button["relief"] = get_value("relief",kw)
        self.button["text"] =get_value("text",kw)
        self.button["width"] = self.width
        self.button["height"] = self.height
        self.button["image"] = self.img
        self.button["bd"] = 0
        self.button["bg"] = get_value("bg",kw)
        self.button["fg"] = get_value("fg",kw)
        self.button["font"] = get_value("font",kw)
        self.button["command"] = get_value("command",kw)
        self.button["compound"]=get_value("compound",kw)
        self.button["background"]=get_value("background",kw)
        self.button["activebackground"]=get_value("activebackground",kw)
        self.button.bind("<Enter>", self.on_enter)
        self.button.bind("<Leave>", self.on_leave)
        self.button.pack()

    def place(self,x,y):
         self.r_frame.place(x=x,y=y)

    def on_enter(self,e):
        self.button['background'] = get_value("enterBg",self.kw)

    def on_leave(self,e):
        self.button['background'] = get_value("leaveBg",self.kw)


#ListBox控件，宽高单位：像素
class Listbox_PX():
    def __init__(self,root,**kw):
        self.kw = kw
        self.width = get_value("width",kw)
        self.height = get_value("height",kw)
        self.bd = get_value("bd",kw)

        if self.width is None : self.width=80
        if self.height is None : self.height=25

        #根Frame
        self.r_frame = Frame(root)
        self.r_frame["width"] = self.width
        self.r_frame["height"] = self.height
        self.r_frame["bg"] = get_value("bdcolor",kw)

        #子Frame
        self.frame = Frame(self.r_frame)
        self.frame["width"] = self.width-self.bd*2
        self.frame["height"] = self.height-self.bd*2
        self.frame["bg"] = get_value("bg",kw)
        self.frame.place(x=self.bd,y=self.bd)
        self.frame.pack_propagate(0)

        self.control = Listbox(self.frame)
        self.control["relief"] = get_value("relief",kw)
        self.control["text"] =get_value("text",kw)
        self.control["width"] = self.width
        self.control["height"] = self.height
        self.control["image"] = self.img
        self.control["bd"] = 0
        self.control["bg"] = get_value("bg",kw)
        self.control["fg"] = get_value("fg",kw)
        self.control["font"] = get_value("font",kw)
        self.control["command"] = get_value("command",kw)
        self.control["compound"]=get_value("compound",kw)
        self.control["background"]=get_value("background",kw)
        self.control["activebackground"]=get_value("activebackground",kw)
        self.control.bind("<Enter>", self.on_enter)
        self.control.bind("<Leave>", self.on_leave)
        self.control.pack()

    def place(self,x,y):
         self.r_frame.place(x=x,y=y)

    def on_enter(self,e):
        self.control['background'] = get_value("enterBg",self.kw)

    def on_leave(self,e):
        self.control['background'] = get_value("leaveBg",self.kw)
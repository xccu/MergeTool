# encoding: utf-8
#GUI扩展
from tkinter import *

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

        self.frame = Frame(root)
        self.frame["width"] = self.width
        self.frame["height"] = self.height
        self.frame["bg"] = get_value("bg",kw)
        self.frame.pack_propagate(0)

        self.text = Text(self.frame)
        self.text["width"] = self.width
        self.text["height"] = self.height
        self.text["bg"] = get_value("bg",kw)
        self.text["fg"] = get_value("fg",kw)
        self.text["font"] = get_value("font",kw)
        self.text.pack()

    def place(self,x,y):
         self.frame.place(x=x,y=y)
    
    def insert(self, index, chars, *args):
        self.text.insert(index, chars, *args)
    
    def delete(self, index1, index2=None):
        self.text.delete(index1, index2)
    
    def get(self,index1, index2=None):
        return self.text.get(index1, index2)

#button控件，宽高单位：像素
class Button_PX():
    def __init__(self,root,**kw):
        self.width = get_value("width",kw)
        self.height = get_value("height",kw)
        self.img_path = get_value("image",kw)

        if self.img_path is None:
            self.img = None
        else:
            self.img = PhotoImage(file=self.img_path)
            self.img.width=25
            self.img.height=25

        if self.width is None : self.width=80
        if self.height is None : self.height=25

        self.frame = Frame(root)
        self.frame["width"] = self.width
        self.frame["height"] = self.height
        self.frame["bg"] = get_value("bg",kw)
        self.frame.pack_propagate(0)

        self.button = Button(self.frame)
        
        self.button["relief"] = get_value("relief",kw)
        self.button["text"] =get_value("text",kw)
        self.button["width"] = self.width
        self.button["height"] = self.height
        self.button["image"] = self.img
        self.button["bd"] = get_value("bd",kw)
        self.button["bg"] = get_value("bg",kw)
        self.button["fg"] = get_value("fg",kw)
        self.button["font"] = get_value("font",kw)
        self.button["command"] = get_value("command",kw)
        self.button["font"] = get_value("font",kw)
        self.button.pack()

    def place(self,x,y):
         self.frame.place(x=x,y=y)

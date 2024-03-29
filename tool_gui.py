# encoding: utf-8
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tool_gui_expand import *
from tool_service import *
from tool_setting_gui import *
import _thread
import os


class Init_Window():
    
    #构造函数
    def __init__(self,window):
        self.window = window   
        self.index = 0

        self.curPath = os.path.abspath(os.path.dirname(__file__)) #项目所在文件夹
        self.temp_path = self.curPath+'\\temp\\'   #临时文件夹
        self.output_path= self.curPath+'\\output\\' #导出文件夹
        
        self.folder=''

        #self.file_service= File_Service(self.bar_callback)
        self.file_service= File_Service()
        self.merge_service = Merge_Service(self.curPath+'\\output\\')
        self.enable=True

    #初始化
    def init(self):


        #样式字典  #00ABFF -> #31B4E5
        btn_styles = {
            'width':80,'height':23,'bd': 0,
            'background': "#31B4E5","enterBg":"#4D4D4D","fg":"white" ,
            "leaveBg":"#31B4E5","activebackground":"#7689ED"
        }
        btn_out_styles = {'relief': "solid",'bd': 0,'bdcolor':"#BCBCBC","background":"#31B4E5","enterBg":"#4D4D4D","fg":"white","leaveBg":"#31B4E5","activebackground":"#7689ED",}
        text_styles = {'bd':1,'bdcolor':"#BCBCBC"}

        label_styles = {'bdcolor':"#BCBCBC",'background':'#090B0C'}

        #设置窗体title
        self.window.title('文件合并工具')
        #设置窗体宽高
        self.window.geometry("800x450")
        #self.window.grid(width=80, height=50)

        #固定宽高，防止用户调整尺寸
        self.window.resizable(0,0) 

        # #F2F2F2 -> #090B0C
        self.container = Frame(self.window, width=800, height=430,background="#090B0C")
        self.container.pack()

        #self.head_frame = Frame(self.container, width=800, height=30,background="#4D4D4D")
        #self.head_frame.place(x=0,y=0)
        
        # #FFFFFF -> #282828
        self.cmd_frame = Frame(self.container, width=385, height=70,background="#282828")
        self.cmd_frame.place(x=10,y=10)

        self.setting_frame = Frame(self.container, width=385, height=70,background="#282828")
        self.setting_frame.place(x=405,y=10)

        #self.container.grid_propagate(False)

        #导出列表按钮
        self.export_list_button = Button_PX(self.cmd_frame, text="导出列表", **btn_styles, command=self.export_list_click)  
        self.export_list_button.place(x=10,y=10)

        #导入列表按钮
        self.import_list_button = Button_PX(self.cmd_frame, text="导入列表", **btn_styles,command=self.import_list_click)  
        self.import_list_button.place(x=100,y=10)

        #清空列表按钮
        self.clear_list_button = Button_PX(self.cmd_frame, text="清空列表", **btn_styles,command=self.clear_list_click)  
        self.clear_list_button.place(x=190,y=10)

        #合并按钮
        self.merge_button = Button_PX(self.cmd_frame, text="合并", **btn_styles,command=self.merge_click)  
        self.merge_button.place(x=280,y=10)

        #设置按钮
        #self.setting_button = Button_PX(self.cmd_frame, text="设置", **btn_styles,command = self.setting_click) 
        #self.setting_button.place(x=460,y=10)

        #上移按钮
        self.up_button = Button_PX(self.cmd_frame, text="向上", **btn_styles,command=self.up_item_click)  
        self.up_button.place(x=10,y=40)

        #下移按钮
        self.down_button = Button_PX(self.cmd_frame, text="向下", **btn_styles,command=self.down_item_click)  
        self.down_button.place(x=100,y=40)

        #选择文件按钮
        self.add_item_button = Button_PX(self.cmd_frame, text="添加", **btn_styles,command=self.add_item_click) 
        self.add_item_button.place(x=190,y=40)

        #删除按钮
        self.remove_item_button = Button_PX(self.cmd_frame, text="移除", **btn_styles,command=self.remove_item_click) 
        self.remove_item_button.place(x=280,y=40)

        #导出文件夹标签
        self.init_Label = Label_PX(self.container,text="导出文件名", width = 80,height=25)
        self.init_Label.place(x=5,y=100)

        #导出文件路径文本框
        self.export_Text = Text_PX(self.container, width=610, height=25,**text_styles)
        self.export_Text.place(x=80,y=100)
        #self.export_Text.insert(1.0,self.output_path)

        #打开导出文件路径按钮
        self.export_open_button = Button_PX(self.container, text="打开",**btn_styles,command=self.export_open_click)  
        self.export_open_button.place(x=700,y=100)

        #创建列表组件
        self.file_Listbox  = Listbox(self.container,height=15,width=110,selectmode = "single")  
        self.file_Listbox.bind('<<ListboxSelect>>',self.listbox_select)
        self.file_Listbox.place(x=10,y=130)

        #底部状态栏:信息 
        self.status_bar = Label(self.window, text="就绪", bd=1, relief=SUNKEN,anchor=W,width=100)
        self.status_bar.pack(side=LEFT)

        #底部状态栏:计数 
        self.status_count_bar = Label(self.window, text="", bd=1, relief=SUNKEN,anchor=W)
        self.status_count_bar.pack(side=BOTTOM, fill=X)

        #设置进度条回调函数
        #self.encryptor.progress_func=self.progress_callback
    
    #打开文件函数
    def add_item_click(self):
        # 选择文件
        file_list =filedialog.askopenfilenames()
        #文件列表写入给file_Listbox控件
        for file in file_list:   
            self.file_Listbox.insert(END,file)

    #删除选项函数
    def remove_item_click(self):
        self.file_Listbox.delete(ACTIVE)

    #选项上移函数
    def up_item_click(self):
        # 获取选中的列表值
        a = self.file_Listbox.get(ACTIVE)   
        # 获取选择值在列表中的位置    
        p = self.index - 1                      
        
        #元组转list
        path_list = list(self.file_Listbox.get(0,END)) 
        if p == -1:
            return
        else:  # 如果位置不等于-1
            # 列表中插入位置p，值为选择的值
            path_list.insert(p, a)  
            # 删除掉原位置的值
            del path_list[p + 2]  
            # 清空列表框
            self.file_Listbox.delete(0, END)  
        for item in path_list:  # 循环列表
            # 列表框最后插入值
            self.file_Listbox.insert(END, item)  
            
        self.index = self.index-1
        self.file_Listbox.select_set(self.index)
        self.file_Listbox.activate(self.index)
        print(self.index)

    #选项下移函数
    def down_item_click(self):
        a = self.file_Listbox.get(ACTIVE)
        p = self.index + 2
        path_list = list(self.file_Listbox.get(0,END)) #元组转list
        if p == len(path_list)+1:
            return
        
        path_list.insert(p, a)
        del path_list[p - 2]
        self.file_Listbox.delete(0, END)
        for item in path_list:
            self.file_Listbox.insert(END, item)

        self.index = self.index+1
        self.file_Listbox.select_set(self.index)
        self.file_Listbox.activate(self.index)
        print(self.index)

    #打开设置窗口函数
    def setting_click(self):        
        self.sub_Window =Setting_Window(Toplevel())
        self.sub_Window.init()

    #打开导出目录函数
    def export_open_click(self):
        path = self.output_path #self.export_Text.get("1.0","end")  
        start_directory = r'D:\testdir'
        print(start_directory)
        print(path)
        os.system("explorer.exe %s" % path)
           
    #合并函数
    def merge_click(self):
        _thread.start_new_thread(self.merge_thread,())

    
    #合并线程函数
    def merge_thread(self):
        self.path_list = self.file_Listbox.get(0,END)
        files= []
        i=1
        for file in self.path_list:  
            if file=='':
                continue
            if not(self.folder == ''):
                file =  '{0}\\{1}'.format(self.folder,file)
            print('file:'+file) 
            self.status_bar["text"] = '读取文件：{0}'.format(file)         
            expand_name = self.file_service.get_file_expand_name(file)
            target_file = '{0}{1}{2}'.format(self.temp_path,i,expand_name)  
            i+=1
            files.append(target_file)
            self.file_service.copy_file(file,target_file)

        #获取导出文件名，若为空则设为默认名称：YYYYmmddHHMMSS.ts
        fileName = self.export_Text.text.get("1.0","end")  
        if len(fileName) == 0 or fileName =='\n':
            fileName =  datetime.datetime.strftime(datetime.datetime.now(),'%Y%m%d%H%M%S')+'.ts'

        self.status_bar["text"] = '生成文件：{0}'.format(fileName.rstrip())             
        self.merge_service.merge(files,fileName)
        self.file_service.delete_file(self.temp_path)


    #导出列表按钮响应函数
    def export_list_click(self):
        # 选择文件夹
        export_path = filedialog.askdirectory()
        export_list = self.file_Listbox.get(0,END)
        data=''
        for file in export_list:  
            data += file.split('/')[-1]+'\n'
        self.file_service.write(export_path+'/test.li',data)

    #导入列表按钮响应函数
    def import_list_click(self):
        # 选择文件
        path =filedialog.askopenfilename()
        self.folder= os.path.split(path)[0].replace('/','\\')  
        print(self.folder)     
        files = self.file_service.read(path)
        file_list = files.split('\n')
        self.file_Listbox.delete(0,END)
        for file in file_list:  
            if file=='':
                continue 
            self.file_Listbox.insert(END,file)

    #清空列表按钮响应函数
    def clear_list_click(self):
        self.file_Listbox.delete(0,END)

    #选中当前项函数
    def listbox_select(self,evt):
        w = evt.widget
        value = w.get(w.curselection())
        print(w.curselection()[0])
        self.index = w.curselection()[0]
        print(value)
    
    #进度条回调函数
    def bar_callback_thread(self,data):
        self.status_bar["text"]=data
    
    def bar_callback(self,data):
        _thread.start_new_thread(self.bar_callback_thread,(data))
        



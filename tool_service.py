# encoding: utf-8
import os
import os.path 
import shutil
import datetime

class File_Service():
    def __init__(self,callback=None):
        self.file_list =[]

        #回调函数
        if callback==None:
            self.print_func = self.default_print
        else:
            self.print_func = callback

    #默认输出函数
    def default_print(self,data):
        print(str(data))

    def get_file_expand_name(self,file_name):
        return os.path.splitext(file_name)[1] 

    def copy_file(self,source_file,target_file):
        #print(source_file+' to '+target_file)
        shutil.copyfile(source_file, target_file)

    def create_dir_not_exist(self,path):
        if not os.path.exists(path):
            os.mkdir(path)
    
    def delete_file(self,path):
        for i in os.listdir(path) :# os.listdir(path)#返回一个列表，里面是当前目录下面的所有东西的相对路径
            file_data = path + i#当前文件夹的下面的所有东西的绝对路径
            if os.path.isfile(file_data) == True:#os.path.isfile判断是否为文件,如果是文件,就删除.如果是文件夹.递归给del_file.
                os.remove(file_data)
                self.print_func('删除临时文件'+file_data)
            else:
                self.delete_file(file_data)

    #读文件
    def read(self,filePath):
        try:
            f = open(filePath, 'r')
            result = f.read()
            return result
        except Exception as ex:
            self.print_func(ex)
        finally:
            if f:
                f.close()
            
    #写文件
    def write(self,filePath,data):
        try:
            f = open(filePath, 'w')
            f.write(data)
            #f.write(bytes)
        except Exception as ex:
            self.print_func(ex)
        finally:
            if f:
                f.close()




class Merge_Service():
    def __init__(self,output_path,callback=None):
        self.output_path = output_path
        #回调函数
        if callback==None:
            self.print_func = self.default_print
        else:
            self.print_func = callback

    #默认输出函数
    def default_print(self,data):
        print(str(data))
    
    def merge(self,pathlist,fileName):       
        self.print_func(pathlist)
        #os.chdir("ts/")
        os.chdir(self.output_path)
        self.shell_str = '+'.join(pathlist)
        self.shell_str = self.shell_str.replace('/','\\')
        self.print_func("cmd")
        self.shell_str = 'copy /b '+ self.shell_str + ' ' + fileName #该命令不支持中文
        os.system(self.shell_str)
        self.print_func(self.shell_str)
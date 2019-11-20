"""
直接在文件中使用的代码
在本地位置创建目录
注意：-我使用过python包，所以如果您想
在项目的主目录中创建使用
函数中的pardir +“ \\” + name
所有文件夹操作均在家中完成
项目目录。
"""
__author__ = 'iByte'
__version__ = '1.0'

from os import chdir
from os import makedirs
from os import removedirs
from os import rename
from os.path import exists
from os.path import pardir
from shutil import copytree
from shutil import move


# 创建文件夹
def create_directory(name):
    if exists(pardir + "\\" + name):
        print('Folder already exists... Cannot Overwrite this')
    else:
        makedirs(pardir + "\\" + name)


# 删除文件夹
def delete_directory(name):
    removedirs(name)


# 重命名文件夹
def rename_directory(direct, name):
    rename(direct, name)


# 设置工作目录
def set_working_directory():
    chdir(pardir)


# 备份文件夹树
def backup_files(name_dir, folder):
    copytree(pardir, name_dir + ':\\' + folder)


# 将文件夹移到特定位置
# 覆盖文件（如果已存在）
def move_folder(filename, name_dir, folder):
    if not exists(name_dir + ":\\" + folder):
        makedirs(name_dir + ':\\' + folder)
    move(filename, name_dir + ":\\" + folder + '\\')


"""
For test purpose:
    1. create_directory("test")
    2. rename_directory("test","demo")
    3. delete_directory("demo")
    4. backup_files('D', 'backup_project')
    5. move_folder(pardir+'\\'+'test.txt', 'D', 'name')
"""
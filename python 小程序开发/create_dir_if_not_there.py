# 检查用户主目录中是否存在目录，如果不存在，则创建它

import os

MESSAGE = 'The directory already exists.'
TESTDIR = 'testdir'
try:
    home = os.path.expanduser("~")  # 通过展开用户的设置主目录来设置变量主目录
    print(home)  # 打印位置

    if not os.path.exists(os.path.join(home, TESTDIR)):  # os.path.join（）用于安全地建立完整路径
        os.makedirs(os.path.join(home, TESTDIR))  # 如果不创建目录，则在其主目录内
    else:
        print(MESSAGE)
except Exception as e:
    print(e)
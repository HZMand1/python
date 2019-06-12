# coding: utf-8
from __future__ import unicode_literals
from wxpy import *

# bot = Bot('bot.pkl')
# my_friend = bot.friends().search('iByte')[0]
# my_friend.send('测试发送消息')

# 日志告警这里有三个参数 %{type} %{path} %{message}，可根据自己的日志自行配置参数
if len(sys.argv) == 4:
    bot = Bot('bot.pkl')
    alarm_group = bot.groups().search('服务器报警小助手')[0]
    message = "项目名：{type}, 日志路径 {path}，详细信息 {message}".format(type=sys.argv[1], path=sys.argv[2], message=sys.argv[3])
    alarm_group.send(message)


# coding: utf-8
from __future__ import unicode_literals
from threading import Timer
from wxpy import *

bot = Bot('bot.pkl')
my_friend = bot.friends().search("iByte")[0]


def send_message():
    try:
        my_friend.send(u"你到家了么！")
        t = Timer(86400, send_message)
        t.start()
    except:
        my_friend.send(u"今天消息发送失败了")


@bot.register(my_friend)
def reply_my_friend(msg):
    print(11)
    print(msg.text, msg.sender)


if __name__ == "__main__":
    send_message()

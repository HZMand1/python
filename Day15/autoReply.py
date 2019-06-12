# 收到某个人的消息之后，自动回复，并播放声音提示
from wxpy import *
import winsound

bot = Bot()
my_friend = bot.friends().search("iByte")[0]


@bot.register(my_friend)
def reply_my_friend(msg):
    print(11)
    print(msg.text, msg.sender)
    winsound.MessageBeep(winsound.MB_ICONHAND)


bot.join()





""" 欢迎关注 "码农架构" 微信公众号，热爱开源，拥抱开源。一个IT民工的技术之路经验分享。
    - 问题咨询 / 建议
    1.关注微信公众号 "码农架构" 后私信
    2.可发送邮件: li.shangzhi@aliyun.com
"""
# coding: utf-8
from __future__ import unicode_literals
from wxpy import *
from wechat_sender import listen
bot = Bot('bot.pkl')
listen(bot)



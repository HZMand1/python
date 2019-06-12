""" 欢迎关注 "码农架构" 微信公众号，热爱开源，拥抱开源。一个IT民工的技术之路经验分享。
    - 问题咨询 / 建议
    1.关注微信公众号 "码农架构" 后私信
    2.可发送邮件: li.shangzhi@aliyun.com
"""
# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/12 15:24
# @Author  : iByte

# coding=utf-8
import random
import urllib.request
import time
from lxml import etree

url = "http://www.xicidaili.com/"
header_list = [
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)',
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1",
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
    "Opera/9.80 (Windows NT 6.1; U; zh-cn) Presto/2.9.168 Version/11.50"
]
'''随机选择一个user-agent 与下面拼接'''
header_one = random.choice(header_list)

header = {
    'User-Agent': header_one,
}
'''最好先进入西刺网站，然后copy 一个ip 地址。如果使用自己的ip 小心被封！！'''
httpproxy_handler = urllib.request.ProxyHandler({"HTTPS": "60.177.229.9:18118"})

opener = urllib.request.build_opener(httpproxy_handler)
request = urllib.request.Request(url, headers=header)
urllib.request.install_opener(opener)
data = urllib.request.urlopen(request).read()

content = etree.HTML(data)
url_list = content.xpath('//tr/td[2]/text()')  # 解析地址
port = content.xpath('//tr/td[3]/text()')  # 解析端口号
text = content.xpath('//td[6]/text()')  # 解析地址类型！

d = list()
li = list()
dir = dict()
for i in range(50, len(url_list)):
    li.append(url_list[i] + ":" + port[i])

for j in range(len(url_list)):
    d.append(text[j])

for i in range(1,len(url_list)): #第一个url 开始！
    # print({text[i]: li[i]})
    '''每次的地址进行提取！'''
    httpproxy_handler = urllib.request.ProxyHandler({text[i]: li[i]})

    url_list = [
        '''这是放置url的地方！'''
    ]

    list = [
        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)',
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1",
        'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
        "Opera/9.80 (Windows NT 6.1; U; zh-cn) Presto/2.9.168 Version/11.50"
    ]

    while True:
        # 通过 urllib2.build_opener()方法使用这些代理Handler对象，创建自定义opener对象
        header_one = random.choice(list)
        url_one = random.choice(url_list)
        header = {
            'User-Agent': header_one,
        }
        opener = urllib.request.build_opener(httpproxy_handler)
        print(str({text[i]: li[i]}) + "\t" + str(url_one) + "\t" + str(header_one) + "正在读取！")
        request = urllib.request.Request(url_one, headers=header)
        time.sleep(10)
        urllib.request.install_opener(opener)
        response = urllib.request.urlopen(request).read()
        print("结束！")
        break
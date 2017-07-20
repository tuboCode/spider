#!/usr/bin/env python

import re
from urllib.request import urlopen
from bs4 import BeautifulSoup

# 请求url并把结果用utf-8编码
# 一个响应的对象
# resp = urlopen("https://en.wikipedia.org/wiki/Main_Page").read().decode("utf-8")
resp = urlopen("http://www.yangtzeu.edu.cn/").read().decode("utf-8")

#使用BeautifulSoupj解析 用soup 指定一个解析器
soup = BeautifulSoup(resp, 'html.parser')
# list_urls = soup.findAll("a", href=re.compile("^/wiki/"))
list_urls = soup.findAll("a", href=re.compile("^http://news.yangtzeu.edu.cn/"))

# 获取所有一/wiki/开头的a的标签的href 属性
for url in list_urls:
    # 过滤--.jpg或.JPG结尾的url
    if not re.search("\.(jpg|JPG)$", url["href"]):
        # 输出所有的url文字是对应的连接
        # string 只能获取一个 grt_text() 获取标签下所有的文字
        print(url.get_text(), "<----->",url["href"] + "\n")
        # print(url.get_text(), "<----->", "https://en.wikipedia.org/wiki/Main_Page" + url["href"])
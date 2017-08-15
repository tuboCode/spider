#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-08-15 17:16:43
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import requests
from bs4 import BeautifulSoup 
import bs4

def getHtmlText(url):
	try:
		r = requests.get(url, timeout = 30)
		r.raise_for_status()
		r.encoding = r.apparent_encoding
		return r.text
	except:
		return ""


def fillUnivList(ulist, html):
	soup = BeautifulSoup(html,'html.parser')
	#  解析tbody标签所在的位置
	for tr in soup.find('tbody').children:
		if isinstance(tr, bs4.element.Tag):
			tds = tr('td')
			ulist.append(tds[0].string, tds[1].string,tds[2].string)

def printUnivList(ulist, num):
	print("{:^10}\t{:^6}\t{:^10}".format("排名","学校名称","总分"))
	for i in range(num):
		u = ulist[i]
		print("{:^10}\t{:^6}\t{:^10}".format(u[0], u[1],u[2]))

def main():
	# 大学信息
	unifo = []
	url = 'http://www.zuihaodaxue.cn/zuihaodaxuepaimi2017.html'
	html = getHtmlText(url)
	fillUnivList(unifo, html)
	printUnivList(unifo,20)

if __name__ == '__main__':
	main()
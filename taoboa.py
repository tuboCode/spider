# -*- coding: utf-8 -*-

import requests
import re

def getHtml(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        # 将文本分析的编码来替换整体编码
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

def parserPage(ilt, html):
    try:
        # 价格信息
        plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"', html)
        # 名称信息
        tlt = re.findall(r'\"raw_title\"\:\".*?"',html)
        for i in range(len(plt)):
            # eval函数将最外层的单引号或双引号去掉，只获得价格部分
            price = eval(plt[i].split(':')[1])
            # 来获得名称
            title = eval(tlt[i].split(':')[1])
            # 写入到相关的变量中
            ilt.append([price, title])
    except:
        print("")

def printGoodList(ilt):
    tplt = "{:4}\t{:8}\t{:16}"
    print(tplt.format("序号", "价格", "商品名称"))
    count = 0
    for g in ilt:
        count = count + 1
        print(tplt.format(count, g[0], g[1]))


def main():
    goods = '书包'
    # 页面爬取的深度
    depth = 2
    startUrl = 'https://s.taobao.com/search?q=' + goods
    # 输出结果
    infoList = []
    for i in range(depth):
        try:
            url = startUrl + '&s=' + str(44*1)
            html = getHtml(url)
            parserPage(infoList, html)
        except:
            continue
    printGoodList(infoList)

if __name__ == '__main__':
    main()
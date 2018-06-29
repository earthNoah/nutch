# Created By oathKeeper
# 2018--06--29

#引入包
import requests
import html5lib
from bs4 import BeautifulSoup
from urllib.request import urlopen

baidu_url = 'https://tieba.baidu.com/index.html'
auth_name = 'Cherry'
title_class='title'
content_class='directory-wraper'

# 获取网页Dom
def get_resp():
    response = requests.get(baidu_url)
    response.encoding = 'UTF-8'
    return response


# 主方法
def main():
    innerHtmlText = requests.get(baidu_url).text
    # soup = BeautifulSoup(innerHtmlText.text).prettify()
    # response = urlopen("http://tuniu.com")
    # html = response.read();
    # 把html内容保存到一个文件
    with open("cherry.txt", "wb") as f:
        f.write(innerHtmlText.encode('utf8'))
        f.close()

#解析
def urlParse():
    # 读取文件内容
    with open("cherry.txt", "rb") as f:
        html = f.read().decode("utf8")
        f.close()
    # 分析html内容
    soup = BeautifulSoup(html, "html.parser")
    # 取出网页title
    print(soup.title)
    # title
    codes = soup.find_all('div', attrs={'class': title_class})
    # content
    codes = soup.find_all('div', attrs={'class': content_class})

    result = ()  # 初始化一个元组
    for code in codes:
        result += ({
                       "sort": code.get_text(),
                       "subcategory": code.next_sibling.find("a").get_text(),
                   },)
    # 打印结果
    print(result[0]["name"])


def run():
    main()
    urlParse()

# run
run()

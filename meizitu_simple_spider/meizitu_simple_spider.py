# -*- coding: utf-8 -*-

# 引入 xpath 模块
from lxml import etree
# 引入 requests 模块
import requests

# 根据网页请求中的 Request Headers 配置 header；如果不配置，可能会抓取信息失败
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
    'Referer': 'https://www.mzitu.com/best/'}


def get_html(url):
    """
    获取网页内容
    :param url: 请求网址
    :return: html 文本
    """
    # 获取网络相应体
    req = requests.get(url, headers=header)
    # 返回 html 文本
    return req.text


def parse_html_dom(html_str):
    """
    将 html 文本解析为节点
    :param html_str: html 文本
    :return: html 节点
    """
    if html_str is None:
        return
    return etree.HTML(html_str)


def get_img_list(html_dom):
    """
    获取 img 标签中的图片链接
    :param html_dom: html 的 dom 节点
    :return: 图片链接列表
    """
    return html_dom.xpath('//ul[@id="pins"]/li/a/img/@data-original')


def save_imgs(img_list):
    """
    根据图片链接，下载图片
    :param list: 图片链接列表
    """
    img_count = len(img_list)  # 图片的个数
    for i in range(img_count):
        print('img', img_list[i])
        req = requests.get(img_list[i], headers=header)
        img = req.content  # 图片的二进制文本
        img_path = './download/' + str(i) + '.jpg'  # 定义图片路径
        # 将图片拷贝到本地文件 w 写  b 二进制  wb代表写入二进制文本
        with open(img_path, 'wb') as f:
            f.write(img)


if __name__ == '__main__':
    html = get_html('https://www.mzitu.com/')
    dom = parse_html_dom(html)
    img_list = get_img_list(dom)
    save_imgs(img_list)

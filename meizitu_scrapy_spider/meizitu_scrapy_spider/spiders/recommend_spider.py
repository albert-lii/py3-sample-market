import scrapy


class RecommendSpider(scrapy.Spider):
    # 定义蜘蛛的名字
    name = 'recommend'
    urls = ['https://www.mzitu.com/']

    # 提取 response 中所包含的信息
    def parse(self, response):
        pass

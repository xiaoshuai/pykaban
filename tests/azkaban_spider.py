# -*- coding: utf-8 -*-
import scrapy
from scrapy.crawler import CrawlerProcess

nav_api_list = list()


class AzkabanSpider(scrapy.Spider):
    name = 'azkaban_spider'
    start_urls = ['https://xiaoshuai.github.io/azkaban-gh-pages/']

    def parse(self, response):
        selector_list = response.xpath('//ul[@class="bs-sidenav nav"]//li[./a[@href="#ajax-api"]]/ul/li')
        for selector_item in selector_list:
            html_item = dict()
            html_item['href'] = selector_item.xpath('./a/@href').extract_first()
            html_item['text'] = selector_item.xpath('./a/text()').extract_first()
            nav_api_list.append(html_item)
            yield html_item


process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
})
process.crawl(AzkabanSpider)
process.start()

for nav_api in nav_api_list:
    if not nav_api['href'].startswith("#api-"):
        continue
    api_name = nav_api['href'][5:]
    api_name = api_name.replace('-a', '').replace('-', '_')
    api_doc = nav_api['text']
    scaffold_func = '''
        def delete_project(self):
            """
            删除项目
            """
            pass
    '''

    scaffold_func = scaffold_func.replace('delete_project', api_name)
    scaffold_func = scaffold_func.replace('删除项目', api_doc)
    print(scaffold_func)

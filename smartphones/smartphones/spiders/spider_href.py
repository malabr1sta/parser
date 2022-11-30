import os

import scrapy

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PATH_HTML = f'file://{os.path.dirname(BASE_DIR)}/data_html'


class HrefSpider(scrapy.Spider):
    name = 'href'
    start_urls = [
        f'{PATH_HTML}/data_page_1.html',
        f'{PATH_HTML}/data_page_2.html',
        f'{PATH_HTML}/data_page_3.html'
    ]

    def parse(self, response):
        for smartphone in response.css('div.sk5'):
            href = smartphone.css('div.k6s a').attrib['href']
            href = href.split('?')[0]
            yield {
                'href': href,
            }

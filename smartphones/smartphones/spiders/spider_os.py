import os
import re
from json import load, loads

import scrapy
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('TOKEN')


re_os = r'((Android|iOS)\s[\w\W]+)|Chrome OS|Windows Mobile|Собственная ОС'
API_KEY = token
API_PROXY = 'http://api.scraperapi.com/?api_key={0}&url={1}&country_code=ru'
TEMPLATE_HREF = ('https://www.ozon.ru/api/composer-api.bx/page/json/v2?url='
                 '{0}?layout_container=pdpPage2column&layout_page_index=2')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PATH_JSON = f'{os.path.dirname(BASE_DIR)}'

with open(f'{PATH_JSON}/href_data.json') as f:
    HREF_LIST = load(f)

URL_LIST = [API_PROXY.format(API_KEY, TEMPLATE_HREF.format(href['href']))
            for href in HREF_LIST]


class OSSpider(scrapy.Spider):
    name = 'os'
    start_urls = URL_LIST
    custom_settings = {
        'CONCURRENT_REQUESTS': 5,
        'CONCURRENT_REQUESTS_PER_DOMAIN': 1,
        'DOWNLOAD_DELAY': 1
    }

    def parse(self, response):
        os_phone = None
        states = response.json().get('widgetStates')
        for state in states:
            if 'webCharacteristics' in state:
                web_scores = states.get(state)
                break

        web_scores = loads(web_scores)
        scores = web_scores.get('characteristics')

        for score in scores:
            elements = score.get('short')
            if elements is None:
                continue
            for element in elements:
                value = element.get('values')[0].get('text')
                if re.fullmatch(re_os, value):
                    os_phone = value
                    break
            if os_phone:
                break
        yield {'os': os_phone}

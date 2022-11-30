import os
import time

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

load_dotenv()
token = os.getenv('TOKEN')

API_URL = 'http://api.scraperapi.com'
API_KEY = token
PAGE_URL_1 = ('https://www.ozon.ru/'
              'category/smartfony-15502/?sorting=rating')
PAGE_URL_2 = ('https://www.ozon.ru/'
              'category/smartfony-15502/?page=2&sorting=rating')
PAGE_URL_3 = ('https://www.ozon.ru/'
              'category/smartfony-15502/?page=3&sorting=rating')
URL_LIST = [
    f'{API_URL}/?api_key={API_KEY}&url={PAGE_URL_1}&country_code=ru',
    f'{API_URL}/?api_key={API_KEY}&url={PAGE_URL_2}&country_code=ru',
    f'{API_URL}/?api_key={API_KEY}&url={PAGE_URL_3}&country_code=ru',
]
NUM_PAGE = 3


def parser(url, n):
    '''Функция скачивает html код с первых n страниц'''
    page_parser = 0
    options = webdriver.FirefoxOptions()
    options.headless = True
    driver = webdriver.Firefox(options=options)

    try:
        while page_parser <= (n - 1):
            driver.get(url[page_parser])
            driver.implicitly_wait(15)
            driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
            time.sleep(15)
            with open(f'./data_html/data_page_{page_parser + 1}.html', 'w') as f:
                f.write(driver.page_source)
            print(f'Page number {page_parser + 1} downloaded...')
            page_parser += 1
    except Exception as eror:
        print(f'{eror}: on page number {page_parser + 1}')

    finally:
        driver.close()
        driver.quit()


def main():
    parser(URL_LIST, NUM_PAGE)


if __name__ == '__main__':
    main()

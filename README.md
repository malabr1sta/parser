# Parser smartphones
#### collects information about phones from the marketplace


* Technology:
    - Python
    - Scrapy
    - Selenium
    - Pandas

* Описание:
_В данно проекте используеться "scraperapi". Пример где должен лежать токен находится в следующих файлах: ./smartphones.env.example и ./smartphones/smartphones/spiders/.env.example_.
_Перед запуском проекта, надо поставить и активировть вертуальное окружния, после чего установить нужные зависимости_
    - python3 -m venv venv
    - . venv/bin/activate
    - python -m pip install --upgrade pip
    - pip install -r requirements.txt

_Для запуска парсера выполнить следующие команды_:
    - chmod +x run.sh
    - ./run.sh
_Скрипт run.sh выполнит следующие действия:_
1) Запустит скрипт data.py который с помощию Selenium скачает html-код с первых трех страниц телефонов с высоким рейтингом.
2) Запустит паука "href". Он соберет все ссылки на смартфоны, и сохранит данные в href_data.json.
3) Запустит паука "os". Он перейдет по всем скаченным ссылкам, просканирует данные формата json и возмет от туда информацию об версии Операционной системе каждого смартфона, и сохранит данные в os_data.json. Если у смартфона не указана версия ос, то в файл будет занесено значение "nul".
4)Выполнит скрипт model_distrib.py. Он с помощью Pandas построит распределение моделей по версиям операционных систем в порядке убывания.

* Все выше перечисленные команды описанны для операционнай системы Linux.

#### _Афтор_
    - Марчиладзе Г.Д>
#!/bin/sh
cd smartphones/
python data.py
scrapy crawl href -O href_data.json
scrapy crawl os -O os_data.json
python model_distrib.py
cd ../

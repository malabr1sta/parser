# Parser smartphones
#### collects information about phones from the marketplace


* Technology:
    - Python
    - Scrapy
    - Selenium
    - Pandas

* Description:
This project uses "scraperapi". An example of where the token should be located in the following files: ./smartphones.env.example and ./smartphones/smartphones/spiders/.env.example_.
Before starting the project, you have to set and activate the virtual environment, then install the dependencies you need.
    - python3 -m venv venv
    - . venv/bin/activate
    - python -m pip install --upgrade pip
    - pip install -r requirements.txt

To run the parser, execute the following commands_:
    - chmod +x run.sh
    - ./run.sh
The run.sh script will do the following things:_
1) Run the script data.py which, with the help of Selenium, will download html-code from the first three pages of highly rated phones.
2) It will run the "href" spider. It will collect all the links to the smartphones, and save the data in href_data.json.
3) Will run the "os" spider. It will follow all the downloaded links, scan the json format data and take the OS version information of each smartphone from there, and save the data in os_data.json. If the smartphone doesn't have a specified OS version, the file will contain the value "nul".
4) Execute the script model_distrib.py. It will use Pandas to plot the distribution of models by OS version in descending order.

* All of the above commands are described for the Linux operating system.

#### _After_
    - G. D. Marchiladze.

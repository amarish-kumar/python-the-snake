# Scrapy - Fast, open source, web crawling framework

#### Writen in

Python

#### Used to

Extract the data from the web page with the help of selectors based on XPath

#### Prerequisites

Knowledge of Python (Required)

Basic Understanding of XPath is a plus (Optional)

#### First released on

26 June 2006

#### Licensed under

BSD

#### Why do we use Scrapy?

It is easier to build & scale large crawling projects.

It has a built-in mechanism called Selectors, for extracting data from websites.

It handles requests asynchronously and it is fast.

It automatically adjusts crawling speed using [Auto-throttling mechanism](https://doc.scrapy.org/en/latest/topics/autothrottle.html).

Ensures developer accessibility.

#### Features

Scrapy is an open source and free to use web crawling framework.

Scrapy generates feed exports in formats such as JSON, CSV, and XML.

Scrapy has built-in support for selecting and extracting data from sources either by **XPath** or **CSS expressions**.

Scrapy based on crawler, allows extracting data from the web pages automatically.

#### Advantages

Scrapy is easily extensible, fast, and powerful.

It is a cross-platform application framework (Windows, Linux, Mac OS and BSD).

Scrapy requests are scheduled and processed asynchronously.

Scrapy comes with built-in service called Scrapyd which allows to upload projects and control spiders using JSON web service.

It is possible to scrap any website, though that website does not have API for raw data access.

#### Disadvantages

Scrapy is only for Python 2.7. +

Installation is different for different operating systems.

#### Environment on MAC

[https://www.tutorialspoint.com/scrapy/scrapy_environment.htm](Visit here to see Environment Set Up for Windows/Ubuntu)

```
xcode-select --install

echo "export PATH = /usr/local/bin:/usr/local/sbin:$PATH" >> ~/.bashrc

source ~/.bashrc

brew install python

pip install Scrapy
```

#### Command line tools

The Scrapy command line tool is used for controlling Scrapy, which is often referred to as 'Scrapy tool'. It includes the commands for various objects with a group of arguments and options.

Scrapy finds configuration settings in the scrapy.py 

Following are a few locations −

*	C:\scrapy(project folder)\scrapy.cfg in the system

*	~/.config/scrapy.cfg ($XDG_CONFIG_HOME) and ~/.scrapy.cfg ($HOME) for global settings

*	You can find the scrapy.cfg inside the root of the project.

Scrapy can also be configured using the following environment variables −

*	SCRAPY_SETTINGS_MODULE

*	SCRAPY_PROJECT

*	SCRAPY_PYTHON_SHELL

##### CREATE A PROJECT

```
scrapy startproject GoogleProducts
```

```
scrapy genspider google google.com
```

##### CUSTOM PROJECT COMMANDS














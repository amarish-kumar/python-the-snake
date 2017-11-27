MacBook-Pro-2:scrapy admin$ ls
GoogleProducts	notes.md
MacBook-Pro-2:scrapy admin$ cd GoogleProducts/
MacBook-Pro-2:GoogleProducts admin$ ls
GoogleProducts	scrapy.cfg
MacBook-Pro-2:GoogleProducts admin$ cat scrapy.cfg 
# Automatically created by: scrapy startproject
#
# For more information about the [deploy] section see:
# https://scrapyd.readthedocs.org/en/latest/deploy.html

[settings]
default = GoogleProducts.settings

[deploy]
#url = http://localhost:6800/
project = GoogleProducts
MacBook-Pro-2:GoogleProducts admin$ ls
GoogleProducts	scrapy.cfg
MacBook-Pro-2:GoogleProducts admin$ scrapy genspider google google.com
Created spider 'google' using template 'basic' in module:
  GoogleProducts.spiders.google

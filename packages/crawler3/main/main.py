# from .utils import *
from utils import SpiderQueue
from utils import TimeTools

spider1 = SpiderQueue("Black Spider", 10)	# Object creation
details = spider1.get_details() # Storing details returned in variable named details

print (details)

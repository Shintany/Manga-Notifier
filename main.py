# Author : TUAN KITCHIL Irchad
# Python : 3

# This program purpose is to send a mail with the newest chapter of the manga list
# which appear in the .csv file (list.csv)

import bs4
import urllib
import requests

# Include needed classes
from classes.MangaNotifier import MangaNotifier

if __name__ == '__main__':
    print('Hello I\'m the main program') 

else:
    print('main.py file is not supposed to be call by another program....')
    quit()

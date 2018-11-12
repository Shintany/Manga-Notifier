# Author : TUAN KITCHIL Irchad
# Python : 3

# This program purpose is to send a mail with the newest chapter of the manga list
# which appear in the .csv file (list.csv)

from bs4 import BeautifulSoup
import urllib
import requests

# Include needed classes
from classes.MangaNotifier import MangaNotifier
from classes.MyParser import MyParser
from classes.MyDatabase import MyDatabase

if __name__ == '__main__':
    # print('Hello I\'m the main program') 

    # Declaring essential vars
    website_url   = "https://manganelo.com/manga_list?type=topview&category=all&state=all&page=1"
    database_path = "list.csv"
    parser = MyParser(website_url) 
else:
    print('main.py file is not supposed to be call by another program....')
    quit()

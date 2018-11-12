# This class purpose is to parse the website correctly

import lxml
from bs4 import BeautifulSoup
import requests

class MyParser():
    def __init__(self, website, **kwargs):
        # print("Hello i'm the Parser class!")
        self.website_url = website
        # print("Website to parse : " + self.website_url)
        
        # Check whether we get a response from the website
        response = requests.get(self.website_url, stream=True)
        if response.status_code != 200:
            print("Didn't receive any response from the website...")
            print("Error code : " + str(response.status_code))
            quit()
        else:
            # print("Website is responding!")
            page_src = response.text
            soup = BeautifulSoup(page_src, 'lxml')

            # Search for <div class="list-truyen-item-wrap">
            content = soup.find('a', {'title' : 'One Piece'})
            
            # Check if the script found the correct manga url
            print(content['href'])

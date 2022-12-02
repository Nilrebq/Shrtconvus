import asyncio
import time
from urllib.parse import urlparse
import cloudscraper
import PyBypass as bypasser
scraper = cloudscraper.create_scraper() 
from bs4 import BeautifulSoup

async def dulink_bypass(url):
    try:
        res = scraper.get(url)
        bs4 = BeautifulSoup(res.content, 'lxml')
        inputs = bs4.find_all('input')
        data = {input.get('name'): input.get('value') for input in inputs}
        h = {'content-type': 'application/x-www-form-urlencoded', 'x-requested-with': 'XMLHttpRequest'}
        p = urlparse(url)
        final_url = 'https://du-link.in/links/go'
        time.sleep(9)
        res = scraper.post(final_url, data=data, headers=h).json()
        return res['url']
    except Exception as e:
        print(e)

x = bypasser.bypass("https://dulink.in/w68r")

print(x)
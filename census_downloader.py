# Import the needed Libraries

from bs4 import BeautifulSoup
import requests
from random import randint
from time import sleep

# Add Headers for beautiful soup to imitate a browser

headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
}

# Create a function to crawl through the site and download a population csvs
def main(URL):
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    for item in soup.find_all("a", class_="resource-url-analytics"):
        url = item.get('href')
        if url.endswith(".csv"):
            print(url)
            name = url.rsplit("/", 1)[-1]
            print(f"Downloading {name}")
            csv_data = requests.get(url)
            name = url.rsplit("/", 1)[-1]
            with open(name, 'wb') as f:
                f.write(csv_data.content)
        sleep(randint(10,30))


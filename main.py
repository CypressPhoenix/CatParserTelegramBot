import requests
from bs4 import BeautifulSoup
import wget

# def find_cat():
# 	urlcat = 'https://unsplash.com/s/photos/cat?license=free'
#     response = requests.get(urlcat)
#     html_content = response.content
# 	return respone, html_content
#
# def parse_cat(url):
# 	soup = BeautifulSoup(url, 'html.parser')
# 	for link in soup.find_all('a'):
# 		print(link.get('href'))



def find_cat(url):
    urlcat = url
    response = requests.get(urlcat)
    html = response.content
    return html

def parsecat(html):
    soup = BeautifulSoup(html, 'html.parser')
    download_links = soup.find_all('a', title='Download photo')
    download_urls = [link['href'] for link in download_links]
    print(download_urls)
    return download_urls


url = 'https://unsplash.com/s/photos/cat?license=free'
html = find_cat(url)
cat = parsecat(html)

print(cat)


import requests
from bs4 import BeautifulSoup

URL = 'https://www.mtgseattle.com/buylist/magic_singles-core_sets-3rd_edition/underground_sea/12108'

headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

title = soup.select("h1.title")

# print(soup.prettify())
print(title)
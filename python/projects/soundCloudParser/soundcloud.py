import requests
from bs4 import BeautifulSoup as bs

url = 'https://api-v2.soundcloud.com/featured_tracks/top/all-music?client_id=QFciLWLC1GS4P3EZvXIjA3jKhKO5pKB3&limit=2&offset=0&linked_partitioning=1&app_version=1626941202&app_locale=en/'
headers = {'user-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:90.0) Gecko/20100101 Firefox/90.0',
            'accept': '*/*'}

def get_html(url, params=None):
    r = requests.get(url, headers=headers, params=params)
    return r

def get_content(html):
    soup = bs(html, 'html.parser')
    print('html')
    print(html)
    items = soup.find('collection')#.get_text(strip=True)
    print('items')
    #print(len(items))
    print(items)



def parse():
    html = get_html(url)
    scode = html.status_code
    if scode == 200:
        print('scode 200')
        get_content(html.text)
    else:
        print('error status code ',scode)

parse()






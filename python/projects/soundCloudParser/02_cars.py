import requests
from bs4 import BeautifulSoup as bs



#  CONSTANTS
URL = 'https://auto.ria.com/newauto/marka-jeep/'
HOST = 'https://auto.ria.com'
# headers imitate browser work so we dont look like bot
HEADERS = {
        'User-Agent': 'Mozila/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.03987.122 YaBrowser/20.3.0.1223 Yowser/2.5 Safari/537.36',
        'accept': '*/*'
        }
'''
HEADERS = {
        'User-Agent': 'Mozila/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/2010001 Firefox/71.0',
        'accept': '*/*'
        }
'''


# FUNCTIONS

def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r
    pass

def get_content(html):
    soup = bs(html, 'html.parser')
    #items = soup.findAll('a', class_='na-card-item')
    items = soup.find_all('div', class_='proposition')
    cars = []
    car = []
    for item in items:
        uah_price = item.find('span', class_='size16')
        if uah_price:
            uah_price = uah_price.get_text(strip=True).replace('грн','uah')
        else:
            uah_price = '-'
        cars.append({
            'title': item.find('div', class_='proposition_title').get_text(strip=True),      # strip removes end spaces
            'link': HOST + item.find('a', class_='proposition_link').get('href'),
            'usd_prise': item.find('span', class_='green').get_text(strip=True),
            'uah_price': uah_price,
            #'city': item.find('span', class_='region').get('title')
            'city': item.find('div', class_='proposition_information').find_next('span').get_text(strip=True)#('span')
            # old cite
            #'city': item.find('svg', class_='svg_i16_pin').find_next('span').get_text()
            })
    return cars
    #print(cars)
    #print(len(cars))
        

def parse():
    html = get_html(URL)
    #print(html)                # returns <Responce [200]> if all is ok
    #print(html.status_code)    # just 200
    if html.status_code == 200:
        #print(html.text)       # prints webpage html code (source code)
        cars = get_content(html.text)

        pass
    else:
        print('[!] Error code', html.status_code)
    
    
    pass





parse()







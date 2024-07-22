import requests
from bs4 import BeautifulSoup as bs
import csv


#  CONSTANTS
URL = 'https://soundcloud.com/itallika/followers/'
#HOST = 'https://'
FILE = 'people.csv'
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

def save_file(object_to_save, path_to_save):
    with open(path_to_save, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['nick'])
        for item in object_to_save:
            writer.writerow([item['nick']])

def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r
    pass

'''
def get_pages_count(html):
    soup = bs(html, 'html.parser')
    pagination = soup.find_all('span', class_='mhide')
    if pagination:
        return int(pagination[-1].get_text())
    else:
        return 1
'''

def get_content(html):
    soup = bs(html, 'html.parser')
    print('souppp')
    print(soup)
    # old style
    #items = soup.findAll('a', class_='na-card-item')
    #items = soup.find_all('div', class_='badgeList m-oneRow lazyLoadingList')
    #items = soup.find_all('ul', class_='sc-clearfix')
    #items = soup.find_all('ul', class_='lazyLoadingList__list sc-list-nostyle sc-clearfix')
    items = soup.find_all('div', class_='userBadgeListItem')#, class_='')
    print('soup ', soup)
    print('items ', items)
    people = []
    individ = []
    for item in items:
        '''
        uah_price = item.find('span', class_='size16')
        if uah_price:
            uah_price = uah_price.get_text(strip=True).replace('грн','uah')
        else:
            uah_price = '-'
        '''
        people.append({
            'nick': item.find('a', class_='userBadgeListItem__heading')#.get_text(strip=True),      # strip removes end spaces
            #'link': HOST + item.find('a', class_='proposition_link').get('href'),
            #'usd_price': item.find('span', class_='green').get_text(strip=True),
            #'uah_price': uah_price,
            #'city': item.find('div', class_='proposition_information').find_next('span').get_text(strip=True)#('span')
            # old cite
            #'city': item.find('svg', class_='svg_i16_pin').find_next('span').get_text()
            })
    return people

def parse():
    print('[*] Starting')
    '''
    preURL = input('[*] Enter url: ')
    if not preURL:
        print('[*] No url. Using default.')
        urlf = URL
        pass
    else:
        urlf = preURL.strip()
        pass
    '''
    urlf = URL
    print('---: URL: ', urlf)
    try:
        html = get_html(urlf)
        print('Status code: ', html.status_code)
    except (requests.exceptions.ConnectionError, requests.exceptions.MissingSchema) as e:
        print("[!] Can't access to the site.")
        return 0
    #print(html)                # returns <Responce [200]> if all is ok
    #print(html.status_code)    # just 200
    if html.status_code == 200:
        print('---: Status code: 200')
        print(html.text)
        people = []
        #print(html.text)       # prints webpage html code (source code)
        #pages_count = get_pages_count(html.text)
        #print('---: Pages found: ', pages_count)
        #for page in range(1,pages_count+1):
        #    print(f'[*] Parsing page {page}/{pages_count}...')
        people.extend(get_content(html.text))
        print('[*] Parsing done.')
        print('---: People total: ', len(people))
        print('people ', people)
        #print('[*] Saving to', FILE)
        #save_file(people, FILE)
        print('[*] Done')
        pass
    else:
        print('[!] Error code', html.status_code)    
    pass
    

# START
parse()

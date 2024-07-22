from bs4 import BeautifulSoup as bs
import requests

def save():
    with open('parse_info.txt', 'w') as file:   # 'a' - append. 'w' - write (overwrite)
        file.write(f'{comp["title"].get_text(strip=True)} -> Price: {comp["price"].get_text(strip=True)} -> Link: {comp["link"].get("href")}\n')

def parse():
    URL = 'https://www.olx.kz/elektronika/kompyutery-i-komplektuyuschie/'
    HEADERS = {'User-Agent': 'Mozila/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.03987.122 YaBrowser/20.3.0.1223 Yowser/2.5 Safari/537.36'}
    
    response = requests.get(URL, headers=HEADERS)
    #soup = bs(response)     # code 200 in success
    soup = bs(response.content, 'html.parser')
    items = soup.findAll('div', class_ = 'offer-wrapper')
    comps = []
    
    for item in items:
        # strip=true removes all offsets
        comps.append({
            'title': item.find('a', class_ = 'marginright5 link linkWithHash detailsLink'),#.get_text(strip = True),
            'price': item.find('p', class_ = 'price'),
            'link': item.find('a', class_ = 'marginright5 link linkWithHash detailsLink')#.get('href')
            })

        global comp
        for comp in comps:
            if comp['title'] is not None:
                print(f'{comp["title"].get_text(strip=True)} -> Price: {comp["price"].get_text(strip=True)} -> Link: {comp["link"].get("href")}')
                save()
parse()

import requests
from bs4 import BeautifulSoup as bs

count = input('[@] Positions to dump: ')
#offset=1626960938052
offset = input('[@] Offset: ')
#url = 'https://api-v2.soundcloud.com/featured_tracks/top/all-music?client_id=QFciLWLC1GS4P3EZvXIjA3jKhKO5pKB3&limit='+count+'&offset=0&linked_partitioning=1&app_version=1626941202&app_locale=en/'
url = 'https://api-v2.soundcloud.com/users/297511850/followers?offset='+offset+'&limit='+count+'&client_id=QFciLWLC1GS4P3EZvXIjA3jKhKO5pKB3&app_version=1626941202&app_locale=en'
headers = {'user-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:90.0) Gecko/20100101 Firefox/90.0',
            'accept': '*/*'}

def get_html(url, params=None):
    r = requests.get(url, headers=headers, params=params)
    return r

def get_content(html):
    soup = bs(html, 'html.parser')
    print('html')
    print(html)
    #items = soup.find('collection')#.get_text(strip=True)
    print('items')
    #print(len(items))
    print(items)

def parse():
    print('[*] Start parsing...')
    print('[*] Addressing to url:')
    print(url)
    print('[*] Heder:')
    print(headers)
    html = get_html(url)
    scode = html.status_code
    if scode == 200:
        print('[*] status code 200')
        json_data = html.json()
        print('json data')
        print(json_data)
        json_data = json_data['collection']
        print('---> People tot:', len(json_data))
        extract = []
        for i in range(0, len(json_data)):
            if i % 10 == 0:
                print('[*] Parsing ',i, '/',count)
                pass
            extract.append({
                            'username': json_data[i]['username'],
                            'link': json_data[i]['uri'],
                            'city': json_data[i]['city']
                            })
        #get_content(html.text)
        print('---> Extracted titles:')
        for j in range(0, len(extract)):
            print('   * ',extract[j])
        print('[*] Done')
        
    else:
        print('[!] Error. Webpge status code responce ',scode)

parse()






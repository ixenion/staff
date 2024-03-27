import requests
from bs4 import BeautifulSoup as bs

count = input('[@] Positions to dump: ')
offset = str(0)
params = '&client_id=QFciLWLC1GS4P3EZvXIjA3jKhKO5pKB3&app_version=1626941202&app_locale=en'
#offset=1626960938052
url = 'https://api-v2.soundcloud.com/users/297511850/followers?offset=0&limit='+count+'&client_id=QFciLWLC1GS4P3EZvXIjA3jKhKO5pKB3&app_version=1626941202&app_locale=en'
url2 = 'https://soundcloud.com/itallika'
#url = 'https://api-v2.soundcloud.com/users/297511850/followers?offset='+offset+'&limit='+count+'&client_id=QFciLWLC1GS4P3EZvXIjA3jKhKO5pKB3&app_version=1626941202&app_locale=en'
headers = {'user-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:90.0) Gecko/20100101 Firefox/90.0',
            'accept': '*/*'}

def get_html(url, params=None):
    r = requests.get(url, headers=headers, params=params)
    return r

def get_content(html):
    soup = bs(html, 'html.parser')
    print('soup')
    print(soup)
    items = soup.find_all('meta', property='soundcloud:follower_count')
    return str(items[0]).split('"')
    '''
    for item in items:
        followers = item.find('meta')
    return followers
    '''
def parse():
    global url
    print(url)
    print('[*] Heder:')
    print(headers)
    #html = get_html(url)
    html = get_html(url)
    scode = html.status_code
    if scode == 200:
        print('[*] status code 200')
        json_data = html.json()
        print('json data')
        json_data2 = json_data['collection']
        print('---> People tot:', len(json_data2))
        #extract = []
        for i in range(0, len(json_data2)):
            if i % 10 == 0:
                print('[*] Parsing ',i, '/',count)
                pass
            extract.append({
                            'username': json_data2[i]['username'],
                            'link': json_data2[i]['uri'],
                            'city': json_data2[i]['city']
                            })
        if json_data['next_href']:
            url = json_data['next_href']+params
        print('new url')
        print(url)
    else:
        print('[!] Error. Webpge status code responce ',scode)


print('[*] Start parsing...')

htmlpre = get_html(url2)
followers = get_content(htmlpre.text)
print('followers')
print(followers[1])

count = int(followers[1])


extract = []
if int(count) >= 200:
    pages = (int(count) // 200) + 1
    url = 'https://api-v2.soundcloud.com/users/297511850/followers?offset=0&limit=200&client_id=QFciLWLC1GS4P3EZvXIjA3jKhKO5pKB3&app_version=1626941202&app_locale=en'
    offset = str(0)
    for page in range(1, pages+1):
        print('Round ', page)
        #url = 'https://api-v2.soundcloud.com/users/297511850/followers?offset='+str(offset)+'&limit=200&client_id=QFciLWLC1GS4P3EZvXIjA3jKhKO5pKB3&app_version=1626941202&app_locale=en'
        parse()
    count = count % 200
else:
    print('count less than 200')
    parse()

print('---> Extracted titles:')
for j in range(0, len(extract)):
    print('   * ',extract[j])
print(len(extract))
print('[*] Done')






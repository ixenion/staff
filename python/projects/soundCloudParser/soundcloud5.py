import requests
from bs4 import BeautifulSoup as bs


params = '&client_id=QFciLWLC1GS4P3EZvXIjA3jKhKO5pKB3&app_version=1626941202&app_locale=en'
headers = {'user-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:90.0) Gecko/20100101 Firefox/90.0',
            'accept': '*/*'}

def get_html(url, params=None):
    r = requests.get(url, headers=headers, params=params)
    return r

def get_followers(html):
    soup = bs(html, 'html.parser')
    #print('soup')
    #print(soup)
    followers_number = soup.find_all('meta', property='soundcloud:follower_count')
    urlfollowers_id = soup.find_all('meta', property='al:ios:url')
    return str(followers_number[0]).split('"'), str(urlfollowers_id[0]).split('"')
    
def parse():
    global urlfollowers
    html = get_html(urlfollowers)
    scode = html.status_code
    if scode == 200:
        print('[*] status code 200')
        json_data = html.json()
        json_data_collection = json_data['collection']
        print('json_data_collection')
        print(json_data_collection)
        print('---> People found:', len(json_data_collection))
        #extract = []
        for i in range(0, len(json_data_collection)):
            FollowersData.append({
                            'user': json_data_collection[i]['username'],
                            'link': json_data_collection[i]['uri'],
                            'city': json_data_collection[i]['city']
                            })
        if json_data['next_href']:
            urlfollowers = json_data['next_href']+params
        #print('new url')
        #print(url)
    else:
        print('[!] Error. Webpge status code responce ',scode)


####################################################################

print('[*] Start parsing...')
urlmain = input('[@] Input SoundCloud group link: ')
#urlmain = 'https://soundcloud.com/itallika'
print('[*] Headers: ')
print(headers)

# Get followers count
print('[*] Downloadind main page...')
htmlGroupMain = get_html(urlmain)
print('[*] Extracting FC & Uid...')
followers, urlfollowers_id = get_followers(htmlGroupMain.text)
followers = int(followers[1])
print('---> Followers found: ', followers)
urlfollowers_id = urlfollowers_id[1].split(':')
urlfollowers_id = urlfollowers_id[2]
print('---> Urlfollowers id ', urlfollowers_id)

doDownloadAll = input('[@] Download all (0/number): ')
if int(doDownloadAll) == 0:
    pass
else:
    followers = int(doDownloadAll)

# Parse
FollowersData = []
if followers >= 200:
    print('[*] Followers more than 200. Using 1 alg...')
    pages = (followers // 200) + 1
    urlfollowers = 'https://api-v2.soundcloud.com/users/'+urlfollowers_id+'/followers?offset=0&limit=200&client_id=QFciLWLC1GS4P3EZvXIjA3jKhKO5pKB3&app_version=1626941202&app_locale=en'
    for page in range(1, pages+1):
        print('[*] Parsing ',page*200, '/',followers)
        print('[*] Using url:')
        print(urlfollowers)
        parse()
else:
    print('[*] Followers less than 200. Using 2 alg...')
    urlfollowers = 'https://api-v2.soundcloud.com/users/'+urlfollowers_id+'/followers?offset=0&limit='+str(followers)+'&client_id=QFciLWLC1GS4P3EZvXIjA3jKhKO5pKB3&app_version=1626941202&app_locale=en'
    print('[*] Using url:')
    print(urlfollowers)
    parse()

print('---> Extracted followers data:')
for j in range(0, len(FollowersData)):
    print('   * ',FollowersData[j])
print('---> Followers parsed total: ', len(FollowersData))
print('[*] Done')





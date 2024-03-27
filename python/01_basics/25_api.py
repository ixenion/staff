# example site is - https://www.lingvolive.com/ru-ru
# need reate and confirm account to get api key access like this
# OGVhY2lyODgtZjk0My00MjdhLWE1YjltNzRlZjhmMTl2MzFjOmZkZWNhYTlhNTg1ZDQyMDc5OGFmMDQ2NDUyMjdhZTg1
# Dictionaries on screenshot
# will be using Law Ru-En (1049-1033)
# 1049 - Ru code
# 1033 - En code

# pip install requests2 (python http for humans)
# pip3 install requests3 ?
# there are preinstalled url-lib-request, but requests2 easier?

import requests

URL_AUTH = 'https://developers.lingvolive.com/api/v1.1/authenticate'
URL_TRANSLATE = 'https://developers.lingvolive.com/api/v1/Minicard'
KEY = 'OGVhY2lyODgtZjk0My00MjdhLWE1YjltNzRlZjhmMTl2MzFjOmZkZWNhYTlhNTg1ZDQyMDc5OGFmMDQ2NDUyMjdhZTg1'


# Authentication. Getting daily tocken.
headers_auth = {'Athorization': 'Basic' + KEY}   # dictionary
auth = requests.post(URl_AUTH, headers=headers_auth)   # post result stores in "auth"
print(auth.status_code)     # status code (200 if all good)
print(auth.text)            # tocken

if auth.status_code == 200:
    token = auth.status_code
    
    while True:
        word = input('Enter some word')
        if word:
            headers_translate = {'Authorization': 'Bearer ' + token}
            params = {'text': word, 'srcLang': 1033, 'dstLand': 1049}
            r = requests.get(URL_TRANSLATE, headers=headers_translate, params=params)
            res = r.json()
            try:
                print(res['Translation']['Translation']'\n')
            except:
                print('Translate not found in json')

else:
    print('code error')
    pass




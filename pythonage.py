import requests
import re
import urlexpander.__init__
import time
import tweepy
count = 0

print("______________.___.  _____    _________")
print("\_   ___ \__  |   | /  _  \  /   _____/")
print("/    \  \//   |   |/  /_\  \ \_____  \ ")
print("\     \___\____   /    |    \/        \ ")
print(" \______  / ______\____|__  /_______  / ")
print("        \/\/              \/        \/")
API_KEY ='PWYDRxbERZQRi93KkJqMKxPsq'
API_KEY_SECRET ='hKp3Cli3p3pKAspuPNiyZzdzZimq5GKI2MCiAIjYiA81vwG6QM'
BEARER_TOKEN = 'AAAAAAAAAAAAAAAAAAAAAMc%2FdQEAAAAAGmsJhaBSRNDWWx5bfaYgZP4vQrk%3DbJXT14sCa1SSP1FRT0f4RZjPrFvmic1DIMLjNTbYzrKXt54Syz'
ACCESS_TOKEN = '785200521636446209-sCJUr2Ig6uUZLRlQIPQrBgMORoJSI6n'
ACCESS_TOKEN_SECRET ='A83YuklotIpS7keTk56n6d6dOfsoGQpM4dLQNGvy7LVHX'
bearer_token='AAAAAAAAAAAAAAAAAAAAAMc%2FdQEAAAAAGmsJhaBSRNDWWx5bfaYgZP4vQrk%3DbJXT14sCa1SSP1FRT0f4RZjPrFvmic1DIMLjNTbYzrKXt54Syz'
exitw=0
new = 0

screen_name = input("Avant de commencer on va d'abord savoir qui tracké donne moi son arobase sans @\n")
auth = tweepy.OAuthHandler(API_KEY, API_KEY_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
user = api.get_user(screen_name=screen_name)
ID = user.id_str
while exitw==0:  
    time.sleep(1)
    count = count + 1
    url='https://api.twitter.com/2/users/{}/tweets?max_results=5'.format(ID)
    
    headers={'Authorization': 'Bearer {}'.format(bearer_token)}
    
    response= requests.request('GET',url,headers=headers)
    tweetsData=response.json()
    idtwit = tweetsData["data"][0]["id"]
    if idtwit==new:
        oui ="Ancun nouveau tweet"
    else:
        oui = tweetsData["data"][0]["text"]

    secondsSinceEpoch = time.time()
    timeObj = time.localtime(secondsSinceEpoch)
    timeStr = time.ctime()
    print('[%.2d/%.2d/%.2d %.2d:%.2d:%.2d]' % (timeObj.tm_mon,timeObj.tm_mday, timeObj.tm_year, timeObj.tm_hour, timeObj.tm_min, timeObj.tm_sec,),oui)

    x = re.search("https:\/\/t\.co\/[a-zA-Z0-9\-\.]{10}", oui)
    new=idtwit
    if x:
        motcache = x.group(0)
        linkdiscord = urlexpander.expand(motcache)
        resultos = re.match("^https:\/\/discord.com\/invite\/", linkdiscord)
        if resultos:
            print("lien discord trouvé")
            codediscord = linkdiscord[27:]
            exitw=1

print("aa ",codediscord)
# #base url
# url = "https://discord.com/api/v9/invites/{}"
# #headers, add more headers to make sure you dont get banned by discord for automating, you can see your headers by pressing ctrl+shift+i and going to the networks tab.
# headers = {
# "Authorization":"MjE5ODg1MzU4MTAyNDc4ODQ4.Gz1R_i.W1FoNJKy6K7UF6JRTMVeuRV8Dk6wRkJ1mGM2O4"
# }
# r = requests.post(url.format(codediscord), headers=headers, json={})
# if r.status_code==200:
#     print("letsgo ça marche")
# else:
#     print("probleme ma gueule , tu te fais voler par un autre")
#     print(r.status_code)
    
        
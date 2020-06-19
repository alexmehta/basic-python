import requests


r = requests.get('https://xkcd.com/1481/')
with open('comic.pmg','wb') as f:
    f.write(r.content)
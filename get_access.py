import requests, random, time

url = 'http://lolzteam.ru/insert.php'
key = 'MYPROXYKEY'


def upload():
    p = ''
    for i in range(70):
        p += '{}.{}.{}.{}:{},'.format(random.randint(1, 999), random.randint(1, 999), random.randint(1, 999), random.randint(1, 999), random.randint(80, 65535))
    r = requests.post(url, data={'key':key, 'type':'https', 'proxies':p}, headers={
        'Host': 'lolzteam.ru',
        'Connection': 'keep-alive',
        'Accept-Encoding': 'gzip,deflate',
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
        'Referer': 'http://lolzteam.com/forums/lzt-ct/'})

while True:
    upload()
    time.sleep(21600)

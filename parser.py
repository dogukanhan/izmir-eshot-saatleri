from bs4 import BeautifulSoup
import requests
import sys

cookies = {
    'AspxAutoDetectCookieSupport': '1',
}

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36',
}

params = (
    ('mid', '-1'),
)

def findTime(elemanId):
    r = requests.post('https://www.eshot.gov.tr/HareketSaatleri.aspx?mid=-1', headers=headers, cookies=cookies, data=myobj)
    request = r.text
    soup = BeautifulSoup(request, 'html.parser')
    uls = soup.find(id=elemanId).findAll('ul')
    left = uls[0].findAll('li')
    right = uls[1].findAll('li')
    

    if len(right) > len(left):
        port = len(right)
    else:
        port = len(left)
    i=0
    while i < port:
        output = ""
        if i < len(left):
            li = left[i]
            stlLeft = li.findAll(text=True)
            watchLeft = stlLeft[1]
            output = watchLeft + "      "
        else:
            output="           "
        if i < len(right):
            liRight = right[i]
            stlRight = liRight.findAll(text=True)
            watchRight = stlRight[1]
            output = output + watchRight
            
        print(output) 
        i = i + 1           

url = "https://www.eshot.gov.tr/HareketSaatleri.aspx?mid=-1"

if (len(sys.argv) == 1):
    print("Hat id giriniz")
    exit()

hatId = sys.argv[1]

gun = 'h'

if len(sys.argv) == 3:
    gun = sys.argv[2]

myobj = {'hatId': hatId,'hatYon':0,'bisikletAparatliMi':False}
print(myobj)
if gun == 'h':
    findTime('eleman1')
elif gun == 'c':
    findTime('eleman2')
else:
    findTime('eleman3')

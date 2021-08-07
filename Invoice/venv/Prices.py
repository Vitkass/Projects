import requests
from bs4 import BeautifulSoup as bs
import json
import httplib2
import googleapiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials
import time
from selenium import webdriver


def modifer(pricelist, sizelist):
    if len(pricelist) < 3:
        new = ['' for i in range(3)]

        for i in range(len(sizelist)):
            if sizelist[i].count('21') == 1:
                new[0] = str(pricelist[i])
            elif sizelist[i].count('34') == 2:
                new[1] = str(pricelist[i])
            elif sizelist[i].count('47') == 1:
                new[2] = str(pricelist[i])

        return new

    else:
        return pricelist


session = requests.Session()

num = 1
url = []
while 1:
    link = 'https://ericksonsurfaces.com/collections/allfinishes?page=' + str(num)

    res = session.get(link)
    soup = bs(res.text, 'lxml')
    titlelink = soup.find_all('a', class_='product-link')
    if titlelink:
        y = ''
        for x in titlelink:
            id = 'https://ericksonsurfaces.com'
            if y == x.get('href'):
                pass
            if y != x.get('href'):
                y = x.get('href')
                id = id + y
                url.append(id)

    else:
        break

    num += 1


driver = webdriver.Safari()
SideList = []

for link in url:

    driver.get(link)
    btn = driver.find_elements_by_tag_name('option')
    SecondSide = ''

    for b in btn[1:]:
        if b.text.find('Small') == -1 and b.text.find('Medium') == -1 and b.text.find('Large') == -1 and b.text.find('"') == -1 :
            SecondSide += b.text + ", "
        else:
            break

    SideList.append(SecondSide)

    print(SecondSide)

driver.quit()


CREDIT_FILE = 'credentials.json'
spreadsheet_id = '1xH7sycIWoLiMKiTM1bvPIF_w69suOSBIYqCJk9KNE8s'
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    CREDIT_FILE,
    ['https://www.googleapis.com/auth/spreadsheets',
     'https://www.googleapis.com/auth/drive'])

httpAuth = credentials.authorize(httplib2.Http())
service = googleapiclient.discovery.build('sheets', 'v4', http = httpAuth)



sitePrice = []
for link, side in zip(url, SideList):

    b = []
    res = session.get(link)

    if res.status_code == 200:
        soup = bs(res.text, 'lxml')
        names = soup.find('h1', class_='section__title-text product-single__title-text')
        scripts = soup.find_all('script')


        price = ''
        for inf in scripts:
            if str(inf).find('ShopifyAnalytics') > 0:
                price = str(inf).split('var meta = ')[1]
                price = price.split("for (var attr in meta) {")[0].strip('')
                break

        jsonP = json.loads(price.replace(';', ''))
        pricelist = [round(int(d.get('price'))/100) for d in jsonP.get('product').get('variants')]
        sizelist = [d.get('public_title') for d in jsonP.get('product').get('variants')]

        pricelist = modifer(pricelist, sizelist)

        b.append(names.text)
        for i in pricelist:
            b.append(i)

        b.append(side)
        sitePrice.append(b)

    else:
        print("Sorry =( ")

values = service.spreadsheets().values().batchUpdate(
    spreadsheetId=spreadsheet_id,
    body={
        "valueInputOption": "USER_ENTERED",
        "data": [
            {"range": "A2:E",
             "majorDimension": "ROWS",
             "values": sitePrice},

	]
    }
).execute()



def compare(first, second, url, namelist, sizelist):

    flag = 0
    aval = 0
    change = 'Изменены следующие текстуры: '


    for one, link, name in zip(first, url, namelist):


        mark = 'Изменено: '
        for two in second:

            if name == two[0]:

                aval = 1

                for i, j, s in zip(one, two[4:], second[0][4:]):
                    try:

                        if str(i) != str(j):
                            print(i, j)
                            mark += s + ', '
                            flag = 1

                    except(IndexError):
                        break

                break

        if aval == 0:

            print('New Texture {}' + name)
            driver = webdriver.Safari()
            driver.get(link)
            btn = driver.find_elements_by_tag_name('option')
            SecondSide = ''

            for t in btn[1:]:
                if t.text.find('Small') == -1 and t.text.find('Medium') == -1 and t.text.find(
                        'Large') == -1 and t.text.find('"') == -1:
                    SecondSide += t.text + ", "
                else:
                    break
            driver.quit()

            new = ['' for u in range(4)]
            new[0] = name
            new[1] = SecondSide
            new[3] = 'Новая Текстура, '
            new.extend(one)

            second.append(new)

        if flag == 1:

            two[2] = mark
            change += str(two[0]) + ", "

        aval = 0
        flag = 0

    for two in second:

        aval = 0
        for name in namelist:

            if name == two[0]:
                aval = 1
                break

        if aval == 0:

            two[3] = 'Удалено'

    return second, change




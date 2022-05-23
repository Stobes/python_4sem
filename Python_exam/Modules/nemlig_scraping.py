from bs4 import BeautifulSoup
from requests_html import HTMLSession

def nemligList():

    URL = 'https://www.nemlig.com/?search=pepsi'


 
    session = HTMLSession()
    r = session.get(URL)

    r.html.render(sleep=1, keep_page=True)

    soup = BeautifulSoup(r.html.html,'lxml')



    print(soup.find_all('productlist-item__name'))

nemligList()
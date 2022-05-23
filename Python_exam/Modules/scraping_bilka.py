from bs4 import BeautifulSoup
from requests_html import HTMLSession

def scrape_list(prudct_list):

    product = []

    for elem in prudct_list:

        session = HTMLSession()

        URL = 'https://www.bilkatogo.dk/s?query=' + elem

        r = session.get(URL)

        r.html.render(sleep=1 , keep_page=True, scrolldown=1)

        #returner p elementer med class name
        productNames = r.html.find('p.name')
        #returnere elementer med class product-price
        productPrices = r.html.find('.product-price')
        #returnere det sidst span element
        kilog = r.html.find('span:last-child[data-v-8e411e84]')


        sub_category = []
        for i  in range(10):
            if '/' in kilog[i].text:
                sub_category.append(
                    [productNames[i].text, productPrices[i+1].text.replace(" ", "."), kilog[i].text.replace(",",".")]
                )
            else:
                None

        product.append(sub_category)
        
    return (product, prudct_list)    

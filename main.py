
# Import the required modules
import requests
from bs4 import BeautifulSoup
import json
import os


def json_from_html_using_bs4(base_url, pageNum):
    print(base_url)
    pageCurrent = 1
    page = requests.get(base_url)
    pageCount = pageNum
    soup = BeautifulSoup(page.text, "html.parser")

    books = soup.find_all(
        'a', attrs={'class':
                         'h3'})


    res = {
    }
    for index in books:
        data = {
            'title': '{0}'.format(index.text),
            'titleLink': str(index.get('href'))
        }
        json_string = json.dumps(data)
        with open('books.json', 'a', encoding='utf-8') as f:
            json.dump(data, f, indent=8, ensure_ascii=False)
            f.write(',')
            f.write('\n')

    print("Created Json File")
    if (len(books) > 0 and pageCount < 10387):
        pageCount += 25
        json_from_html_using_bs4("http://www.world-art.ru/animation/list.php?limit_1={0}".format(pageCount), pageCount)
if __name__ == "__main__":
    base_url = "http://www.world-art.ru/animation/list.php?limit_1=0"

    res = json_from_html_using_bs4(base_url, 0)
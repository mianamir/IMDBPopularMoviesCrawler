import requests
from bs4 import BeautifulSoup


def get_popular_movies_urls():
    """
    Will crawl IMDB popular movies page
    :return: list of urls
    """
    URL = 'https://www.imdb.com/chart/moviemeter?ref_=nv_mv_mpm'
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    data = []
    table = soup.find('table', attrs={'class': 'chart full-width'})
    table_body = table.find('tbody')
    rows = table_body.find_all('tr')
    for row in rows:
        a_tags = row.find_all('a')
        for a_single in a_tags:
            data.append(a_single['href'])
    return list(set(data))



from bs4 import BeautifulSoup
import requests


class Dashboard:
    def __init__(self, url):
        self.request = requests.get(url)
        print('This the package for retrive last news and conferences about radiology')

    def info(self):
        print('how to use this package:')
        print('package News for the recent news in auntminnie')
        print('package conferences for the recent conferences radiology in auntminnie')
        print('.test for testing the web')
        print('.data for take a data from web')
        print('.run for run .test and .data')

    def test(self):
        try:
            if self.request.status_code == 200:
                soup = BeautifulSoup(self.request.text, 'html.parser')
                print(f"{soup.find('title').string} is accsesable")
        except Exception:
            print("Can't accses web")

    def data(self):
        pass

    def run(self):
        self.test()
        self.data()


class News(Dashboard):
    def data(self):
        print('This is the recent news:')

        soup = BeautifulSoup(self.request.text, 'html.parser')
        news = soup.find_all('span', attrs={'class': 'Head'})
        for i in news:
            print(i.get_text())


class Conferences(Dashboard):
    def data(self):
        print('This is the recent Radiology Conferences:')

        soup = BeautifulSoup(self.request.text, 'html.parser')
        con = soup.find('div', attrs={'class': 'supBoxLoopCtrl'})
        con = con.findChildren('a')
        for i in con:
            print(i.text)
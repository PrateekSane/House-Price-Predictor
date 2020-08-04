from bs4 import BeautifulSoup as bs
import requests
import random


class HousePriceScraper:
    def __init__(self, is_scraping=False):
        self.homeLinks = []
        self.homeLinkPrice = {}
        self.homeData = []
        self.isScraping = is_scraping
        self.visited = {}
        self.count = 0
        self.mins = [300000, 400000, 500000, 600000, 700000, 800000, 900000, 1000000, 1250000]
        self.maxs = [500000, 600000, 700000, 800000, 900000, 1000000, 1250000, 1500000, 1750000]
        self.LANGUAGE = "en-US,en;q=0.5"
        self.session = requests.Session()
        self.user_agents = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
                            'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
                            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36',
                            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
                            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.83 Safari/537.1',
                            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
                            'Mozilla/5.0 (X11; U; Linux i686; pt-BR; rv:1.9.0.15) Gecko/2009102815 Ubuntu/9.04 (jaunty) Firefox/3.0.15',
                            'Mozilla/5.0 (SMART-TV; Linux; Tizen 2.4.0) AppleWebkit/538.1 (KHTML, like Gecko) SamsungBrowser/1.1 TV Safari/538.1',
                            'Mozilla/5.0 (iPhone; CPU iPhone OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 123.1.0.26.115 (iPhone12,1; iOS 13_3; en_US; en-US; scale=2.00; 828x1792; 190542906)',
                            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36",
                            'Mozilla/5.0 (Linux; U; Android 2.2) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
                            'Mozilla/5.0 (Linux; Android 9; SM-G950F Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.3729.157 Mobile Safari/537.36',
                            'Mozilla/5.0 (iPhone; CPU iPhone OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBIOS;FBDV/iPhone10,1;FBMD/iPhone;FBSN/iOS;FBSV/13.3.1;FBSS/2;FBID/phone;FBLC/en_US;FBOP/5;FBCR/]',
                            'Mozilla/5.0 CK={} (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
                            'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)',
                            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
                            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
                            'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36',
                            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',
                            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/605.1.15 (KHTML, like Gecko)',
                            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
                            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.5 Safari/605.1.15']
########################################################################################################################

    def session_set(self, url):
        ua = self.user_agents[random.randint(0, len(self.user_agents) - 1)]
        self.session.headers['User-Agent'] = ua
        self.session.headers['Accept-Language'] = self.LANGUAGE
        self.session.headers['Content-Language'] = self.LANGUAGE
        r = self.session.get(url)
        return r

    def create_search_soup(self, page, max_cost, min_cost, url_p1, url_p2, url_p3, url_p4,):
        url = url_p1 + str(page) + url_p2 + str(max_cost) + url_p3 + str(min_cost) + url_p4
        r = self.session_set(url)
        soup = bs(r.text, 'html.parser')
        return soup

    def create_home_soup(self, link):
        r = self.session_set(link)
        soup = bs(r.text, 'html.parser')
        return soup

########################################################################################################################
    def scrape_house_links(self, page_count):
        p1 = 'https://www.zillow.com/homes/95630_rb/?searchQueryState=%7B%22pagination%22%3A%7B%22currentPage%22%3A'
        p2 = '%7D%2C"usersSearchTerm"%3A"95630"%2C"mapBounds"%3A%7B"west"%3A-122.23061173828125%2C"east"%3A-120.071798261718' \
             '75%2C"south"%3A38.03589295136473%2C"north"%3A39.295539882121034%7D%2C"regionSelection"%3A%5B%7B"regionId"%3A98' \
             '325%2C"regionType"%3A7%7D%5D%2C"isMapVisible"%3Atrue%2C"mapZoom"%3A9%2C"filterState"%3A%7B"price"%3A%7B"max"%3A'
        p3 = '%2C"min"%3A'
        p4 = '%7D%2C"con"%3A%7B"value"%3Afalse%7D%2C"pmf"%3A%7B"value"%3Afalse%7D%2C"fore"%3A%7B"value"%3Afalse%7D%2C"apa"%' \
             '3A%7B"value"%3Afalse%7D%2C"sch"%3A%7B"value"%3Atrue%7D%2C"mf"%3A%7B"value"%3Afalse%7D%2C"mp"%3A%7B"max"%3A6027' \
             '%2C"min"%3A1730%7D%2C"sort"%3A%7B"value"%3A"priced"%7D%2C"auc"%3A%7B"value"%3Afalse%7D%2C"nc"%3A%7B"value"%3Af' \
             'alse%7D%2C"rs"%3A%7B"value"%3Atrue%7D%2C"land"%3A%7B"value"%3Afalse%7D%2C"tow"%3A%7B"value"%3Afalse%7D%2C"manu' \
             '"%3A%7B"value"%3Afalse%7D%2C"fsbo"%3A%7B"value"%3Afalse%7D%2C"cmsn"%3A%7B"value"%3Afalse%7D%2C"pf"%3A%7B"value' \
             '"%3Afalse%7D%2C"fsba"%3A%7B"value"%3Afalse%7D%7D%2C"isListVisible"%3Atrue%7D'

        if self.isScraping:
            for i in range(page_count):
                page = i + 1
                for max_cost in self.maxs:
                    soup = self.create_search_soup(page, max_cost, 0, p1, p2, p3, p4)
                    print(soup)
                    cur_link = ''
                    for house in soup.find_all('a', {'class': "list-card-link list-card-img"}):
                        cur_link = house.get('href')
                        self.count += 1
                        if cur_link not in self.visited:
                            self.homeLinks.append(cur_link)
                            self.visited[cur_link] = 1
                        else:
                            self.visited[cur_link] += 1
                    for price in soup.find_all('div', {'class': 'list-card-price'}):
                        temp = price.text
                        temp = temp.replace('$', '')
                        temp = temp.replace(',', '')
                        temp = temp.replace('M', '')
                        temp = float(temp)
                        if temp < 50000:
                            temp = temp*1000000
                        self.homeLinkPrice[cur_link] = temp
        if not self.isScraping:
            print('check if you want to Scrape')

    def scrape_home_data(self):
        if self.isScraping:
            self.scrape_house_links(20)
        else:
            self.read_home_links_list()
#       Add Checks: if bed/bath not there pop it. add label checks to match
        for link in self.homeLinks:
            soup = self.create_home_soup(link)
            temp = []
            school = []
            for data in soup.find_all('span', {'class': 'ds-bed-bath-living-area'}):
                val = data.find('span').text
                temp.append(val)
            temp = temp[0:3]
            for data in soup.find_all('span', {'class': "ds-body ds-home-fact-value"}):
                val = data.text
                temp.append(val)
            for data in soup.find_all('span', {'class': "Text-aiai24-0 Qookr"}):
                val = data.text
                school.append(val)
            for i in range(len(school)):
                if school[i] == 'K-5' or school[i] == '6-8' or school[i] == '9-12':
                    temp.append(school[i + 1])
            self.homeData.append(temp)
            print(self.homeData)
#            bed, bath, sq ft, type, year built, heating, cooling, parking, hoa, lot, elementary, middle, high

########################################################################################################################

    def write_home_links_list(self):
        f = open('homeLinksAndPrice.txt', 'w+')
        for link in self.homeLinkPrice:
            f.write(str(link) + ',\n')
        for link in self.homeLinkPrice:
            if self.homeLinkPrice[link] < 50000:
                self.homeLinkPrice[link] = 0
            f.write(str(self.homeLinkPrice[link]) + ',\n')

        f.close()

    def read_home_links_list(self):
        if not self.isScraping:
            f = open('homeLinksEdit.txt', 'r')
            lines = f.readlines()
            f.close()
            self.homeLinks = []
            for line in lines:
                self.homeLinks.append(line.strip(',\n'))
        if self.isScraping:
            print('Check if you want to ReScrape Data')

    def check_duplicates(self):
        check = {}
        self.read_home_links_list()
        for link in self.homeLinks:
            if link in check:
                check[link] += 1
            else:
                check[link] = 1
        max_link = max(check)
        print(check[max_link])
########################################################################################################################


if '__main__' == __name__:
    scraper = HousePriceScraper(is_scraping=True)
#   scraper.house_links(20)
#    print(len(scraper.homeLinks))
#    scraper.read_home_links_list()
#    scraper.check_duplicates()
#    scraper.scrape_home_data()
    scraper.scrape_house_links(1)
#    scraper.write_home_links_list()
    print(scraper.homeLinkPrice)
    print(scraper.count)



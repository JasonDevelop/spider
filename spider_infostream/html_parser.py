from bs4 import BeautifulSoup
import re
import urlparse
class htmlParser(object):

    def get_new_urls(self, page_url, soup):
        new_urls = set()
        '''
        links = soup.find_all('a', href = re.compile(r"/view/\d+\.htm"))
        for link in links:
            new_url = link['href']
            new_full_url = urlparse.urljoin(page_url, new_url)
            new_urls.add(new_full_url)
        return new_urls
        '''
        # <a href="/8hr/page/3?s=4896139" rel="nofollow">
        # <ul class="pagination">
        links = soup.find('ul', class_="pagination").find_all('a')
        for link in links:
            new_url = link['href']
            new_full_url = urlparse.urljoin(page_url, new_url)
            new_urls.add(new_full_url)
        return new_urls




    def get_new_data(self, page_url, soup):
        '''
        res_data = {}
        res_data['url'] = page_url

        # <dd class="lemmaWgt-lemmaTitle-title"> <h1>Python</h1>
        title_node = soup.find('dd', class_="lemmaWgt-lemmaTitle-title").find('h1')
        res_data['title'] = title_node.get_text()

        #<div class="lemma-summary" label-module="lemmaSummary">
        summary_node = soup.find('div', class_="lemma-summary")
        res_data['summary'] = summary_node.get_text()
        '''
        res_data_article_set = set()
        article_nodes = soup.find_all('div', class_="article block untagged mb15")

        for article_node in article_nodes:
            res_data_article_set.add(article_node.find('div', class_="content").get_text())
        return res_data_article_set

    def parse(self, page_url, html_content):
        if page_url is None or html_content is None:
            return
        soup = BeautifulSoup(html_content, 'html.parser', from_encoding= 'utf-8')

        new_urls = self.get_new_urls(page_url, soup)
        new_data_set = self.get_new_data(page_url, soup)

        return new_urls, new_data_set
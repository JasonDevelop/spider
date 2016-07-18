# coding : utf8
import html_downloader
import html_outputer
import html_parser
import url_manager


class spiderMain(object):
    def __init__(self):
        self.urls = url_manager.urlManager()
        self.downloader = html_downloader.htmlDownloader()
        self.parser = html_parser.htmlParser()
        self.outputer = html_outputer.htmlOutputer()


    def craw(self, root_url):
        self.urls.add_new_url(root_url)
        #count = 1
        pagecount = 1
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()

                print 'craw page %d : %s' % (pagecount, new_url)
                html_content = self.downloader.download(new_url)
                new_urls, new_data_set = self.parser.parse(new_url, html_content)
                print new_urls
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data_set)
                if pagecount == 5:
                    break
                pagecount = pagecount + 1
            except:
                print 'craw failed'

        self.outputer.output_html()






if __name__ == "__main__":
    #root_url = "http://baike.baidu.com/view/21087.htm"
    root_url = "http://www.qiushibaike.com/hot/"
    obj_spider = spiderMain()
    obj_spider.craw(root_url)



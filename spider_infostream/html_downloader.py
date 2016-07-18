import urllib2

class htmlDownloader(object):

    def download(self, url):

        if url is None:
            return None

        print url
        #url = 'http://www.qiushibaike.com/hot/page/' + str(page)
        user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        headers = { 'User-Agent' : user_agent }
        request = urllib2.Request(url, headers = headers)
        response = urllib2.urlopen(request)

        print response.getcode()
        if response.getcode() != 200:
            return None
        #print response.read()
        return response.read()

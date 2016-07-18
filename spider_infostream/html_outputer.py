__author__ = 'Jason'


class htmlOutputer():

    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)
    def collect_data(self, data_set):
        if data_set is None:
            return
        for data in data_set:
            self.datas.append(data)
    def output_html(self):
        fout = open('data.html', 'w')
        fout.write('<html>')
        fout.write("<head><meta http-equiv='content-type' content='text/html;charset=utf-8'></head>")
        fout.write('<body>')
        fout.write('<table>')
        for data in self.datas:
            fout.write('<tr>')
            '''
            fout.write('<td> %s </td>'% data['url'])
            fout.write('<td> %s </td>'% data['title'].encode('utf-8'))
            fout.write('<td> %s </td>'% data['summary'].encode('utf-8'))
            '''
            fout.write('<td> %s </td>'% data.encode('utf-8'))
            fout.write('</tr>')
        fout.write('</html>')
        fout.write('</body>')
        fout.write('</table>')



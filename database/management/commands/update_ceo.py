import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtWebKit import *
import re
import requests
from database.models import Company

class Render(QWebPage):

    def __init__(self, url):
        self.app = QApplication(sys.argv)
        QWebPage.__init__(self)
        self.loadFinished.connect(self._loadFinished)
        self.mainFrame().load(QUrl(url))
        self.app.exec_()

    def _loadFinished(self, result):
        self.frame = self.mainFrame()
        self.app.quit()
all_companies = Company.objects.all()
for company in all_companies:
    company_name = company.name
    print "-------input-------"
    print company.name
    print company.ceo
    print "-----------------"
    # url = 'http://www.google.com/search?hl=en-IN&source=hp&biw=&bih=&q=' + company_name + '+company+ceo'
    url = 'http://www.google.com/search?start=0&num=10&q=' + company_name + '+company+ceo+name'
    print url
    r = Render(url)
    html = unicode(r.frame.toHtml()).encode('utf-8')
    print html
    result = re.search('class="_m3b">(.*)</', html)
    ceo_name = result.group(1).split("</")[0]
    print "-------output-------"
    print company.name
    print ceo_name

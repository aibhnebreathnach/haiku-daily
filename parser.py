# Utility class to parse the HTML from randomhaiku.com
# and get sections of haiku for later use.

from HTMLParser import HTMLParser
import urllib2


class Parser(HTMLParser):

    def __init__(self):
        HTMLParser.__init__(self)
        self.inLink = False
        self.lasttag = None

    def handle_starttag(self, tag, attrs):
        if tag == "div":
            for name, value in attrs:
                if name == "class" and value == "line":
                    self.inLink = True
                    self.lasttag = tag

    def handle_endtag(self, tag):
        if tag == "div":
            self.inLink = False

    def handle_data(self, data):
        if self.lasttag == "div" and self.inLink and data.strip():
            print data

# Get raw HTMl for parsing
def get_raw_html(url):
    page = urllib2.urlopen(url)
    return page.read()


text = get_raw_html("http://www.randomhaiku.com/")

parser = Parser()
parser.feed(text)
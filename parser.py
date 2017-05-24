# Utility class to parse the HTML from randomhaiku.com
# and get sections of haiku for later use.

from HTMLParser import HTMLParser
import urllib2

# Set of 5 and 7 syllable phrases - no duplicates
fives = set()
sevens = set()

class Parser(HTMLParser):

    def __init__(self):
        HTMLParser.__init__(self)

        self.inElement = False
        self.lasttag = None

        # List of haiku parsed from website
        self.haiku = []

    def handle_starttag(self, tag, attrs):
        if tag == "div":
            for name, value in attrs:
                if name == "class" and value == "line":
                    self.inElement = True
                    self.lasttag = tag

    def handle_endtag(self, tag):
        if tag == "div":
            self.inElement = False

    def handle_data(self, data):
        if self.lasttag == "div" and self.inElement and data.strip():
            self.haiku.append(data)

    # Split haiku into 5s and 7s
    def split_haiku(self):
        fives.add(self.haiku[0])
        sevens.add(self.haiku[1])
        fives.add(self.haiku[2])
        self.haiku[:] = [] # Clear haiku list


# Get raw HTMl for parsing
def get_raw_html(url):
    page = urllib2.urlopen(url)
    return page.read()

# Write 5 and 7 syllable phrases to their files
def write_fives(fives):
    f = open("data/5s.txt", "a") # "a" for append
    for i in set(fives):
        string = i + "\n"
        f.write(string)
    f.close()

def write_sevens(sevens):
    f = open("data/7s.txt", "a") # "a" for append
    for i in set(sevens):
        string = i + "\n"
        f.write(string)
    f.close()

# Remove duplicate lines from 5 and 7 files
def remove_duplicates(filepath):
    lines = open(filepath).readlines()
    uniqlines = set(lines)
    uniqout = open(filepath, 'w').writelines(set(uniqlines))



parser = Parser()
for i in range(0,100):
    html_raw = get_raw_html("http://www.randomhaiku.com/")
    print 'Roation: ', i
    parser.feed(html_raw)
    parser.split_haiku()

write_fives(fives)
write_sevens(sevens)

remove_duplicates('data/7s.txt')
remove_duplicates('data/5s.txt')

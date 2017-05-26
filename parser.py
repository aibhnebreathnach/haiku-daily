# Utility class to parse the HTML from randomhaiku.com
# and get sections of haiku for later use.
from lxml import html
import requests, sys

# Set of 5 and 7 syllable phrases - no duplicates
fives = set()
sevens = set()

class Parser():

    def __init__(self):

        self.inElement = False
        self.lasttag = None

        # List of haiku parsed from website
        self.haiku = []


    def parse_haiku(self, tree):
        self.haiku = tree.xpath('//div[@class="line"]/text()')

    # Split haiku into 5s and 7s
    def split_haiku(self):
        fives.add(self.haiku[0])
        sevens.add(self.haiku[1])
        fives.add(self.haiku[2])

        # Clear haiku list, to only need
        # one parser object for many GETs
        self.haiku[:] = []


# Get tree of html tags for processing
def get_html_tree(url):
    page = requests.get(url)
    return html.fromstring(page.content)

# Write 5 and 7 syllable phrases to their files
def write_fives(fives):
    f = open('data/5s.txt', 'a') # 'a' for append
    for i in set(fives):
        string = i + '\n'
        f.write(string)
    f.close()

def write_sevens(sevens):
    f = open('data/7s.txt', 'a') # 'a' for append
    for i in set(sevens):
        string = i + '\n'
        f.write(string)
    f.close()

# Remove duplicate lines from 5 and 7 files
def remove_duplicates(filepath):
    lines = open(filepath).readlines()
    uniqlines = set(lines)
    uniqout = open(filepath, 'w').writelines(set(uniqlines))


# Controller
parser = Parser()
count = int(sys.argv[1])
for i in range(0, count):
    html_tree = get_html_tree("http://www.randomhaiku.com/")
    print 'Roation: ', i
    parser.parse_haiku(html_tree)
    parser.split_haiku()

write_fives(parser.fives)
write_sevens(parser.sevens)

remove_duplicates('data/5s.txt')
remove_duplicates('data/7s.txt')

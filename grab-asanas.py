import urllib
# Get a file-like object for the Python Web site's home page.

base_url  = 'http://www.yinyoga.com/'
image_url = base_url + 'images/'
asana_index_url = base_url + "ys2_2.0_yinyoga_asanas.php"

html = urllib.urlopen(asana_index_url).read()

from BeautifulSoup import BeautifulSoup

soup = BeautifulSoup(html)
#print soup.prettify()

lis = soup.findAll('li')

import re

asanas = []

for li in lis:
    asana = {}
    a = li.find('a')
    print a['href'], "\t", a.string
    asana['title'] = a.string
    asana['page_url'] = base_url + a['href']
    asana_page_html = urllib.urlopen(asana['page_url']).read()
    soup = BeautifulSoup(asana_page_html)
    img = soup.find('img', src=re.compile('asana.+gif'))
    #print "\t", img, img['src']
    asana['img_url'] = base_url + img['src']
    asanas.append( asana )

import json

print json.dumps(asanas, indent=4)

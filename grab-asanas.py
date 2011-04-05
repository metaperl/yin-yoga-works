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
    asana['name'] = a.string
    asana['page_url'] = base_url + a['href']
    asana_page_html = urllib.urlopen(asana['page_url']).read()
    soup = BeautifulSoup(asana_page_html)
    img = soup.find('img', src=re.compile('asana.+gif'))
    #print "\t", img, img['src']
    asana['img_url'] = base_url + img['src']
    asanas.append( asana )

import json

print json.dumps(asanas, indent=4)

from lxml import etree
root = etree.Element("asanas")

def textelem(tag_name, text):
    e = etree.Element(tag_name)
    e.text = text
    return e

for asana in asanas:
    ae = etree.Element("asana")
    for key in asana:
        tmp = textelem(key, asana[key])
        ae.append(tmp)
    root.append(ae)

print(etree.tostring(root, pretty_print=True))



# import sys
# sys.path.append('/home/thequietcenter/prg/web2py')

# from gluon.dal import DAL, Field

# db = DAL('sqlite://storage.db')

# db.asanas.bulk_insert(asanas)



import requests
import lxml.html
from lxml import etree

tree = etree.parse('123.html', lxml.html.HTMLParser())

text = tree.xpath('/html/body/tag1/tag2/text()')

print(text)


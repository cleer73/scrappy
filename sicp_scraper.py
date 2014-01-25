#!/usr/bin/env python
# -*- coding: utf-8 -*-

from BeautifulSoup import BeautifulSoup

import requests
import re

BASE_URL = 'http://mitpress.mit.edu/sicp/full-text/book/'
INDEX_PAGE = 'book-Z-H-4.html'

def savePage(name, content):
    page = open('./html/%s' % name, 'w')
    page.write(content)
    page.close()

def fetchPage(name):
    try:
        page = open('./html/%s' % name, 'r')
    except IOError:
        url = '%s/%s' % (BASE_URL, name)
        print '  [@] HTTP GET: %s' % url
        response = requests.get(url)
        html = response.text
    else:
        print '  [*] Cached File: %s' % name
        html = page.read()

    savePage(name, html)
    return html

def processingMessage(name):
    print
    print "@ PROCESS: %s" % name


if __name__ == "__main__":
    processingMessage(INDEX_PAGE)
    index = BeautifulSoup(fetchPage(INDEX_PAGE))

    pages = []

    for link in index.findAll('a'):
        name = link.get('href')
        if name:
            pageName = name.split("#")[0]
            if pageName not in pages and pageName != 'book.html':
                pages.append(pageName)
        else:
            print '  [!] ERROR: %s' % (link)

    for name in pages:
        processingMessage(name)
        html = fetchPage(name)
    #     html = modifyPage(html)
    #     # print html

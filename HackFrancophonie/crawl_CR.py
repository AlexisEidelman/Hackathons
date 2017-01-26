# -*- coding: utf-8 -*-
"""
Crée pendant le HackFrancophonie

###############################################################################
Ce script va chercher les pages de conseil des ministres depuis la liste des liens
récupérée à partir de crawl pui extract_list_CR.
Tout est lié au site lefaso.net

"""
import cookielib
import urllib2
import os

url_opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookielib.CookieJar()))


list_pages = open('list_pages.txt').read().split('\n')

for page in list_pages:
  url = 'http://lefaso.net/' + page
  try:
    request = urllib2.Request(url)
    response = url_opener.open(request)
  except:
    print('erreur : ', url)
    continue
    #TODO: on devrait tester le 404 plutot que ce try except
  html_page =  response.read()
  with open(os.path.join('CR', page[16:] +  '.html'), 'w') as f:
      f.write(html_page)


import pdb; pdb.set_trace()

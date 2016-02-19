# -*- coding: utf-8 -*-
"""
Crée pendant le HackFrancophonie

###############################################################################
Ce script récupère les conseils du ministre sur le site lefaso.net

"""

import cookielib
import urllib2
import os


base_url = "http://lefaso.net/spip.php?rubrique64&debut_articles="

url_opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookielib.CookieJar()))

list_conseil_ministre = []
erreur_404 = []
i = 1
while True:
  url = base_url + str(i)
  try:
    request = urllib2.Request(url)
    response = url_opener.open(request)
  except:
    erreur_404 += [i]
    print('erreur : ', i)
    i += 1
    continue
    #TODO: on devrait tester le 404 plutot que ce try except
  html_page =  response.read()
  if "Compte rendu du Conseil des ministres" in html_page:
    list_conseil_ministre += [i]
  with open(os.path.join('rubrique', str(i) +  '.html'), 'w') as f:
      f.write(html_page)
  if i % 10 == 0:
    print(i)
  i += 20

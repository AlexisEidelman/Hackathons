# -*- coding: utf-8 -*-
"""
Crée pendant le HackFrancophonie

###############################################################################
Ce script récupère les pages des comptes rendus du conseils du ministre
à partir des rubriques (voir crawl)

"""
import os
import re

path = 'rubrique'
list_pages = []

def scrap(file):
  text = open(file).read()
  list_links = re.findall('spip.php\?article\d+', text)
  list_links = list(set(list_links))
  return list_links

for html in os.listdir(path):
  list_de_la_page = scrap(os.path.join(path,html))
  list_pages += list_de_la_page


list_pages = list(set(list_pages))
with open('list_pages.txt', 'w') as f:
    f.write('\n'.join(list_pages))

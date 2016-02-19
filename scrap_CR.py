# -*- coding: utf-8 -*-
"""
Crée pendant le HackFrancophonie

###############################################################################
Ce script récupère les pages des comptes rendus du conseils du ministre
à partir des rubriques (voir crawl)

"""
import os
import re
from bs4 import BeautifulSoup


path = 'CR'
list_pages = []

## on commence par les titres économies et finance


#Ministère des Finances et du Budget
i = 0
def scrap(file, substract):
  list_links = []
  text = open(file).read()
#  print substract in text
#  soup = BeautifulSoup(text)
#  import pdb; pdb.set_trace()
  
  if substract in text:
    # list_links = re.findall(substract, text)
    # list_links = list(set(list_links))
    list_links += [file]
  else:
    print(file)
  return list_links

def files_containing(substract, path):
    list_pages = []
    for html in os.listdir(path):
      list_de_la_page = scrap(os.path.join(path,html), substract)
      list_pages += list_de_la_page

    list_pages = list(set(list_pages))
    return list_pages





if __name__ == 'main':

    substract = "F CFA"
    
    list_pages = files_containing(substract, path)
    print(len(list_pages))

    with open(substract + '.txt', 'w') as f:
        f.write('\n'.join(list_pages))
    
    print len(os.listdir(path))

# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26 11:37:39 2016

@author: aeidelman
"""

import os
import json

path = '/home/sgmap/data/DatacampAN/'

path_qg = os.path.join(path, 'AN', 'Questions_gouvernement_XIV.json')

with open(path_qg) as qg_file:
    data = json.load(qg_file)

qg = data['questionsGvt']['question']
assert isinstance(qg, list)

caracteristiques_question = ['renouvellements', 'auteur', 'type',
                             'indexationAN', 'textesQuestion', 'identifiant',
                             'signalement', 'minAttribs', 'uid',
                             'minInt', 'cloture', 'textesReponse']

all_texts = ''

for idx in range(len(qg)):
    exemple = qg[idx]
    texte = exemple['textesReponse']['texteReponse']['texte']
    assert exemple['type'] in ['QG']   

    dest = os.path.join(path, 'AN', 'html', str(idx) + '.html')
    with open(dest, 'w', encoding='utf8') as output:
       output.write(texte)

    all_texts += texte + 7*'\n'


extract_text = all_texts.split(7*'\n')
size = int(len(extract_text)/10)
extract_text = extract_text[:size]
extract_text = 7*'\n'.join(extract_text)

dest_all = os.path.join(path, 'AN', 'all.html')
with open(dest_all, 'w', encoding='utf8') as output:
   output.write(extract_text)

# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26 09:13:40 2016

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
def load(param):
    assert param in ['qe', 'qg']
    

qe = qg
param = 'qg'
exemple = qg[123]
assert all([x in caracteristiques_question for x in exemple.keys()])
assert len(exemple.keys()) in [9, 12] # 12 pour les qe, 9 pour les qg

auteur = exemple['auteur']
groupe = auteur['groupe']
identite = auteur['identite']

indexationAN = exemple['indexationAN']
analyses = indexationAN['analyses']
rubrique = indexationAN['rubrique']
teteAnalyse = indexationAN['teteAnalyse']

if param == 'qe':
    texte = exemple['textesQuestion']['texteQuestion']['texte']
    date = exemple['textesQuestion']['texteQuestion']['infoJO']['dateJO']
    assert exemple['type'] in ['QE']
if param == 'qg':
    texte = exemple['textesReponse']['texteReponse']['texte']
    assert exemple['type'] in ['QG']   

with open(str(idx) + '.html', 'w', encoding='utf8') as output:
   output.write(texte)

identifiant = exemple['identifiant']

minAttribs = exemple['minAttribs']
minInt = exemple['minInt']

cloture = exemple['cloture']

textesReponse = exemple['textesReponse']

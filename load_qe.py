# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26 09:13:40 2016

@author: aeidelman
"""
import os
import json
import pandas as pd

path = '/home/sgmap/data/DatacampAN/'

path_qe = os.path.join(path, 'AN', 'Questions_ecrites_XIV.json')

with open(path_qe) as qe_file:
    data = json.load(qe_file)

qe = data['questionsEcrites']['question']
assert isinstance(qe, list)

test = pd.DataFrame(qe)


def is_dict(serie):
    is_dict = serie.apply(lambda x: isinstance(x, dict) or isinstance(x, list))
    return all(is_dict)

def serie_of_dict_to_df(serie):
    if not is_dict(serie):
        return serie
    # assert all(is_dict)
    
    # c'est un bug parfois on a des listes
    cond = serie.apply(lambda x: isinstance(x, list))
    serie[cond] = serie[cond].str.get(0)

    # c'est pas un bug parfois,il y a des None
    serie2 = pd.DataFrame(list(serie))
    return serie2



def dict_to_df(df):
    columns = [df[col] for col in df.columns]
    is_col_dict = [is_dict(col) for col in columns]
    for col in df.columns[is_col_dict]:
        new_col = serie_of_dict_to_df(df[col])
        if isinstance(new_col, pd.Series):
            df[col] = col
        else:
            new_col1 = dict_to_df(new_col)
            del df[col]
            df = pd.concat([df, new_col1], axis=1)
    return df

auteur = dict_to_df(test)
auteur.columns = auteur.columns.tolist()[:6] + ['parti','nom_parti'] + auteur.columns.tolist()[8:]
to_keep = [x for x in range(19)] + [21,22,23]

auteur = auteur.iloc[:, to_keep]

repondu = auteur[auteur['cloture'].notnull()].reset_index()
reponse = serie_of_dict_to_df(repondu['cloture'])
cloture = pd.to_datetime(reponse['dateCloture'], format='%Y-%m-%d')
debut = pd.to_datetime(repondu['dateJO'], format='%Y-%m-%d')

repondu['temps'] = (cloture - debut)/pd.to_timedelta('1d')

import numpy as np
parti_dev = repondu.groupby(['nom_parti','developpe'])['temps'].agg([np.mean, 
                            lambda x : len(x)])
parti_dev.reset_index().to_csv('parti_dev_temps_moyen.csv', index=False)

parti = repondu.groupby(['nom_parti'])['temps'].agg([np.mean, lambda x : len(x)])
parti.reset_index().to_csv('parti_temps_moyen.csv', index=False)

parti = repondu.groupby(['developpe'])['temps'].agg([np.mean, lambda x : len(x)])
parti.reset_index().to_csv('developpe_temps_moyen.csv', index=False)

parti = repondu.groupby(['abrege'])['temps'].agg([np.mean, lambda x : len(x)])
parti.reset_index().to_csv('abrege_temps_moyen.csv', index=False)
xxx


caracteristiques_question = ['renouvellements', 'auteur', 'type',
                             'indexationAN', 'textesQuestion', 'identifiant',
                             'signalement', 'minAttribs', 'uid',
                             'minInt', 'cloture', 'textesReponse']
exemple = qe[95749]

assert all([x in caracteristiques_question for x in exemple.keys()])
assert len(exemple.keys()) == 12

auteur = exemple['auteur']
groupe = auteur['groupe']
identite = auteur['identite']

indexationAN = exemple['indexationAN']
analyses = indexationAN['analyses']
rubrique = indexationAN['rubrique']
teteAnalyse = indexationAN['teteAnalyse']

texte = exemple['textesQuestion']['texteQuestion']['texte']
date = exemple['textesQuestion']['texteQuestion']['infoJO']['dateJO']
assert exemple['type'] == 'QE'

identifiant = exemple['identifiant']

minAttribs = exemple['minAttribs']
minInt = exemple['minInt']

cloture = exemple['cloture']

textesReponse = exemple['textesReponse']


    
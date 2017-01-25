# -*- coding: utf-8 -*-

import os
import pandas as pd

path_data = '/home/sgmap/data'

## Ambassades
# données téléchargées sur data.gouv.fr

path_ambassades_csv = os.path.join(path_data, 'MAEDI', 'representations_francaises.csv')
amb = pd.read_csv(path_ambassades_csv, encoding='cp1252', sep=';')
# => 101 ambassades


# Annuaire
# csv chargé depuis le travail fait et reposté sur data.gouv.fr
path_dila = os.path.join(path_data, 'annuaire', 'annuaire_20160712.csv')
dila = pd.read_csv(path_dila)
# on cherche les ambassades
contains_amb = dila['http://www.w3.org/2000/01/rdf-schema#label'].str.contains('stitut fr')
#mieux :
contains_amb = dila['parent'] == 'an/171940'

# dila['enfant'] == dila['index']
columns_to_remove = ['enfant', 'df/formulaireContactHerite',
                     'df/coordonneeComplementaireHeritee', ]
del dila['enfant']
for col in dila.columns:
    if dila.loc[contains_amb, col].nunique() > 1 :
        print(dila.loc[contains_amb, col].value_counts())

label = dila.loc[contains_amb, 'http://www.w3.org/2000/01/rdf-schema#label']
assert all(label.str.startswith('Ambassade de France '))
label = label.str[20:]
assert all(label.str.split(' - ').str.len() == 2)
pays = label.str.split(' - ').str[0].str.upper()
pays = pays.str.replace('É', 'E')
ville = label.str.split(' - ').str[1]
ville = ville.str.replace('-', ' ')

#### Début de comparaison
#on regarde sur un pays
amb['Pays']
Pays_amb = amb['Pays']
# Pas d'accent !!!
amb['Ville'] # contient des dates, Majuscule en 1ere lettre
ville.isin(amb['Ville'])


len(pays[~pays.isin(amb['Pays'])])

len(ville[~ville.isin(amb['Ville'])])
# 40 villes
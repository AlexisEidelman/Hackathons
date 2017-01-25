On travaille avec annuaire_ambassade.py pour voir si les
ambassades du [fichier des représentations](http://www.data.gouv.fr/fr/datasets/coordonnees-des-representations-diplomatiques/)
publié par le MAEDI sont cohérentes avec les données de l'annuaire de
l'administration publié par la dila (voir le repo Annuaire du Github
AlexisEidelman).


Pour réaliser le rapprochement des deux bases de données, on essaie de
jouer sur les champs Pays et Ville que l'on peut identifier dans chaque base.
Malheureusement, ces deux données ne repectent pas du tout le même
standard.

Cela est bien dommage car il existe une base [états et capitales du monde](http://www.data.gouv.fr/fr/datasets/etats-et-capitales-du-monde/)
publiée par le MAE sur data.gouv.fr qui pourrait servir de référentiel pour
les dénominations géographiques françaises.


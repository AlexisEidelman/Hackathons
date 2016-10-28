# Proposition de traitements des arrêtés

Les arrêtés définissant les bureaux de votes sont disponibles sous forme de fichiers PDF (scans).

Le problème étant complexe, appliquons le principe du "diviser pour régner" et découpons-le en sous problèmes plus simples à résoudre séparément.

## Etape 1: OCR (PDF -> TXT)

Cette étape permet de récupérer le texte (approximatif) contenu dans les scans PDF.


## Etape 2: extraction des données voies/adresses par bureau de vote (TXT -> CSV)

L'objectif est d'analyser le contenu du texte et d'obtenir en final des données tabulaires homogènes.

Pour quelques communes, un exemple de fichier CSV cible a été fait (à la main) pour permettre de travailler sur l'étape suivante.


## Etape 3: transformation en découpage géographique (CSV -> GéoJson)

A partir des données CSV extraite des PDF des arrêtés, il faut faire l'appariement avec les tronçons de voies et adressespour obtenir les contours correspondants à chaque bureau de vote.

L'objectif ici est de produire un fichier géographique (geojson, shapefile, etc).

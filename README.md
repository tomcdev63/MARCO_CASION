# CARS 🚗


![Screenshot](https://github.com/tomcdev63/MARCO_CASION/blob/main/IMG/E1_marco_casion_DEMO.gif?raw=true)


<!-- PROJECT LOGO -->
<br />
<p align="center">


<!-- SOMMAIRE -->
## Sommaire 📋

* [Contexte_du_projet](#contexte_du_projet)
  * [Construit_avec](#Construit_avec)
* [Installation](#Installation)
  * [Usage](#usage)
* [Sources](#sources)
  * [Création d’une API](#creation_dune_api)
* [Annexes](#annexes)
 

<!-- CONTEXTE DU PROJET -->
## Contexte_du_projet

La société « Marco Casion » achète des voitures d’occasion en Inde. 
Marco (gérant de la société) avait pour habitude de faire des offres de reprise via un questionnaire et une réponse par email.
Pour gagner du temps et rendre son offre plus attractive, il a décidé de moderniser son process en donnant une réponse immédiate via son site internet à l’aide d’un formulaire qui prend en compte un certain nombre de critères. Afin d’attirer les vendeurs, Marco propose des prix de rachat 9% plus élevés que la moyenne observée pour ce même véhicule en Inde. 
C’est dans ce cadre qu’il vous sollicite pour réaliser l’application qui permettra à tout vendeur de véhicule d’occasion de connaître le tarif de rachat de son véhicule par « Marco Casion ».
En termes de données, cette société met à disposition une base de données relationnelle qui contient les caractéristiques des véhicules d’occasion en Inde et leur prix de vente.

<!-- CONSTRUIT AVEC -->
## Construit_avec 

* [Anaconda](https://www.anaconda.com/)

<!-- INSTALLATION -->
## Installation

* Clone du repos

    ```sh
    git clone https://github.com/tomcdev63/ML.git
    ```

* Création de l'environnement Python

    ```sh
    conda create --name myenv
    ```

* Chargement de l'environnement 

    ```sh
    conda env update -n myenv --file environment.yml
    ```
    
<!-- USAGE -->
## Usage 
 
* ```src/app/00_CLEAN_BDD.ipynb``` - Notebook concernant l'import des données et un premier nettoyage rapide.
* ```src/app/00_MAIN_BDD.ipynb``` - Création de modèles de regression et de leur améliorations via des méthodes de Cleaning, Feature engineering etc.
* Afin de lancer le site internet en mode local via FASTAPI, rendez-vous dans un CMD --> ```cars/src/app``` puis exécuter la commande ci-dessous : 

    ```sh
    uvicorn main:app --reload
    ```
![Screenshot](https://github.com/tomcdev63/MARCO_CASION/blob/main/IMG/Capture.JPG?raw=true)

<!-- MODELES -->
## Modèles
* ```data/models/linear_regression_best_78%``` - modèle de Regression Linéaire avec un r2 à 78%  
* ```data/models/random_forest_regressor_best_89%``` - modèle de Random Forest Regressor avec un r2 à 89%

<!-- SOURCES -->
## Sources

* https://fr.wikipedia.org/wiki/Régression_linéaire#:~:text=Comme%20les%20autres%20modèles%20de,des%20valeurs%20particulières%20de%20x
* https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html
* https://help.tableau.com/current/pro/desktop/fr-fr/calculating_z_scores.htm
* https://medium.com/swlh/random-forest-and-its-implementation-71824ced454f

## Plan de la base de données relationnelle

![Screenshot](https://github.com/tomcdev63/MARCO_CASION/blob/main/IMG/14.JPG?raw=true)

## Mise en place de techniques de monitoring

Grâce à la librairie MLFlow les divers tests concernant les algorithmes employés ainsi que leurs hyperparamètres (voir Annexe 8) ont pu être sauvegardés au sein d’une interface graphique. Cela a pour but d’avoir une représentation visuelle et graphique de l’ensemble des essais effectués ainsi que de détecter et corriger les éventuels dysfonctionnements et anomalies pouvant survenir.
Après avoir fait tourner le notebook regroupant les différents algorithmes d’IA, il suffit alors de lancer le serveur local MLFlow et de se rendre dans le dossier src/app/, puis d’exécuter la commande :  
 
```mlflow ui``` 


## Création d’une API

Afin de répondre au mieux à la demande du client, un site internet intégrant un module d'estimation (indiquant le prix moyen d'une voiture d'occasion reprise en Inde et celui appliqué par la société "MARCO CASION" : 9% de plus) a été mis en place grâce au framework FastAPI.   
Ainsi les futurs vendeurs désireux de connaitre le prix de rachat de leur véhicule par la société Marco Casion n’auront plus qu’à se rendre sur le site de Marco et indiquer les différents critères de leur véhicule afin d’avoir une estimation du prix de rachat de celui-ci.  
Ce site est accessible en ligne à l’adresse :   
⦁	http://ml.car.tomdev.ovh/   
Ou de manière locale, en se rendant dans le dossier src/app/ et en exécutant la commande :  
 
```uvicorn main:app```

De plus, afin de permettre à Marco de conserver un historique des différentes demandes des éventuels futurs vendeurs, une nouvelle table a été créée au sein de la base de données relationnelles fournie. Celle-ci permet en parallèle d'alimenter la base de données originale de nouvelles données :)
 
![Screenshot](https://github.com/tomcdev63/MARCO_CASION/blob/main/IMG/15.JPG?raw=true)
![Screenshot](https://github.com/tomcdev63/MARCO_CASION/blob/main/IMG/E1_marco_casion_DEMO.gif?raw=true)

## Annexes

⦁	Annexe 1 : Normalisation des données
Source : 
https://dataanalyticspost.com/Lexique/normalisation/#:~:text=Normalisation%20%3A%20La%20normalisation%20est%20une,l'application%20de%20certains%20algorithmes.⦁	&⦁	text=Cette%20m%C3%A9thode%20a%20en%20outre,dans%20la%20fouille%20de%20donn%C3%A9es.   
Normalisation : La normalisation est une méthode de prétraitement des données qui permet de réduire la complexité des modèles. C'est également un préalable à l'application de certains algorithmes. ... Cette méthode a en outre de nombreuses applications dans la fouille de données.

⦁	Annexe 2 : MinMaxScaler
Transforme les entités en adaptant chaque entité à une plage donnée. Cet estimateur met à l'échelle et traduit chaque caractéristique individuellement de telle sorte qu'elle se situe dans la plage donnée sur l'ensemble d'apprentissage, par exemple entre zéro et un.

⦁	Annexe 3 : OneHotEncoder
Encode les caractéristiques catégorielles sous la forme d'un tableau numérique unique. L'entrée de ce transformateur doit être un tableau d'entiers ou de chaînes, indiquant les valeurs prises par les caractéristiques catégorielles (discrètes). Les caractéristiques sont encodées à l'aide d'un schéma d'encodage one-hot (alias 'one-of-K' ou 'dummy'). Cela crée une colonne binaire pour chaque catégorie et renvoie une matrice clairsemée ou un tableau dense.

⦁	Annexe 4 : Hyperparamètres
Sources :
⦁	https://fr.wikipedia.org/wiki/Hyperparam%C3%A8tre  

Dans l'apprentissage automatique, un hyperparamètre est un paramètre dont la valeur est utilisée pour contrôler le processus d'apprentissage. En revanche, les valeurs des autres paramètres (généralement la pondération de nœuds) sont obtenues par apprentissage.
Un exemple d'hyperparamètre de modèle est la topologie et la taille d'un réseau de neurones. Des exemples d'hyperparamètres d'algorithme sont la vitesse d'apprentissage et la taille des lots.
Les différents hyperparamètres varient en fonction de la nature des algorithmes d'apprentissage, par exemple certains algorithmes d'apprentissage automatique simples (comme la régression des moindres carrés) n'en nécessitent aucun. Compte tenu de ces hyperparamètres, l'algorithme d'apprentissage apprend les paramètres à partir des données. Par exemple, la régression LASSO est un algorithme qui ajoute un hyperparamètre de régularisation à la régression des moindres carrés, qui doit être défini avant d'estimer les paramètres via l'algorithme d'apprentissage.

⦁	Annexe 5 : Score (MAE, RMSE, R2)
MAE : Différence absolue entre les vraies valeurs et les valeurs prédites.
MSE : Moyenne des écarts au carré entre les vraies valeurs et les valeurs prédites.
RMSE : Correspond à la racine carrée du MSE.
Median ABS error : Médiane des différences absolues des erreurs.
CV mean : Moyenne des différents score R2 produits après avoir effectué un GridSearch.
STD : Dispersion des points autour de la moyenne des différentes distributions.

⦁	Annexe 6 : ZSCORE

En statistiques, le score z (ou score standard) d'une observation désigne le nombre d'écarts-types qui se trouve au-dessus ou en dessous de la moyenne de la population. Pour calculer un résultat z, vous devez connaître la moyenne de population et l'écart-type de population. 
Créer une visualisation de score z pour répondre aux questions du type suivant : 
Quel pourcentage de valeurs est-il inférieur à une valeur spécifique ? 
Quelles valeurs peuvent être considérées comme exceptionnelles ? Par exemple, dans un test de QI, quels scores représentent les 5 % supérieurs ? 
Quel est le score relatif d'une distribution par rapport à une autre ? Par exemple, Michael est plus grand que la moyenne des hommes, et Emily est plus grande que la moyenne des femmes, mais qui est plus grand relativement dans son sexe ?

![Screenshot](https://github.com/tomcdev63/MARCO_CASION/blob/main/IMG/z_score.png?raw=true)

⦁	Annexe 7 : Regression Lineaire

En statistiques, en économétrie et en apprentissage automatique, un modèle de régression linéaire est un modèle de régression qui cherche à établir une relation linéaire entre une variable, dite expliquée, et une ou plusieurs variables, dites explicatives.
On parle aussi de modèle linéaire ou de modèle de régression linéaire.
Comme les autres modèles de régression, le modèle de régression linéaire est aussi bien utilisé pour chercher à prédire un phénomène que pour chercher à l'expliquer.
Après avoir estimé un modèle de régression linéaire, on peut prédire quel serait le niveau de y pour des valeurs particulières de x. 

⦁	Annexe 8 : Random Forest Regressor

La forêt aléatoire est un algorithme d'apprentissage supervisé qui utilise une méthode d'apprentissage d'ensemble pour la classification et la régression.
Les arbres en forêts aléatoires sont exécutés en parallèle. Il n'y a pas d'interaction entre ces arbres lors de la construction des arbres.
Il fonctionne en construisant une multitude d'arbres de décision au moment de l'apprentissage et en produisant la classe qui est le mode des classes (classification) ou la prédiction moyenne (régression) des arbres individuels.
Une forêt aléatoire est un méta-estimateur (c'est-à-dire qu'il combine le résultat de plusieurs prédictions) qui agrège de nombreux arbres de décision , avec quelques modifications utiles :
* Le nombre d'entités pouvant être fractionnées à chaque nœud est limité à un certain pourcentage du total (appelé hyperparamètre ). Cela garantit que le modèle d'ensemble ne repose pas trop sur une caractéristique individuelle et fait un usage équitable de toutes les caractéristiques potentiellement prédictives .
* Chaque arbre tire un échantillon aléatoire de l'ensemble de données d'origine lors de la génération de ses divisions, ajoutant un élément supplémentaire de caractère aléatoire qui empêche le surajustement.

![Screenshot](https://github.com/tomcdev63/MARCO_CASION/blob/main/IMG/Captur%C3%B9%C3%B9e.JPG?raw=true)

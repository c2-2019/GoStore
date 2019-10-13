# Sommaire
##  Introduction..............................................................................................................................
##  Description du projet............................................................................................................
- #### I.Objectifs du projet...........................................................................................................
- #### II.Avantages attendu............................................................................................................
- #### III.Desavantages................................................................................................................
- #### IV.Fonctionnalités ciblées......................................................................................................

##  Objectifs quantitatifs.............................................................................................................

## Déroulement du projet...............................................................................................................

- #### I.Planification.......................................................................................................................................
- #### II.Spécifications.................................................................................................................................
- #### III.Conception..................................................................................................................................
- #### IV.Programmation..............................................................................................................................
- #### V.Tests unitaires................................................................................................................................
- #### VI.Intégration...........................................................................................................................
- #### VII.Test global...................................................................................................................................

##  Spécification........................................................................................................................

- #### I. Spécifications fonctionnelles ................................................................................................................................

- #### II. Spécifications technique.......................................................................................................................

   .1. Technologies utilisées .........................................................................................................................................
   
   
   .2. Configurations de machines....................................................................................................................................
   
   
   .3. Architecture technique de produit.....................................................................................................................................
   
   
   .4. les librairies utilisées...................................................................................................................................





#  Introduction
Dans le cadre de l’unité d’enseignement "Projet" du matière Architectures Logicielles Java (C2) à l’université ISAE Cnam, il nous ait demandé de travailler sur un projet de développement de système d’information de notre choix.
Après discussion entre les membres de l’équipe chargée de la mise en œuvre du projet, nous avons décidé de créer un système spécial pour les magasins "Go Store".

"Go Store" est un système de magasin de haute technologie de style "Amazon Go". Ce système fournit un magasin qui n’a pas besoin de caissier ni de caisse enregistreuse. Entrez dans le magasin, prenez les choses et allez

Ce document décrit le contexte, les besoins fonctionnels et les objectifs du projet. Un premier découpage des étapes nécessaires à la réalisation d’un tel projet donne lieu dans de document à un planning prévisionnel. Ce document a pour finalités de définir le projet de manière simple et détaillée et de définir les objectifs auxquels devra répondre une future spécification technique.

#  Description du projet

## I. Objectifs du projet
L'objectif principal du projet est d'améliorer la gestion des ventes et des achats en magasin et de transformer le processus de vente et de facturation en un processus automatique.
Au départ, il s’agit d’identifier clairement les besoins et les attentes
Un système d'information permettant la gestion des échanges.

"Go store" est une infrastructure de magasinage modulaire qui offre aux clients une expérience de magasinage sans friction. Inspirée par les innovations récentes révélées par Amazon Go, notre équipe souhaitait ambitieusement recréer la même expérience - avec un budget étudiant.

L'idée commence par un système dans lequel les personnes s'inscriront dans notre base de données en fournissant leur nom et leur photo une seule fois. Les clients peuvent ensuite accéder à notre magasin en lisant simplement le code via l'application qui se trouvera sur leur téléphone à notre entrée. Ils pourront également prendre un article et l'ajouter automatiquement à leur panier. Les éléments sont découverts comme capturés en plaçant des capteurs de lumière et à ultrasons sous leurs étagères respectives.

Les gestionnaires peuvent également suivre les clients dans leurs magasins en temps réel via notre application de gestion en déterminant quels clients sont en magasin et ce qu'ils ont dans leur panier.

Les clients peuvent visualiser leur panier en temps réel sur leur téléphone avec notre application , puis sortir devant notre caméra de sortie et être informés de leur facture sur leur téléphone. Tout cela sans interaction humaine et mieux encore, sans temps d'attente.

Tout au long du projet, la notion de passage à l’échelle devra être prise en compte. L’objectif à long terme de la conception et du développement d’un tel système d’information est de pouvoir être utilisé par toutes les catégories et magasins.


## II. Avantages attendu du "Go Store"

- Pas d'attente dans les lignes.
- Pas de caissiers.
- Pas de caisse.
- Pas de glisser votre carte.
- Gain de temps (le temps compte).
- Le client peut porter ses bagages à l'intérieur le magasin.
- Le vol à l'étalage est littéralement impossible


## III Desavantages

- Le client devrait avoir l'application .
- Le client devrait avoir un compte.
- Le client a besoin d’Internet pour entrer dans le magasin.

## IV. Fonctionnalités ciblées

Les fonctionnalités attendues de l'application sont les suivantes :
- Ajoutter , Mettre à jour, et effacer un produit.
- Inscrire, Mettre à jour , et effacer un client.
- Permettre au client d'entrer au magasin après la verification d'identite a partir une application sur leur telephone.
- Détection du produit pris.
- Detecter le client qui a pris le produit.
- Ajouter le produit en temps réel au shopping cart.
- Supprimer le produit en temps réel du shopping cart si le produit a été ramené.
- Permettre au client de voir les  produits sélectionnés en temps reel, leurs prix et la facture totale via l'application.
- Vérifiez si le compte client a assez d'argent pour ouvrir la porte au moment du départ.
-La facture totale est automatiquement déduite du compte lorsque le client quitte et envoie un message l'informant du montant retiréز
-Permettre au gérant de magasin de voir les clients qui sont dans le magasin et les produits qu'ils ont choisis.
- Permettre au gérant de magasin de voir les rapports de vente.


# Objectifs quantitatifs

Ce projet qui sera appliqué est en principe un projet universitaire et l’objectif est d’appliquer les acquis de l’enseignement scolaire. Il peut ensuite être étendu, consulté et appliqué dans les magasins pour faciliter les achats et faciliter ainsi la vie des gens.

# Contraintes du projet

### I. Contraintes en termes de délais
A partir de la livraison du cahier des charges, nous disposons d’environ un mois et demis pour la réalisation du projet. Le délai semble court pour le projet entier dédié à la gestion des processus d'un magasin complet ,mais reste suffisant pour se concentrer sur la partie prévue pour l'idee.

### II. Contraintes de sécurité
La gestion de la sécurité est la principale contrainte de notre système. L'application doit posséder une gestion de privilèges et de niveaux d'accès pour les différents types d'utilisateurs (Clients,administration,..). Selon leur statut, le contenu des pages varie et l'accès aux informations avec un statut
supérieur est interdit.

### III. Contraintes technique
 La structure de notre système doit être extensible pour
la mettre en place facilement dans les magasins. De plus, le développement devra
suivre toutes les normes techniques pour une meilleure performance, maintenance et facilité de mise à jour.


# Spécifications

## I. Spécifications fonctionnelles

L'utilisateur devra simplement télécharger l'application et créer un profil. Le profil contient le nom complet, la photo du visage de l'utilisateur, les informations de la carte de paiement, son numéro de téléphone et son adresse s'il le souhaite. 
Une fois le profil créé, l'utilisateur peut accéder au magasin en scannant le QR code. Il peut ensuite effectuer l'achat et prendre les produits qu'il souhaite, puis quitter le magasin sans s'arrêter devant le fonds de comptabilité ou compter la valeur des produits qu'il a pris. 
Au moment du départ, il est seulement nécessaire de refaire le scan du QR code pour pouvoir sortir.





# Déroulement du projet

## I. Planification

Une première analyse du projet nous à permis de définir une suite d’étapes à suivre pour sa réalisation.

- #### Spécifications
Durant cette étape, nous allons définir clairement ce qui doit être réalisé pour atteindre chaque objectif du projet.

- #### Conception
Cette phase permettra de faire le choix entre les différentes solutions techniques en respectant les contraintes du projet.

- #### Programmation
Écriture du code des différents modules et leurs fonctionnalités.

- #### Tests unitaires
Cette étape se chevauche avec l'étape de programmation, les tests unitaires devront être effectues pendant le développement pour s'assurer du bon fonctionnement du chaque module du l'application.

- #### Intégration
Regroupement de l'ensemble des modules après leur validation par chaque développeur des composants qu'il a réalisé.

- #### Test global
Cette partie permet de s'assurer que toutes les fonctionnalités de l'application sont valides, après l'intégration.
Le diagramme ci-dessous illustre pour chaque étape du déroulement du projet, les dates de début et de fin ainsi que la durée.

[![1-](images/temps.png "1-")]




## II. Spécifications technique

### 1.Technologies utilisées

Nous utiliserons une architecture J2EE pour le serveur sur lequel nous développerons une API RESTful. Pour
l’application et l’interface Web, nous utiliserons VueJS et Apache Cordova. La
base de données sur le serveur sera en MySQL. Les communications en
temps réel (positionnement) seront faites en Websocket ou via les services
fournis par Google Maps.

rusberypi ,automation, sensor --> python  language by default in rusberpi compatible with equipments end sensors

microservice dependent : using java scalable java 

mobile app : cross platform code wa7ad ios and android easy to integrate universal 

### 2.Configurations de machines



### 3.Architecture technique de produit


### 4.Les librairies utilisées



## II. Ressources
Pour finir, nous allons décrire l'ensemble des ressources mises a disposition pour la réalisation du projet.

#### Ressources humaines
Le projet sera réalisé par un groupe de trois étudiants. Il est nécessaire d'évaluer la charge de travail que chaque membre sera en mesure de fournir, notamment pour les tâches qui nécessitent une répartition : programmation et tests unitaires. On estime la charge de travail personnel qui devra être
consacrée à la conception, au développement et aux tests unitaires à environ 120 heures pour chaque membre du groupe.


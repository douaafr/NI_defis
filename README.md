# **Tortue Montante**

Un jeu simple et amusant où vous guidez une tortue à travers des obstacles pour atteindre le sommet de l'écran sans toucher les déchets. Si vous touchez un déchet, vous revenez au point de départ !

---

## **Prérequis**

Avant de pouvoir exécuter ce projet, assurez-vous que vous avez installé les éléments suivants :

1. **Python** (version 3.7 ou supérieure) : [Télécharger Python](https://www.python.org/downloads/)
2. **Pygame** : une bibliothèque Python pour développer des jeux.

   Pour installer Pygame, exécutez la commande suivante dans votre terminal ou votre invite de commande :
   
   pip install pygame
   

---

## **Comment jouer**

1. **Lancer le jeu :**
   - Téléchargez les fichiers nécessaires (`tortue.png`, `dechets.png`, `background.jpg`) et placez-les dans le même répertoire que le fichier Python.
   - Ouvrez un terminal dans ce répertoire et exécutez :
     
     python <nom_du_fichier>.py
    

2. **Commandes :**
   - **Flèche gauche** : déplacer la tortue vers la gauche.
   - **Flèche droite** : déplacer la tortue vers la droite.
   - **Flèche haut** : déplacer la tortue vers le haut.
   - **Flèche bas** : déplacer la tortue vers le bas.

3. **Objectif :**
   - Évitez les déchets sur votre chemin.
   - Atteignez le haut de l'écran pour gagner.

4. **Attention :**
   - Si vous touchez un déchet, la tortue retourne à son point de départ.

---

## **Fichiers requis**

Placez les fichiers suivants dans le même répertoire que le script :

- **tortue.png** : une image représentant la tortue (taille recommandée : 50x50 pixels).
- **dechets.png** : une image représentant les déchets (taille recommandée : 50x50 pixels).
- **background.jpg** : une image de fond pour le jeu (dimensions : 400x600 pixels).

---

## **Fonctionnalités**

- Génération aléatoire des obstacles avec une limite de 3 déchets par ligne.
- Message de démarrage avant le début du jeu.
- Détection des collisions avec les obstacles.
- Message de victoire lorsque la tortue atteint le haut de l'écran.
- Réinitialisation automatique en cas de collision avec les déchets.

---

## **Démonstration**

1. **Écran de démarrage** : Un message s'affiche demandant d'appuyer sur une touche pour commencer.
2. **Gameplay** : La tortue se déplace à l'aide des flèches tout en évitant les obstacles.
3. **Écran de victoire** : Lorsque vous atteignez le haut de l'écran, un message de victoire s'affiche.

---

## **Améliorations possibles**

- Ajouter un système de score en fonction du temps ou des mouvements.
- Intégrer différents niveaux de difficulté.
- Ajouter des sons et des musiques pour rendre le jeu plus immersif.

---

## **Crédits**

- Développé en Python avec **Pygame**.
- Images utilisées :
  - `tortue.png` : image représentant la tortue.
  - `dechets.png` : image représentant les obstacles.
  - `background.jpg` : image utilisée comme fond du jeu.

---

## **Licence**

Vous pouvez utiliser et modifier ce projet librement à des fins éducatives ou personnelles. 😊

--- 

Ce fichier devrait te donner une présentation claire et complète de ton projet !
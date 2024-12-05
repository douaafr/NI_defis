import pygame
import random

pygame.init()

# Configuration des dimensions
largeur_fenetre = 400
hauteur_fenetre = 600
taille_case = 50

# Initialisation de la fenêtre
fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))
pygame.display.set_caption("Tortue Montante")

# Chargement des images
image_tortue = pygame.image.load("tortue.png")
image_dechet = pygame.image.load("dechets.png")
background = pygame.image.load("background.jpg")

# Redimensionnement des images
image_tortue = pygame.transform.scale(image_tortue, (taille_case, taille_case))
image_dechet = pygame.transform.scale(image_dechet, (taille_case, taille_case))
background = pygame.transform.scale(background, (largeur_fenetre, hauteur_fenetre))

# Position initiale de la tortue
pos_tortue = [largeur_fenetre // 2, hauteur_fenetre - taille_case]
tortue = pygame.Rect(pos_tortue[0], pos_tortue[1], taille_case, taille_case)

# Liste pour les obstacles
obstacles = []

# Fonction pour créer les obstacles avec restriction
def creer_obstacles():
    obstacles.clear()
    for i in range(0, hauteur_fenetre, taille_case):
        dechets_sur_la_ligne = 0  # Compteur pour les déchets sur la ligne
        for j in range(0, largeur_fenetre, taille_case):
            if i != hauteur_fenetre - taille_case:  # Ignorer la première ligne (ligne de départ)
                if random.random() < 0.1 and dechets_sur_la_ligne < 3:  # 10% de chance et max 3 déchets par ligne
                    obstacles.append(pygame.Rect(j, i, taille_case, taille_case))
                    dechets_sur_la_ligne += 1

# Fonction pour afficher un message à l'écran
def afficher_message(fenetre, texte, taille, couleur, x, y):
    police = pygame.font.Font(None, taille)
    surface_texte = police.render(texte, True, couleur)
    rect_texte = surface_texte.get_rect(center=(x, y))
    fenetre.blit(surface_texte, rect_texte)

# Création initiale des obstacles
creer_obstacles()

# Variables pour la boucle de jeu
clock = pygame.time.Clock()
vitesse = 5
score = 0
jeu = True
en_jeu = False  # Ajout d'une phase d'attente avant le début
message_collision = ""

# Boucle de jeu
while jeu:
    if not en_jeu:
        # Afficher le message de début avec une taille de police plus petite
        fenetre.blit(background, (0, 0))
        afficher_message(fenetre, "Appuyez sur une touche pour commencer", 24, (255, 255, 255), largeur_fenetre // 2, hauteur_fenetre // 2)
        pygame.display.flip()
        
        # Attendre que le joueur appuie sur une touche pour commencer
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                jeu = False
            if event.type == pygame.KEYDOWN:
                en_jeu = True
        continue

    # Réinitialiser le message de collision à chaque itération
    message_collision = ""

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jeu = False

    # Contrôles de la tortue
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and tortue.x > 0:
        tortue.x -= taille_case
    if keys[pygame.K_RIGHT] and tortue.x < largeur_fenetre - taille_case:
        tortue.x += taille_case
    if keys[pygame.K_UP] and tortue.y > 0:
        tortue.y -= taille_case
    if keys[pygame.K_DOWN] and tortue.y < hauteur_fenetre - taille_case:
        tortue.y += taille_case

    # Vérification de la collision avec les déchets
    for obstacle in obstacles:
        if tortue.colliderect(obstacle):
            message_collision = "Vous avez touché un déchet ! Retour au départ."
            tortue.x = largeur_fenetre // 2
            tortue.y = hauteur_fenetre - taille_case
            break

    # Vérification si la tortue atteint la fin de la matrice
    if tortue.y <= 0:
        fenetre.blit(background, (0, 0))
        afficher_message(fenetre, "Vous avez accés a notre site !", 36, (255, 255, 255), largeur_fenetre // 2, hauteur_fenetre // 2)
        pygame.display.flip()
        pygame.time.wait(3000)  # Attendre 3 secondes avant de fermer
        jeu = False

    # Affichage du fond d'écran
    fenetre.blit(background, (0, 0))

    # Dessin des obstacles
    for obstacle in obstacles:
        fenetre.blit(image_dechet, (obstacle.x, obstacle.y))

    # Dessin de la tortue
    fenetre.blit(image_tortue, (tortue.x, tortue.y))

    # Afficher le message de collision s'il existe
    if message_collision:
        afficher_message(fenetre, message_collision, 24, (255, 0, 0), largeur_fenetre // 2, hauteur_fenetre // 2 + 100)

    # Mise à jour de l'affichage
    pygame.display.flip()

    # Limitation de la vitesse de la boucle
    clock.tick(vitesse)

# Quitter pygame
pygame.quit()

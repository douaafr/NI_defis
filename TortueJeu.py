import pygame
import random

pygame.init()

largeur_fenetre = 400
hauteur_fenetre = 600
taille_case = 50

fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))
pygame.display.set_caption("Tortue Montante")

# Chargement des images
image_tortue = pygame.image.load("tortue.png")
image_dechet = pygame.image.load("dechets.png")
background = pygame.image.load("background.jpg")  # Charger le fond

# Redimensionnement des images
image_tortue = pygame.transform.scale(image_tortue, (taille_case, taille_case))
image_dechet = pygame.transform.scale(image_dechet, (taille_case, taille_case))
background = pygame.transform.scale(background, (largeur_fenetre, hauteur_fenetre))  # Ajuster le fond à la taille de la fenêtre

pos_tortue = [largeur_fenetre // 2, hauteur_fenetre - taille_case]

obstacles = []

tortue = pygame.Rect(pos_tortue[0], pos_tortue[1], taille_case, taille_case)

def creer_obstacles():
    obstacles.clear()
    for i in range(0, hauteur_fenetre, taille_case):
        for j in range(0, largeur_fenetre, taille_case):
            # Ne pas placer d'obstacles sur la ligne de départ
            if i != hauteur_fenetre - taille_case:  
                if random.random() < 0.1:  # 10% de chance de mettre un déchet sur chaque case
                    obstacles.append(pygame.Rect(j, i, taille_case, taille_case))

# Création initiale des obstacles
creer_obstacles()

# Boucle de jeu
clock = pygame.time.Clock()
vitesse = 5
score = 0
jeu = True

while jeu:
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
            print("Vous avez touché un déchet ! Repartie au départ.")
            tortue.x = largeur_fenetre // 2
            tortue.y = hauteur_fenetre - taille_case
            break

    # Vérification si la tortue atteint la fin de la matrice
    if tortue.y <= 0:
        print("Bravo ! Vous avez gagné !")
        jeu = False

    # Affichage du fond d'écran
    fenetre.blit(background, (0, 0))

    # Dessin des obstacles
    for obstacle in obstacles:
        fenetre.blit(image_dechet, (obstacle.x, obstacle.y))

    # Dessin de la tortue
    fenetre.blit(image_tortue, (tortue.x, tortue.y))

    # Mise à jour de l'affichage
    pygame.display.flip()

    # Limitation de la vitesse de la boucle
    clock.tick(vitesse)

# Quitter pygame
pygame.quit()

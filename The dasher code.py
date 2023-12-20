#Mohamed Salama Id:231000359
#Zain elabdeen osama 231000356
#Abdelrahman mohamed hassan 231001730
import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("The Dasher v0.01")
icon = pygame.image.load(r"thedasher.png")
pygame.display.set_icon(icon)
Text_font = pygame.font.Font(r'font/Pixeltype.ttf',50)
fps=pygame.time.Clock()

Sky_surf=pygame.image.load(r'sky.jpg').convert()
Ground_surf=pygame.image.load(r'e4.png').convert()
Ground_rect=Ground_surf.get_rect(bottomleft=(0,400))

player_surf=pygame.image.load(r'e3.png').convert_alpha()
player_rect=player_surf.get_rect(midbottom=(700,352))
player_movement=5
playerright=pygame.transform.flip(player_surf,True,False)
playerleft=pygame.transform.flip(playerright,True,False)
left=True

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(Sky_surf,(-570,-500))
    screen.blit(Ground_surf,(0,350))
    screen.blit(player_surf,player_rect)

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player_rect.x -= player_movement
        left=True
    if keys[pygame.K_RIGHT]:
        player_rect.x += player_movement
        left=False
    if keys[pygame.K_UP]:
        player_rect.y -= player_movement
    if keys[pygame.K_DOWN]:
        player_rect.y += player_movement

    if player_rect.x<=-40:
        player_rect.x=760
    if player_rect.x>=780:
        player_rect.x=-20    
    if left:
        player_surf = playerleft
    else:
        player_surf = playerright
    if player_rect.y > 259:
        player_rect.y = 259
    
    
        
    
    pygame.display.update()
    fps.tick(60)

import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("The Dasher v0.01")
icon = pygame.image.load(r"thedasher.png")
pygame.display.set_icon(icon)
Text_font = pygame.font.Font(r'font/Pixeltype.ttf',50)
fps=pygame.time.Clock()

Sky_surf=pygame.image.load(r'bettersky.png').convert()
Ground_surf=pygame.image.load(r'e1.png').convert()

player_surf=pygame.image.load(r'e3.png').convert_alpha()
player_rect=player_surf.get_rect(midbottom=(800,350))
player_movement=3

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(Sky_surf,(0,0))
    screen.blit(Ground_surf,(0,350))
    screen.blit(player_surf,player_rect)

    player_rect.x=player_rect.x-player_movement

    if player_rect.x<=-5 or player_rect.x>=760:
        player_movement=player_movement*-1
        player_surf=pygame.transform.flip(player_surf,True,False)
    
    pygame.display.update()
    fps.tick(60)

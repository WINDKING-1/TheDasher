import pygame
from sys import exit
import random

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("The Dasher v0.01")
icon = pygame.image.load(r"thedasher.png")
pygame.display.set_icon(icon)
Text_font = pygame.font.Font(r'font/nanopixel.ttf',50)
fps=pygame.time.Clock()

Sky_surf= pygame.image.load(r'graphics/Sky.png').convert()
Ground_surf = pygame.image.load(r'graphics/ground.png').convert()
Text_surf = Text_font.render("The dasher 9000", False, 'Black')
Lives_surf= Text_font.render("❤️", True, 'red' )
Lives_rect= Lives_surf.get_rect(bottomright=(50,50))

snail_surf = pygame.image.load(r'graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surf.get_rect(midbottom=(600,300))

player_surf = pygame.image.load(r'graphics/Player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom=(80,300))

snailmove = random.randint(0, 50)*-1

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(Sky_surf,(0,0))
    screen.blit(Ground_surf,(0,300))
    screen.blit(Text_surf,(250,50))
    screen.blit(player_surf,player_rect)
    screen.blit(snail_surf,(snail_rect.x,270))
    screen.blit(Lives_surf,Lives_rect)


    snail_rect.x+=snailmove
    #if snail_rect.x<=3 or snail_rect.x>=735:
        #snailmove= -1*snailmove
        #snail_surf = pygame.transform.flip(snail_surf, True, False)
    if snail_rect.x<=0 or snail_rect.x>765:
        snail_rect.x=760 
        snailmove = random.randint(2,4)*-1
    mouse_pos=pygame.mouse.get_pos()

    if player_rect.collidepoint(mouse_pos):
        print("No")
        snailmove=3
  
    


    pygame.display.update()
    fps.tick(60)

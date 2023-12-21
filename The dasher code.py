#Zain elabdeen osama ID:231000356
#Mohamed Salama ID:231000359
#Abdelrahman mohamed hassan ID:231001730

import pygame
from sys import exit


pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("The Dasher v0.01")
icon = pygame.image.load(r"thedasher.png")
pygame.display.set_icon(icon)
Text_font = pygame.font.Font(r'font/Pixeltype.ttf',50)
fps=pygame.time.Clock()


#Sky_surf=pygame.image.load(r'sky.jpg').convert()
Sky_surf=pygame.image.load(r'bettersky.png').convert()
Ground_surf=pygame.image.load(r'download.png').convert()
Ground_rect=Ground_surf.get_rect(bottomleft=(0,400))


player_surf=pygame.image.load(r'e3.png').convert_alpha()
player_rect=player_surf.get_rect(midbottom=(700,352))
player_movement=5
player_fallseed=8
player_jump=10
player_aircount = 5

dashavailabe=True
dash_d=120
dash_cd=600
last_dashtimer=0

playerright=pygame.transform.flip(player_surf,True,False)
playerleft=pygame.transform.flip(playerright,True,False)
left=True

def playergoright():
    player_rect.x += player_movement

def playergoleft():
    player_rect.x -= player_movement

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()

    #screen.blit(Sky_surf,(-570,-500))
    screen.blit(Sky_surf,(0,0))
    screen.blit(Ground_surf,(0,351))
    screen.blit(player_surf,player_rect)

    keys = pygame.key.get_pressed()

    if player_rect.colliderect(Ground_rect):
        airborn=False
        player_aircount=6
    else:
        airborn=True
        
    if player_aircount == 6:
        player_rect.y += player_fallseed

    if player_aircount < 6:
        player_rect.y -= player_aircount * player_jump

    if player_aircount !=6:
        player_aircount+=1
    
    if not dashavailabe and (pygame.time.get_ticks()-last_dashtimer)>dash_cd:
        dashavailabe=True

    if keys[pygame.K_a]:
        playergoleft()
        left=True
    if keys[pygame.K_d]:
        playergoright()
        left=False
    if keys[pygame.K_SPACE] and not airborn:
        player_rect.y -= player_jump
        player_aircount = 1


    if keys[pygame.K_s]:
        for i in range(-3,0):
            player_rect.y-=player_fallseed*i


    if dashavailabe:
        if keys[pygame.K_LSHIFT]:
            if keys[pygame.K_w]:
                player_rect.y -= player_movement*14
                

            if left:
                player_rect.x-=dash_d
                dashavailabe=False
                last_dashtimer=pygame.time.get_ticks()
            if not left:
                player_rect.x+=dash_d
                dashavailabe=False
                last_dashtimer=pygame.time.get_ticks()

    if player_rect.x<=-51:
        player_rect.x=775
    if player_rect.x>=780:
        player_rect.x=-50    
    if left:
        player_surf = playerleft
    else:
        player_surf = playerright
    if player_rect.y > 259:
        player_rect.y = 259
        
    
    pygame.display.update()
    fps.tick(60)
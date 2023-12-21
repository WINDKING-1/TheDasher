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

level=1

Sky_surf=pygame.image.load(r'bettersky.png').convert()
Ground_surf=pygame.image.load(r'download.png').convert()
Ground_rect=Ground_surf.get_rect(bottomleft=(0,400))
Sky_surf2=pygame.image.load(r'sky.jpg').convert()
Ground_surf2=pygame.image.load(r'e4.png').convert()

player_surf=pygame.image.load(r'e3.png').convert_alpha()
player_rect=player_surf.get_rect(midbottom=(700,352))
player_movement=5
player_fallseed=8
player_jump=5
player_aircount = -8

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

def player_y_min():
    if player_rect.y > 259:
        player_rect.y = 259

def disdancecap():
    if player_rect.x<=-51:
        player_rect.x=775
    if player_rect.x>=780:
        player_rect.x=-50 

def gravity():
    player_rect.y += player_fallseed

def lvl1():
    screen.blit(Sky_surf,(0,0))
    screen.blit(Ground_surf,(0,351))
    screen.blit(player_surf,player_rect)

def lvl2():
    screen.blit(Sky_surf2,(-570,-500))
    screen.blit(Ground_surf2,(0,351))
    screen.blit(player_surf,player_rect)

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()

    if level==1:
        lvl1()
    elif level==2:
        lvl2()
    keys = pygame.key.get_pressed()

    if player_rect.colliderect(Ground_rect):
        airborn=False
        player_aircount=0
    else:
        airborn=True
        
    if player_aircount == 0 and airborn:
        gravity()

    if player_aircount < 0:
        player_rect.y += player_aircount * player_jump

    if player_aircount !=0:
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
        player_aircount = -7

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

    disdancecap()
    if left:
        player_surf = playerleft
    else:
        player_surf = playerright

    player_y_min()
 
    pygame.display.update()
    fps.tick(60)
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
Text_font = pygame.font.Font(r'font/Pixeltype.ttf',35)
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
player_jump=2.9
player_aircount = -8

dashavailabe=True
dash_d=120
dash_cd=600
last_dashtimer=0

combo_count=0
combo_font_size=35
combo_font = pygame.font.Font(r'font/Pixeltype.ttf',combo_font_size)

playerright=pygame.transform.flip(player_surf,True,False)
playerleft=pygame.transform.flip(playerright,True,False)
left=True

player_health=70
Health_text= str(player_health)+"%"

def playergoright():
    player_rect.x += player_movement

def playergoleft():
    player_rect.x -= player_movement

def player_y_min():
    if player_rect.y > 259:
        player_rect.y = 259

def distancecap():
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

def dash_up():
    player_rect.y -= dash_d

def dash_down():
    player_rect.y += dash_d

def dash_left():
    player_rect.x-=dash_d

def dash_right():
    player_rect.x+=dash_d

def Health_min():
    global player_health
    if player_health<0:
        player_health=0

def status_text():
    if player_health<=10:
        Health_color='purple'

    elif player_health<=30:
        Health_color='red'

    elif player_health<=60:
        Health_color='orange'

    elif player_health<=80:
        Health_color='yellow'

    else:
        Health_color='green'
    
    Health_surf=Text_font.render(Health_text, True,Health_color)
    screen.blit(Health_surf,(20,20))

def combo_coloring():
    if combo_count==0:
        combo_color='white'
    elif combo_count==1:
        combo_color='yellow'
        combo_font_size=55
        
    combo='x'+str(combo_count)
    Combo_surf=combo_font.render(combo, True,combo_color)
    screen.blit(Combo_surf,(20,40))

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
        player_aircount +=1
    
    if not dashavailabe and (pygame.time.get_ticks()-last_dashtimer)>dash_cd:
        dashavailabe=True

    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        playergoleft()
        left=True

    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        playergoright()
        left=False

    if keys[pygame.K_SPACE] and not airborn:
        player_rect.y -= player_jump
        player_aircount = -9

    if keys[pygame.K_s] or keys[pygame.K_DOWN]:
        for i in range(-3,0):
            player_rect.y-=player_fallseed*i

    if dashavailabe:
        if keys[pygame.K_LSHIFT]:
            if keys[pygame.K_w]:
                dash_up()

            if keys[pygame.K_s]:
                dash_down()

            if left:
                dash_left()
                dashavailabe=False
                last_dashtimer=pygame.time.get_ticks()
            
            if not left:
                dash_right()
                dashavailabe=False
                last_dashtimer=pygame.time.get_ticks()

    if left:
        player_surf = playerleft
    else:
        player_surf = playerright

    distancecap()
    player_y_min()
    status_text()
    combo_coloring()
    Health_min()

    pygame.display.update()
    fps.tick(60)
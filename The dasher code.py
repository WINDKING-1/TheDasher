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
fps_value=60
level=1

player_dash = False
player_dash1 = False
player_dash2 = False
dashing=False
dash_timer=0
direction = 1
DASH_DURATION = 10
DASH_DISTANCE = 100
dash_delay = 60
last_dash=None
double_jumped=False
Sky_surf=pygame.image.load(r'bettersky.png').convert()
Ground_surf=pygame.image.load(r'download.png').convert()
Ground_rect=Ground_surf.get_rect(bottomleft=(0,400))
Sky_surf2=pygame.image.load(r'sky.jpg').convert()
Ground_surf2=pygame.image.load(r'e4.png').convert()
death_screen_surf=pygame.image.load(r'died1.jpg').convert()

player_surf=pygame.image.load(r'e3.png').convert_alpha()
player_rect=player_surf.get_rect(midbottom=(700,352))
player_movement=5
player_fallseed=8
player_jump=2.9
player_aircount = -8

combo_count=4
combo_1_size=30
combo_2_size=40
combo_3_size=50
combo_4_size=65
combo_font_1 = pygame.font.Font(r'font/Pixeltype.ttf',combo_1_size)
combo_font_2 = pygame.font.Font(r'font/Pixeltype.ttf',combo_2_size)
combo_font_3 = pygame.font.Font(r'font/Pixeltype.ttf',combo_3_size)
combo_font_4 = pygame.font.Font(r'font/Pixeltype.ttf',combo_4_size)

playerright=pygame.transform.flip(player_surf,True,False)
playerleft=pygame.transform.flip(playerright,True,False)
left=True

player_health=24
Alive=True

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

def deathscreen():
    screen.blit(death_screen_surf,(0,0))
    player_died=True

def Health_min():
    global player_health
    if player_health<0:
        player_health=0
    if player_health>100:
        player_health=100

def player_bleed():
    global player_health
    player_health-=0.1

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


    if player_health==100:
        player_health_text=str(player_health)

    elif player_health >=10:
        player_health_text=str(player_health)[:2]

    else:
        player_health_text=str(player_health)[:3]

    Health_text= str(player_health_text)+"%"
    Health_surf=Text_font.render(Health_text, True,Health_color)
    screen.blit(Health_surf,(20,20))

def combo_coloring():
    combo='x'+str(combo_count)
    if combo_count==0:
        combo_color='white'
        Combo_surf=Text_font.render(combo, True,combo_color)
    elif combo_count==1:
        combo_color='yellow'
        Combo_surf=combo_font_1.render(combo, True,combo_color)
    elif combo_count==2:
        combo_color='red'
        Combo_surf=combo_font_2.render(combo, True,combo_color)
    elif combo_count==3:
        combo_color='blue'
        Combo_surf=combo_font_3.render(combo, True,combo_color)
    elif combo_count>=4:
        combo_color='green'
        Combo_surf=combo_font_4.render(combo, True,combo_color)

    screen.blit(Combo_surf,(400,20))

def player_dead_check():
    global level
    global Alive
    global fps_value
    if player_health<=0:
        level=0
        Alive=False
        fps_value=5

        
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()

    player_dead_check()

    if dash_timer!=0:
        dashing=True
    

    if level==1:
        lvl1()
    elif level==2:
        lvl2()
    elif level==0:
        deathscreen()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LSHIFT] and keys[pygame.K_d]:
        player_dash = True
    else:
        player_dash = False
    
    if keys[pygame.K_LSHIFT] and keys[pygame.K_a]:
        player_dash1 = True
    else:
        player_dash1 = False

    if keys[pygame.K_LSHIFT] and keys[pygame.K_w]:
        player_dash2 = True
    else:
        player_dash2 = False

    if player_dash:
        if dash_timer < DASH_DURATION:
            player_rect.x += (direction * DASH_DISTANCE) / DASH_DURATION
            dash_timer += 1

    if dash_timer >= 10:
        if dash_delay > 0:
            dash_delay -=1
        else:
            player_dash = False
            dash_delay = 40

    if player_dash1:
        if dash_timer < DASH_DURATION:
            player_rect.x -= (direction * DASH_DISTANCE) / DASH_DURATION
            dash_timer += 1

    if player_dash2:
        if dash_timer < DASH_DURATION:
            player_rect.y -= 100 / DASH_DURATION
            dash_timer += 1
    
    if dash_timer >= 10:
        dashing=False
        if dash_delay > 0:
            dash_delay -=1
        else:
            dash_timer = 0
            dash_delay = 40

    if Alive:
        if player_rect.colliderect(Ground_rect):
            airborn=False
            player_aircount=0
            double_jumped=False
        else:
            airborn=True

        if player_aircount < 0:
            player_rect.y += player_aircount * player_jump

        if player_aircount !=0:
            player_aircount +=1

        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            playergoleft()
            left=True

        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            playergoright()
            left=False

        if keys[pygame.K_SPACE] and not airborn:
            player_rect.y -= player_jump
            player_aircount = -9

        if keys[pygame.K_SPACE] and airborn and player_aircount==0 and not double_jumped:
                player_rect.y -= player_jump
                player_aircount = -6
                double_jumped=True

    if left:
        player_surf = playerleft
    else:
        player_surf = playerright

    if last_dash==dash_timer:
            dashing=False
        
    if player_aircount == 0 and airborn:
        last_dash=dash_timer
        if not dashing:
            gravity()

    #player_bleed()
    distancecap()
    player_y_min()
    if Alive:
        combo_coloring()
    Health_min()
    status_text()

    pygame.display.update()
    fps.tick(fps_value)
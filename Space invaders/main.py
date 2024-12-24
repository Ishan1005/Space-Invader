import math
import random
import pygame

pygame.init()
scr = pygame.display.set_mode((700,700))
pygame.display.set_caption("Space Game")
clock = pygame.time.Clock()

pimg = pygame.image.load('player.png')
eimg = pygame.image.load('enemy.png')
bimg = pygame.image.load('bullet.png')

px = 370
py = 500
px_cha = 0

num_e = 6
ex = []
ey = []
ex_cha = []
ey_cha = []
for _ in range(num_e):
    ex.append(random.randint(0,730))
    ey.append(random.randint(50,150))
    ex_cha.append(4)
    ey_cha.append(40)
    
bx = 0
by = 500
by_cha = 10
b_s = "ready"
def player(x,y):      
    scr.blit(pimg,(x,y))   

def enemy(x,y):      
    scr.blit(eimg,(x,y))                           

def fire_bullet(x,y):      
    global bullet_state                           
    bullet_state = "fire"
    scr.blit(bimg,(x + 16,y - 10))

def is_collision(ex,ey,bx,by):
    return abs(ex - bx) < 27 and abs(ey - by) < 27
running = True
while running:
    scr.fill((0,0,0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                running = False

        if event.type == pygame.KEYDOWN:
            if event.type == pygame.K_LEFT:
                px_cha = -5
            if event.type == pygame.K_RIGHT:
                px_cha = 5
            if event.type == pygame.K_SPACE and b_s == "ready":
                bx = px
                fire_bullet(bx,by)
        if event.type == pygame.KEYUP:
            if event.type == pygame.K_LEFT:
                px_cha = -0
            if event.type == pygame.K_RIGHT:
                px_cha = 0
    px += px_cha
    px = max(0,min(px,736))

    for i in range(num_e):
        ex[i] += ex_cha[i]
        if ex[i] <= 0 or ex[i] >= 736:
          ex_cha[i] *= -1
          ey[i] += ey_cha[i]
        if is_collision(ex[i],bx,by):
            by = 500
            b_s = "ready"
            ex[i] = random.randint(0,736)
            ey[i] = random.randint(50,150)

        enemy(ex[i],ey[i])

    if b_s == "fire":
        fire_bullet(bx,by)
        by -= by_cha
        if by < 0:
            by = 500
            b_s = "ready"

    player(px,py)
   
    clock.tick(60)
        
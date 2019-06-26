'''
Purpose: My First Game
autbor: Kurt Burdick
date modified: 3/1/2019
made with the help of techwithtim tutorials
check out Piskel for future reference
'''
#always needed for every pygame file
import pygame
pygame.init()

#Set window size 
win = pygame.display.set_mode((500,500))

#set window caption
pygame.display.set_caption("First Game")

x = 50
y = 50
width = 40
height = 60
vel = 20

run = True
while run:
    pygame.time.delay(100)

    #for-loop that allows key presses to be processed and not exit the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False #this if case allows game to be quit

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > 0:
        x -= vel

    if keys[pygame.K_RIGHT] and x < 460:
        x += vel

    if keys[pygame.K_UP] and y > 0:
        y -= vel

    if keys[pygame.K_DOWN] and y < 440:
        y += vel
        
    win.fill((0,0,255)) #fills background
    pygame.draw.rect(win, (0, 255, 0), (x, y, width, height)) #draws character
    pygame.display.update() #updates screen

pygame.quit()

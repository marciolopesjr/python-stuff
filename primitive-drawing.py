import pygame, sys
from pygame.locals import*

pygame.init()

displaySurf = pygame.display.set_mode((500,400),0,32)
pygame.display.set_caption('Drawing')

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

displaySurf.fill(white)

pygame.draw.polygon(displaySurf, green,((146,0),(291,106),(237,277),(56,277),(0,106)))
pygame.draw.line(displaySurf, blue, (60,60),(120,60),4)
pygame.draw.line(displaySurf, blue,(120,60),(60,120))
pygame.draw.line(displaySurf, blue, (60,120),(120,120),4)
pygame.draw.circle(displaySurf, blue,(300,50),20,0)
pygame.draw.ellipse(displaySurf, red, (300,250,40,80),1)
pygame.draw.rect(displaySurf,red,(200,150,100,50))

pixObj = pygame.PixelArray(displaySurf)
pixObj[480][380] = black
pixObj[482][382] = black
pixObj[484][384] = black
pixObj[486][386] = black
pixObj[488][388] = black

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()

import random

import pygame as pg
#Initializing PG Module
pg.init()
#Creating game screen
screen=pg.display.set_mode((800,600))
#Setting the logo of game screen
pg.display.set_caption("First Pygame")
#setting icon
icon=pg.image.load("car.png")
pg.display.set_icon(icon)
#Background
background=pg.image.load("Background.jpeg")
#Creating object in window
car=pg.image.load("car.png")
carX=0
carY=300
cardX=0
cardY=0
#Creating obstacles in window
stone=pg.image.load("stone.png")
stoneX=400
stoneY=400
stonedX=0
stonedY=1
#Function for drawing object on screen
def Car(x,y):
    screen.blit(car,(x,y))
def Stone(x,y):
    screen.blit(stone,(x,y))
#Stabilizing game screen while Quit not occurs
run=True
while run:
    pass
    # change color of window
    screen.fill((155, 180, 255))
    #stabilizing background
    screen.blit(background,(0,0))
    for event in pg.event.get():
        if event.type==pg.QUIT:
            run=False
        # Changing the position of the object
        if event.type == pg.KEYDOWN:
            key = pg.key.name(event.key)
            print(key, "Key is pressed")
            if event.key== pg.K_RIGHT:
                cardX=.5
            if event.key== pg.K_LEFT:
                cardX=-.5
            #if event.key==pg.K_UP:
                #cardY=-.5
            #if event.key==pg.K_DOWN:
                #cardY=.5
        if event.type == pg.KEYUP:
            if event.key == pg.K_RIGHT or event.key== pg.K_LEFT:
                cardX=0
            if event.key == pg.K_UP or event.key == pg.K_DOWN:
                cardY=0
            key = pg.key.name(event.key)
            print(key, "Key is released")
    carX+=cardX
    carY+=cardY
    stoneY+=stonedY
    if(stoneY>=600):
        stonedY=-1
    if(stoneY<-90):
        stonedY=+1

    #Setting Boundery
    if carX >= 715:
        carX = -100
    if carX < -100:
        carX = 715
    if carY<=-100:
        carY=505
    if carY >505:
        carY =-100
    Car(carX,carY)
    Stone(stoneX,stoneY)
    #Updating the gaming window continuously
    pg.display.update()

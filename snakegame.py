import pygame,sys,time
from pygame.locals import *
import random

pygame.init()

screenLength=800
screenBreadth=600
DISPLAYSURF=pygame.display.set_mode((screenLength,screenBreadth)) #Define a screen of size lxb


pygame.display.set_caption(' SNAKE WORLD')
#Snake Head variables
snakeHeadX=10
snakeHeadY=200

WHITE = (255,255,255)  #Defining Colors to use
PURPLE = (255,0,255)
RED = (255,0,0)
BLACK = (0,0,0)
AQUA = (0,255,255,200)
DISPLAYSURF.fill(WHITE)

fpsClock=pygame.time.Clock()

# Displaying Score of top left
score = 0



deltaX=10
deltaY=0

snakeBodyX=[0,0,0,0,0,0,0,0]
snakeBodyY=[0,0,0,0,0,0,0,0]
snakeLength=5

xf=random.randrange(20,380,10)
yf=random.randrange(20,280,10)

fruit=pygame.image.load('fruit.jpg')
# Furit Position in game initial condition. 
DISPLAYSURF.blit(fruit,(150,150))

#function definition to avoid boundary hit 
# Snake goes into wall and comes out on opposite side
def boundary(snakeHeadX,snakeHeadY):
    global screenBreadth
    if snakeHeadX>screenLength:
        snakeHeadX=snakeHeadX-screenLength
    elif snakeHeadX<0:
        snakeHeadX=snakeHeadX+screenLength

    if snakeHeadY>screenBreadth:
        snakeHeadY=snakeHeadY-screenBreadth
    elif snakeHeadY<0:
        snakeHeadY=snakeHeadY+screenBreadth
        
    return [snakeHeadX,snakeHeadY]

end=0
    


while True:
   
    DISPLAYSURF.fill(WHITE)    
    pygame.draw.rect(DISPLAYSURF,AQUA,(0,0,40,40))
    scoreLabel = pygame.font.SysFont("Times New Roman", 25).render(str(score), 1, BLACK)
    DISPLAYSURF.blit(scoreLabel,(10,5))


    for event in pygame.event.get():

        #Detecting a keyboard Stroke - w,a,s,d
        if event.type == pygame.KEYDOWN:        
            
            if event.key == ord("a"):
                deltaX=-10
                deltaY=0
            elif event.key == ord("s"):
                deltaX=0
                deltaY=10
            elif event.key == ord("w"):
                deltaX=0
                deltaY=-10
            elif event.key == ord("d"):
                deltaX=10
                deltaY=0
            
        elif event.type == QUIT or end==1:            
            pygame.quit()
            sys.exit()
    
    
    
    
    snakeBodyX[1] = snakeHeadX
    snakeBodyY[1] = snakeHeadY
    for i in range(snakeLength,0,-1):
        snakeBodyX[i+1] = snakeBodyX[i]
        snakeBodyY[i+1] = snakeBodyY[i]
    
    
    # Update Snake Head Varibales.
    snakeHeadX += deltaX
    snakeHeadY += deltaY
    

    [snakeHeadX,snakeHeadY] = boundary(snakeHeadX,snakeHeadY)   #function call to avoid boundary hit

    # To Check if Snakes head is touching it's body anywhere. 
    for i in range(2,snakeLength):
        if snakeHeadX == snakeBodyX[i] and snakeHeadY == snakeBodyY[i]:

            end=1            
            pygame.time.wait(1000)
            pygame.quit()
            sys.exit()  


    # Drawing the updated SNAKE
    for i in range(1,snakeLength):
        pygame.draw.rect(DISPLAYSURF, RED, (snakeBodyX[i], snakeBodyY[i], 12, 12))
    
    DISPLAYSURF.blit(fruit,(xf,yf))   #fruit size 15x21 pixels

    #Isf Head is around Furit, Increase Score and Generate New Fruit. 
    if snakeHeadX in range(xf-5,xf+10) and snakeHeadY in range(yf-5,yf+21):        
        
        snakeLength+=1
        score+=1
        snakeBodyX.append(0)
        snakeBodyY.append(0)

        #Generating next fruit in a random Place
        xf=random.randrange(20,380,10)
        yf=random.randrange(20,280,10)
        
    
    # One Game cycle complete, update the screen to show all changes to DISPLAYSURF    
    pygame.display.update() 
    fpsClock.tick(8)
    

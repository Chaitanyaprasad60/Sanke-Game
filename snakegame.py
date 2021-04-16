import pygame,sys,time
from pygame.locals import *
#import pyautogui
import random

pygame.init()
l=800
br=600
DISPLAYSURF=pygame.display.set_mode((l,br))
pygame.display.set_caption(' world')
a=10
b=200
WHITE=(255,255,255)
PURPLE=(255,0,255)
RED=(255,0,0)
BLACK=(0,255,0)
AQUA=(0,255,255,200)
DISPLAYSURF.fill(WHITE)
fpsClock=pygame.time.Clock()
k=1
u=0
x=[0,0,0,0,0,0,0,0]
y=[0,0,0,0,0,0,0,0]
f=5
xf=random.randrange(20,380,10)
yf=random.randrange(20,280,10)
fruit=pygame.image.load('fruit.jpg')
DISPLAYSURF.blit(fruit,(150,150))


def boundary(a,b):
                                             #function definition to avoid boundary hit
    global br
    if a>l:
        a=a-l
    elif a<0:
        a=a+l

    if b>br:
        b=b-br
    elif b<0:
        b=b+br
        
    return [a,b]

end=0
    


while True:
   
    DISPLAYSURF.fill(WHITE)
    
    pygame.draw.rect(DISPLAYSURF,AQUA,(0,0,40,40))
    for event in pygame.event.get():
        if event.type== pygame.KEYDOWN:
            
            
            if event.key == ord("a"):
                k=-10
                u=0
            elif event.key == ord("s"):
                k=0
                u=10
            elif event.key == ord("w"):
                k=0
                u=-10
            elif event.key == ord("d"):
                k=10
                u=0
            
        elif event.type==QUIT or end==1:
            
            pygame.quit()
            sys.exit()
    
    
    
    
    x[1]=a
    y[1]=b
    for i in range(f,0,-1):
        x[i+1]=x[i]
        y[i+1]=y[i]
    
    
    a=a+k
    b=b+u
    

    [a,b]=boundary(a,b)                                     #function call to avoid boundary hit

    for i in range(2,f):
        if a==x[i] and b==y[i]:
            #pygame.draw.rect(DISPLAYSURF, BLACK, (40, 40, 40, 10))
            end=1
            
            pygame.time.wait(1000)
            pygame.quit()
            sys.exit()
    
            
            
            
    

    for i in range(1,f):
        pygame.draw.rect(DISPLAYSURF, RED, (x[i], y[i], 12, 12))
    
    #pygame.draw.rect(DISPLAYSURF, PURPLE, (xf, yf, 10, 10))
    DISPLAYSURF.blit(fruit,(xf,yf))                              #fruit size 15x21 pixels

    if a in range(xf-5,xf+10) and b in range(yf-5,yf+21):
        
        
        f=f+1
        x.append(0)
        y.append(0)
        print(f)
        xf=random.randrange(20,380,10)
        yf=random.randrange(20,280,10)
        
        #time.sleep(10)
        #pygame.quit()
        #sys.exit()
    
    
        
    pygame.display.update() 
    fpsClock.tick(8)
    

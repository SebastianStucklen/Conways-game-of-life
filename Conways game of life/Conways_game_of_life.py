import pygame
import random

pygame.init()
pygame.display.set_caption("game of life")
screen = pygame.display.set_mode((1600,900))
clock = pygame.time.Clock()

map = [[random.random() > -0.7 for i in range(64)] for i in range(36)]

#gameloop
while True:
    clock.tick(60)
    event = pygame.event.get()

    #input section
    for event in pygame.event.get():
        break

    screen.fill((0,0,0))
    for y in range(36):
        for x in range(64):
            nothing = 0
            #pygame.draw.rect(screen, (0,144,144), (x*50, y*50, 50, 50), 1)
    #update section
    map2 = map.copy()
    for y in range(36):
        for x in range(64):
            if map[y][x]==0:
                lel = random.randint(6,8)
                #pygame.draw.rect(screen, (0,0,0), (x*25, y*25, 25, 25))
                pygame.draw.rect(screen, (0,144,144), (x*50, y*50, 50, 50), lel)
            if map [y][x]==1:
                lel = random.randint(6,8)
                pygame.draw.rect(screen, (0,144,144), (x*50, y*50, 50, 50), lel)
                #r = random.randint(144,255)
                #g = random.randint(44,144)
                #r = random.randint(244,255)
                #g = random.randint(244,255)
                #b = random.randint(244,255)
                #lel = random.randint(0,13)
                #pygame.draw.rect(screen, (r,g,b), (x*25, y*25, 25, 25),lel)

            
            counter = 0
            if y<35 and map[y+1][x]==1: #check above
                counter+=1
            if x<63 and map[y][x+1] == 1: #check right
                counter+=1
            if x>=0 and map[y][x-1] == 1: #check left
                counter+=1
            if y<35 and x<63 and map[y+1][x+1]==1: #check top right
                counter+=1
            if y<35 and x>=0 and map[y+1][x-1]==1: #check top left
                counter+=1
            if y>=0 and map[y-1][x]==1: #check below
                counter+=1
            if y>=0 and x<63 and map[y-1][x+1]==1: #check bottom right
                counter+=1
            if y>=0 and x>=0 and map[y-1][x-1]==1: #check bottom left
                counter+=1


            if map[y][x]==1 and counter <=1:
                map2[y][x]=0
                print("i died from lonliness")
            if map[y][x]==1 and counter >1:
                print("i lived")
            if map[y][x]==1 and counter >=4:
                map2[y][x]=0
                print("i died from overcrowding")
            if map[y][x]==0 and counter ==3:
                map2[y][x]=1
                print("i have been born")
    map = map2
    pygame.time.wait(17)
    pygame.display.flip()
    #render
    #map
            

pygame.quit()
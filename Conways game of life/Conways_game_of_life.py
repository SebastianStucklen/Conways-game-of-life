import pygame
import random

pygame.init()
pygame.display.set_caption("game of life")
screen = pygame.display.set_mode((800,800))
clock = pygame.time.Clock()

map = [[random.random() > 0.7 for i in range(16)] for i in range(16)]

#gameloop
while True:
    clock.tick(60)
    event = pygame.event.get()

    #input section
    for event in pygame.event.get():
        break

    screen.fill((0,0,0))
    for i in range(16):
        for j in range(16):
            pygame.draw.rect(screen, (255,255,255), (j*50, i*50, 50, 50), 1)
    #update section
    for i in range(16):
        for j in range(16):
            if map[i][j]==0:
                pygame.draw.rect(screen, (0,0,0), (j*50, i*50, 50, 50))
                pygame.draw.rect(screen, (255,255,255), (j*50, i*50, 50, 50), 1)
            if map [i][j]==1:
                pygame.draw.rect(screen, (255,144,0), (j*50, i*50, 50, 50))

            
            counter = 0
            if i<15 and map[i+1][j]==1: #check above
                counter+=1
            if j<15 and map[i][j+1] == 1: #check right
                counter+=1
            if i<15 and j<15 and map[i+1][j+1]==1: #check top right
                counter+=1
            if i<15 and j>=0 and map[i+1][j-1]==1: #check top left
                counter+=1
            if map[i][j]==1 and counter <=1:
                map[i][j]=0
                print("i died from lonliness")
            if map[i][j]==1 and counter >1:
                print("i lived")
            if map[i][j]==1 and counter >=4:
                map[i][j]=0
                print("i died from overcrowding")
            if map[i][j]==0 and counter ==3:
                map[i][j]=1
                print("i have been born")
    pygame.time.wait(200)
    pygame.display.flip()
    #render
    #map
            

pygame.quit()
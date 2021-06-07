# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 18:29:40 2020

@author: Mehmet Akıncı
"""

import pygame


if __name__ == "__main__":
    
    pygame.init()
    hits = 0
    window = pygame.display.set_mode((960,540))
    x_dir,y_dir = 1,1
    x,y = 480,270
    points=[]
    radius = 20
    run = True
    while run:
        pygame.time.delay(100)
        window.fill((255,255,255))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        pygame.draw.rect(window,(0,0,0),(70,60,820,420)) 
        pygame.draw.rect(window,(125,255,0),(80,70,800,400))        
        if x >= (880 - radius) or x <= (80 + radius):
            x_dir *= -1
            hits += 1
        if y >= (470 - radius) or y <= (70 + radius):
            y_dir *= -1
            hits += 1
        pygame.draw.circle(window,(255,0,0),(x,y),radius,20)    
        if hits > 5:
            run = False
            done = pygame.font.SysFont("Helvetica",50).render("Game End !",1,(0,0,0),(255,255,255))
            window.blit(done,(350,0))
        else:
            hit_counter = pygame.font.SysFont("Helvetica",30).render("Number of Hits: " + str(hits),1,(0,0,0),(255,255,255))
            window.blit(hit_counter,(10,0))
        x += 15 * x_dir
        y += 15 * y_dir    
        pygame.display.update()      
pygame.time.wait(3000)
pygame.quit()
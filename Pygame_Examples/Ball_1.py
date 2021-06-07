# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 17:22:23 2020

@author: Mehmet Akıncı
"""
import pygame
import math
from decimal import Decimal
            
class Ball():
    
    def __init__(self,velocity,position):
        self.velocity = velocity
        self.position = position
        self.radius = 20
        self.width = 20
        
    def move(self):
        self.position = (self.position[0] + self.velocity[0],self.position[1] + self.velocity[1])
         
    def update(self,width_border,height_border):
        if (width_border[0]+self.radius) >= self.position[0] or (width_border[1]-self.radius) <= self.position[0]:
            self.velocity[0] *= -1
        if (height_border[0]+self.radius) >= self.position[1] or (height_border[1]-self.radius) <= self.position[1]:
            self.velocity[1] *= -1    
        

class Table():
    def __init__(self,width,height):
        self.position = [80,70]
        self.width = width
        self.height = height
        self.b_width = width + 20
        self.b_height = height + 20
        self.b_position = (self.position[0]-10,self.position[1]-10)

def Collision_Check(ball_1,ball_2):
    x = float(ball_2.position[0] - ball_1.position[0])
    y = float(ball_2.position[1] - ball_1.position[1])
    if math.sqrt((x**2)+(y**2)) < float(Decimal(ball_1.radius + ball_2.radius)) :   
        return True
    else:
        return False
    
def Elastic_Collision (ball_1,ball_2):
    temp = ball_2.velocity
    ball_2.velocity = ball_1.velocity
    ball_1.velocity = temp    
    
if __name__ == "__main__":  
    width = 960
    height = 540
    delay = 10
    
    window = pygame.display.set_mode((width,height))
    table = Table(800,400)
    ball_1 = Ball([-4,6],[480,270])
    ball_2 = Ball([7,-3],[400,300])
    run = True
    pygame.init()
    
    while run:
        pygame.display.update()
        window.fill((255,255,255))
        pygame.time.delay(delay)
        pygame.draw.rect(window,(0,0,0),(70,60,table.b_width,table.b_height)) 
        pygame.draw.rect(window,(125,255,0),(table.position[0],table.position[1],table.width,table.height))
        pygame.draw.circle(window,(255,0,0),(ball_1.position[0],ball_1.position[1]),ball_1.radius,ball_1.width)
        pygame.draw.circle(window,(255,0,0),(ball_2.position[0],ball_2.position[1]),ball_2.radius,ball_2.width)
        
        if Collision_Check(ball_1,ball_2) == True:
            '''pygame.time.wait(3000)'''
            Elastic_Collision(ball_1,ball_2)
            
        ball_1.update((table.position[0],table.position[0]+table.width),(table.position[1],table.position[1]+table.height))
        ball_1.move()
        ball_2.update((table.position[0],table.position[0]+table.width),(table.position[1],table.position[1]+table.height))
        ball_2.move()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
         


pygame.time.wait(1000)
pygame.quit()                
        
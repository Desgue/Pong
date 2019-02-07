import pygame
from .config import Globals, Colors
from math import cos,sin,radians,pi
class Player(pygame.Rect):
    def __init__(self):
        super(Player,self).__init__(20,225,20,150)
        self.velocity = 5
        self.points = 0
        print("player class initated")
    def update(self,up,down):
        if up and self.y >= 10:
            self.y -= self.velocity
        if down and self.y <= Globals.win_height - (self.height +10):
            self.y += self.velocity
        pass
    
class Enemy(pygame.Rect):
    def __init__(self):
        super(Enemy,self).__init__(760,225,20,150)
        self.velocity = 2
        self.points = 0
        print("enemy class initated")
    def update(self,ballYpos):
        middle = self.y + self.height /2
        if ballYpos != middle:
            if ballYpos > middle and self.y <= Globals.win_height- (self.height+self.velocity):
                self.y += self.velocity
            if ballYpos < middle and self.y >= self.velocity*2:
                self.y -= self.velocity

        
class Ball(pygame.Rect):
    def __init__(self):
        super(Ball,self).__init__(400,300,20,20)
        self.velocity = 5
        self.angle = radians(0)
        self.dir_x = cos(self.angle)
        self.dir_y = -sin(self.angle)
        print("Ball class instancieted")
    def reset(self):
        self.x =400
        self.y = 300
        self.angle = radians(0)
        self.dir_x = cos(self.angle)
        self.dir_y = -sin(self.angle)
    def update(self,player,enemy):       
        self.x += self.dir_x * self.velocity
        self.y += self.dir_y * self.velocity

        self.handle_bound_collision()
        self.handle_paddle_collision(player,enemy)
            
    def handle_bound_collision(self):
        if self.y <=  0 or self.y>= Globals.win_height - 10:
            self.dir_y*= -1.05
            
    def handle_paddle_collision(self,player,enemy):
        intersectY = self.y
        if self.colliderect(player):
            relativeIntersectY = (player.y + (player.height / 2) ) - intersectY
            normalizedRelativeIntersectY = relativeIntersectY / (player.height/2)
            self.angle = radians(normalizedRelativeIntersectY * 60)
            self.dir_x = cos(self.angle)
            self.dir_y = -sin(self.angle)
            
        if self.colliderect(enemy):
            relativeIntersectY = (enemy.y + (enemy.height/2)) - intersectY
            normalizedRelativeIntersectY = relativeIntersectY / (enemy.height/2) 
            self.angle = radians(normalizedRelativeIntersectY * 60)
            self.dir_x = -cos(self.angle)
            self.dir_y = sin(self.angle)
    

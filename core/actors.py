import pygame
from .config import WINDOW_SIZE, BALL_SIZE, PADDLE_SIZE
from math import cos,sin,radians,pi
class Player(pygame.Rect):
    def __init__(self):
        super(Player,self).__init__(20,225,PADDLE_SIZE)
        self.velocity = 5
        self.points = 0
        print("player class initated")
    def update(self,up,down):
        if up and self.y >= 10:
            self.y -= self.velocity
        if down and self.y <= WINDOW_SIZE.height - (self.height +10):
            self.y += self.velocity
        pass
    
class Enemy(pygame.Rect):
    def __init__(self):
        super(Enemy,self).__init__(760,225,PADDLE_SIZE)
        self.velocity = 3
        self.points = 0
        print("enemy class initated")
    def update(self,ball_y_pos):
        middle = self.y + self.height /2
        if ball_y_pos != middle:
            if ball_y_pos > middle and self.y <= WINDOW_SIZE.height- (self.height+self.velocity):
                self.y += self.velocity
            if ball_y_pos < middle and self.y >= self.velocity*2:
                self.y -= self.velocity

        
class Ball(pygame.Rect):
    def __init__(self):
        super(Ball,self).__init__(400,300,BALL_SIZE)
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
        if self.y <=  0 or self.y>= WINDOW_SIZE.height - 10:
            self.dir_y*= -1.05
            
    def handle_paddle_collision(self,player,enemy):
        intersect_y = self.y
        if self.colliderect(player):
            relative_intersect_y = (player.y + (player.height / 2) ) - intersect_y
            normalized_relative_intersect_y = relative_intersect_y / (player.height/2)
            self.angle = radians(normalized_relative_intersect_y * 60)
            self.dir_x = cos(self.angle)
            self.dir_y = -sin(self.angle)
            
        if self.colliderect(enemy):
            relative_intersect_y = (enemy.y + (enemy.height/2)) - intersect_y
            normalized_relative_intersect_y = relative_intersect_y / (enemy.height/2) 
            self.angle = radians(normalized_relative_intersect_y * 60)
            self.dir_x = -cos(self.angle)
            self.dir_y = sin(self.angle)
    

import pygame
from .config import Colors, Globals

class Button(pygame.Rect):
    def __init__(self,x, y, width, height,color, text = "Default"):
        super(Button, self).__init__(x, y, width, height)
        self.font = pygame.font.SysFont("Comic Sans MS", 56)
        self._text = text
        self.color = color
        
    def render(self,screen):
        pygame.draw.rect(screen, self.color, self)
        
    def handle_events(self, events):
        pass
    
    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, new_text):
        self._text = new_text
        

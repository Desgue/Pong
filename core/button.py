import pygame
from .config import WINDOW_SIZE, FONT_PATH

class Button(pygame.Rect):
    def __init__(self,x, y, width, height,color, text = "Default", x_padding = 0, y_padding =0):
        super(Button, self).__init__(x, y, width, height)
        self.font = pygame.font.SysFont(FONT_PATH, 36)
        self._text = text
        self._color = color
        self._xpadding = x_padding
        self._ypadding = y_padding
        
    def render(self,screen):    
        return NotImplemented
        
    def handle_events(self, events):
        return NotImplemented


# Properties
    @property
    def color(self):
        return self._color
    @color.setter
    def color(self, new_color):
        self._color = new_color
        
    @property
    def text(self):
        return self._text
     
    @text.setter
    def text(self, new_text):
        self._text = new_text
        
    @property
    def padding(self):
        return self._padding
    @padding.setter
    def padding(self, new_padding):
        self._padding = new_padding

    @property
    def x_padding(self):
        return(x_padding)
    @x_padding.setter
    def x_padding(self, new_padding):
        self._xpadding = new_padding

    @property
    def y_padding(self):
        return (y_padding)
    @y_padding.setter
    def y_padding(self, new_padding):
        self._ypadding = new_padding
    
class StartButton(Button):
    def __init__(self, x,y,width,height,color,text, x_padding, y_padding):
        super(MenuButton, self).__init__(
        x,
        y,
        width,
        height,
        color,
        text = "Start",
        x_padding,
        y_padding)

    def render(self,screen):
        pygame.font.init()
        text = self.font.render(self._text, True, self._color)
        screen.blit(text, (self.x + self.x_padding, self.y + self.y_padding) )

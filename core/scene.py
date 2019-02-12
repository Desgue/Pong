from .actors import Player,Enemy,Ball
from .config import WINDOW_SIZE, FONT_PATH
from .button import Button
import pygame

class SceneManager(object):
    def __init__(self):
        self.go_to(MenuScene())

    def go_to(self, scene):
        self.scene = scene
        self.scene.manager = self

class Scene(object):
    def __init__(self):
        pass
    def render(self, screen):
        raise NotImplementedError
    def update(self):
        raise NotImplementedError
    def handle_events(self, events):
        raise NotImplementedError
    
class MenuScene(Scene):
    def __init__(self):
        super(MenuScene,self).__init__()
        pygame.font.init()
        self.font = pygame.font.Font(FONT_PATH,52)
        self.sfont = pygame.font.Font(FONT_PATH, 32)
        #self.start_btn = Button(250,200, 200,50, pygame.Color("white"))
    def update(self):
        pass    
    def render(self, screen):      
        screen.fill(pygame.Color("green"))
        #self.start_btn.render(screen)
        text1 = self.font.render('Pong Rework', True, (255, 255, 255))
        text2 = self.sfont.render('> press SPACE to start <', True, (255, 255, 255))
        screen.blit(text1, (200, 50))
        screen.blit(text2, (200, 350))
        #self.start_btn.render(screen)
    
    def handle_events(self,events):
        for e in events:
            if e.type == pygame.KEYDOWN and (e.key == pygame.K_SPACE or e.key == pygame.K_RETURN):
                self.manager.go_to(GameScene()) 
                
class GameScene(Scene):
    def __init__(self):
        super(GameScene, self).__init__()
        pygame.font.init()
        self.font = pygame.font.SysFont("Comic Sans MS", 30)
        self.player = Player()
        self.enemy = Enemy()
        self.points ={"player": 0, "enemy": 0}
              
        self.ball = Ball()
        
    def render(self,screen):
        self.player_score=self.font.render("{}".format(self.player.points),1,pygame.Color("white"))
        self.enemy_score=self.font.render("{}".format(self.enemy.points),1, pygame.Color("white"))  
        screen.blit(self.player_score,(150,100))
        screen.blit(self.enemy_score,(630,100))
        pygame.draw.rect(screen,pygame.Color("white"),self.player)
        pygame.draw.rect(screen,pygame.Color("white"),self.enemy)
        pygame.draw.rect(screen,pygame.Color("white"),self.ball)

    def update(self):
        pressed = pygame.key.get_pressed()
        up,down = [pressed[key] for key in (pygame.K_UP, pygame.K_DOWN)]
        self.handle_point()
        self.player.update(up,down)
        self.enemy.update(self.ball.y)
        self.ball.update(self.player,self.enemy)
        

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pass

    def handle_point(self):
        if self.ball.x <= self.ball.width:
            self.enemy.points += 1
            self.ball.reset()                     
        if self.ball.x >= (WINDOW_SIZE.width + self.ball.width):
            self.player.points += 1
            self.ball.reset()
            self.ball.dir_x *= -1  

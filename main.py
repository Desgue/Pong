from __future__ import absolute_import
import pygame
from core.config import WINDOW_SIZE
from core.scene import GameScene, SceneManager

def main():
    screen = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption("Pong")
    clock = pygame.time.Clock()
    manager = SceneManager()
    running= True
    pygame.init()
    while running:
        clock.tick(120)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill(pygame.Color("black"))
        manager.scene.render(screen)
        manager.scene.handle_events(pygame.event.get())
        manager.scene.update()
        pygame.display.flip()
            
    pygame.quit()

if __name__ == "__main__":
    main()

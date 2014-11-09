import os

import pygame
import kezmenu

from main import Game


class Custom(object):
    running = True

    def main(self, screen):
        clock = pygame.time.Clock()
        background = pygame.image.load(os.path.join('img', 'background.png'))
        menu = kezmenu.KezMenu(
            ['Done!', lambda: Game().main(screen)],
            ['Options', lambda: setattr(self, 'running', True)],
            ['Quit', lambda: setattr(self, 'running', False)],
        )
        menu.font = pygame.font.SysFont('Arial', 40, bold=True)
        menu.x = 300
        menu.y = 100
        menu.enableEffect('raise-col-padding-on-focus', enlarge_time=0.1)

        while self.running:
            menu.update(pygame.event.get(), clock.tick(30)/1000.)
            screen.blit(background, (0, 0))
            menu.draw(screen)
            pygame.display.flip()

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    Custom().main(screen)

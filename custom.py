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
        )
        menu.font = pygame.font.SysFont('Arial', 40, bold=True)
        menu.x = 320
        menu.y = 400
        menu.enableEffect('raise-col-padding-on-focus', enlarge_time=0.1)

        rect1 = pygame.Rect(200, 25, 300, 50)
        rect2 = pygame.Rect(50, 125, 400, 40)
        rect3 = pygame.Rect(50, 225, 400, 40)
        rect4 = pygame.Rect(50, 325, 400, 40)
        rect5 = pygame.Rect(500, 125, 40, 40)
        rect6 = pygame.Rect(500, 225, 40, 40)
        rect7 = pygame.Rect(500, 325, 40, 40)
        # text = "%s: %.1f%%" % (self.label, self.percentage)
        # screen.blit(
        #     self.font.render(text, True, (0, 0, 0), (0, 0)), self.rect)

        while self.running:
            menu.update(pygame.event.get(), clock.tick(30)/1000.)
            screen.blit(background, (0, 0))
            menu.draw(screen)
            pygame.draw.rect(screen, (255, 0, 0), rect1)
            pygame.draw.rect(screen, (255, 0, 0), rect2)
            pygame.draw.rect(screen, (255, 0, 0), rect3)
            pygame.draw.rect(screen, (255, 0, 0), rect4)
            pygame.draw.rect(screen, (0, 0, 255), rect5)
            pygame.draw.rect(screen, (0, 0, 255), rect6)
            pygame.draw.rect(screen, (0, 0, 255), rect7)
            pygame.display.flip()

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    Custom().main(screen)

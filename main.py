import os

import pygame

from player import Player
from widgets import Progressbar, Panel
from config import Options


class Game(object):
    def main(self, screen):
        clock = pygame.time.Clock()

        sprites = pygame.sprite.Group()
        self.player = Player(sprites)

        self.panel = Panel((255, 0, 0))

        self.walls = pygame.sprite.Group()
        block = pygame.image.load(os.path.join('img', 'wall.png'))
        for x in range(0, Options.RESOLUTION[0] - Options.PANEL_WIDTH, 32):
            for y in range(0, Options.RESOLUTION[1], 32):
                if x in (0, Options.RESOLUTION[0]-32-Options.PANEL_WIDTH) or \
                        y in (0, Options.RESOLUTION[1]-32):
                    wall = pygame.sprite.Sprite(self.walls)
                    wall.image = block
                    wall.rect = pygame.rect.Rect((x, y), block.get_size())
        sprites.add(self.walls)

        self.test_progressbar = Progressbar(100, 20, 33, (0, 0, 200),
                                            (0, 0, 0), "Test")

        while 1:
            dt = clock.tick(Options.FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                if event.type == pygame.KEYDOWN and \
                        event.key == pygame.K_ESCAPE:
                    return
                if event.type == pygame.KEYDOWN and \
                        event.key == pygame.K_RETURN:
                    return

            sprites.update(dt / 1000., self)
            screen.fill((100, 100, 100))
            self.panel.draw(screen)
            self.test_progressbar.draw(screen)
            sprites.draw(screen)
            pygame.display.flip()


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode(Options.RESOLUTION)
    Game().main(screen)

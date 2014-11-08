# import os

import pygame
import tmx

from player import Player
from widgets import Progressbar, Panel
from config import Options


class Game(object):
    def main(self, screen):
        clock = pygame.time.Clock()

        sprites = pygame.sprite.Group()

        self.panel = Panel((255, 0, 0))

        self.tilemap = tmx.load('map.tmx', screen.get_size())

        self.sprites = tmx.SpriteLayer()
        start_cell = self.tilemap.layers['triggers'].find('player')[0]
        self.player = Player((start_cell.px, start_cell.py), self.sprites)
        self.tilemap.layers.append(self.sprites)


        self.test_progressbar = Progressbar(140, 20, 33, (0, 0, 200),
                                            (0, 0, 0), "Programming")

        while 1:
            dt = clock.tick(Options.FPS)

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and \
                        event.key == pygame.K_w:
                    self.test_progressbar.update(5)
                if event.type == pygame.KEYDOWN and \
                        event.key == pygame.K_s:
                    self.test_progressbar.update(-5)
                if event.type == pygame.QUIT:
                    return
                if event.type == pygame.KEYDOWN and \
                        event.key == pygame.K_ESCAPE:
                    return
                if event.type == pygame.KEYDOWN and \
                        event.key == pygame.K_RETURN:
                    return

            self.tilemap.update(dt / 1000., self)
            sprites.update(dt / 1000., self)
            screen.fill((100, 100, 100))
            self.test_progressbar.draw(screen)
            sprites.draw(screen)
            self.tilemap.draw(screen)
            self.panel.draw(screen)
            pygame.display.flip()


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode(Options.RESOLUTION)
    Game().main(screen)

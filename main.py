import pygame

import tmx

from player import Player
from widgets import Panel
from config import Options
from npcs import Mentor


class Game(object):
    def main(self, screen):
        clock = pygame.time.Clock()

        sprites = pygame.sprite.Group()

        self.panel = Panel((255, 0, 0))

        self.tilemap = tmx.load('map.tmx', screen.get_size())

        self.sprites = tmx.SpriteLayer()

        start_cell = self.tilemap.layers['triggers'].find('player')[0]
        self.player = Player((start_cell.px, start_cell.py),
                             5, 3, 5, self.sprites)

        mentor_spawn_points = self.tilemap.layers['triggers'].find('mentor')

        self.tilemap.layers.append(self.sprites)

        # self.test_progressbar = Progressbar(140, 20, 33, (0, 0, 200),
        #                                     (0, 0, 0), "Programming")
        mentor_exists = False
        while 1:
            dt = clock.tick(Options.FPS)

            place = 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                if event.type == pygame.KEYDOWN and \
                        event.key == pygame.K_ESCAPE:
                    return
                if event.type == pygame.KEYDOWN and \
                        event.key == pygame.K_RETURN:
                    return
                if event.type == pygame.KEYDOWN and \
                        event.key == pygame.K_m:
                    mentor_exists = True
                    mc = mentor_spawn_points[place]
                    self.m = Mentor((mc.px, mc.py), mentor_spawn_points,
                                    self.sprites)

                if event.type == pygame.KEYDOWN and \
                        event.key == pygame.K_c:
                    self.m.change_to_random_place()

            if mentor_exists:
                last = self.player.rect.copy()
                print last.right
                new = self.player.rect
                cell = self.m.rect
                print cell.left
                if last.colliderect(cell):
                    self.m.visited(self.player)

            self.tilemap.update(dt / 1000., self)
            sprites.update(dt / 1000., self)
            screen.fill((100, 100, 100))
            self.panel.draw(screen)
            # self.test_progressbar.draw(screen)
            sprites.draw(screen)
            self.tilemap.draw(screen)
            self.panel.draw(screen)
            pygame.display.flip()


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode(Options.RESOLUTION)
    Game().main(screen)

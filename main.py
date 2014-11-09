import random

import pygame

import tmx

from player import Player
from widgets import Panel, Progressbar, Popup
from config import Options
from npcs import Mentor


class Game(object):
    def __init__(self):
        self.pr_pr = 0
        self.d_pr = 0
        self.i_pr = 80

    def main(self, screen):
        clock = pygame.time.Clock()
        sprites = pygame.sprite.Group()

        EVERY_SECOND = pygame.USEREVENT + 1
        EVERY_TEN_SECONDS = pygame.USEREVENT + 2
        second = 1000  # milliseconds
        pygame.time.set_timer(EVERY_SECOND, second)
        pygame.time.set_timer(EVERY_TEN_SECONDS, second*5)

        self.panel = Panel((170, 170, 170))
        self.tilemap = tmx.load('map.tmx', screen.get_size())
        self.sprites = tmx.SpriteLayer()

        start_cell = self.tilemap.layers['triggers'].find('player')[0]
        self.player = Player((start_cell.px, start_cell.py),
                             6, 6, 7, self.sprites)

        mentor_spawn_points = self.tilemap.layers['triggers'].find('mentor')

        self.tilemap.layers.append(self.sprites)

        self.programming_progress = Progressbar(485, 25, 150, 23, self.pr_pr,
                                                (74, 119, 233),
                                                (0, 0, 0), " Programming")
        self.design_progress = Progressbar(485, 75, 150, 23, self.d_pr,
                                           (67, 166, 56),
                                           (0, 0, 0), " Design")
        self.idea_progress = Progressbar(485, 125, 150, 23, self.i_pr,
                                         (255, 128, 0),
                                         (0, 0, 0), " Idea")
        self.player_programming_skill = pygame.Rect(485, 200, 150, 23)

        self.popup = Popup((255, 128, 0), "", show=False)

        mentor_exists = False
        while 1:
            dt = clock.tick(Options.FPS)

            place = 1
            for event in pygame.event.get():
                if event.type == EVERY_SECOND:
                    self.programming_progress.update(0.3)
                    self.design_progress.update(0.4)
                if event.type == EVERY_SECOND:
                    if random.randint(0, 100) < 80:
                        if not mentor_exists:
                            mc = mentor_spawn_points[random.randint(0, 3)]
                            self.m = Mentor((mc.px, mc.py), mentor_spawn_points,
                                            self.sprites)
                            mentor_exists = True
                        else:
                            self.m.change_to_random_place()

                if event.type == pygame.QUIT:
                    return
                if event.type == pygame.KEYDOWN and \
                        event.key == pygame.K_ESCAPE:
                    return
                if event.type == pygame.KEYDOWN and \
                        event.key == pygame.K_RETURN:
                    return
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if self.popup.rect.collidepoint(x, y):
                        self.popup.show = False

            if mentor_exists:
                last = self.player.rect.copy()
                new = self.player.rect
                cell = self.m.rect
                if last.colliderect(cell):
                    self.popup = self.m.visited(self.player)

            self.tilemap.update(dt / 1000., self)
            sprites.update(dt / 1000., self)
            screen.fill((100, 100, 100))
            self.panel.draw(screen)
            sprites.draw(screen)
            self.tilemap.draw(screen)
            self.panel.draw(screen)
            self.programming_progress.draw(screen)
            self.design_progress.draw(screen)
            self.idea_progress.draw(screen)
            self.popup.draw(screen)
            pygame.display.flip()


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode(Options.RESOLUTION)
    Game().main(screen)

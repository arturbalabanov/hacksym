import os

import pygame

from player import Player


class Progressbar(object):
    def __init__(self, width, height, percentage, bgcolor, border_color, label):
        self.rect = pygame.Rect(200 + 1, 200 + 1, width, height)
        self._border = pygame.Rect(200, 200, width, height)
        self.percentage = percentage
        self.bgcolor = bgcolor
        self.border_color = border_color
        self.label = label

    def draw(self, screen):
        pygame.draw.rect(screen, self.border_color, self._border, 1)
        pygame.draw.rect(screen, self.bgcolor, self.rect)


class Panel(object):
    ITEM_HEIGTH = 80

    def __init__(self, bgcolor):
        self.rect = pygame.Rect(Game.RESOLUTION[0] - Game.PANEL_WIDTH, 0,
                                Game.PANEL_WIDTH, Game.RESOLUTION[1])
        self.bgcolor = bgcolor

    def draw(self, screen):
        pygame.draw.rect(screen, self.bgcolor, self.rect)


class Game(object):
    FPS = 60
    RESOLUTION = (640, 480)
    PANEL_WIDTH = 160

    def main(self, screen):
        clock = pygame.time.Clock()

        sprites = pygame.sprite.Group()
        self.player = Player(sprites)

        self.panel = Panel((255, 0, 0))
        # self.panel = pygame.Rect(self.RESOLUTION[0] - self.PANEL_WIDTH, 0,
        #                          self.PANEL_WIDTH, self.RESOLUTION[1])

        self.walls = pygame.sprite.Group()
        block = pygame.image.load(os.path.join('img', 'wall.png'))
        for x in range(0, self.RESOLUTION[0] - self.PANEL_WIDTH, 32):
            for y in range(0, self.RESOLUTION[1], 32):
                if x in (0, self.RESOLUTION[0]-32-self.PANEL_WIDTH) or \
                        y in (0, self.RESOLUTION[1]-32):
                    wall = pygame.sprite.Sprite(self.walls)
                    wall.image = block
                    wall.rect = pygame.rect.Rect((x, y), block.get_size())
        sprites.add(self.walls)

        self.test_progressbar = Progressbar(100, 20, 33, (0, 0, 200),
                                            (0, 0, 0), "Test")

        while 1:
            dt = clock.tick(self.FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                if event.type == pygame.KEYDOWN and \
                        event.key == pygame.K_ESCAPE:
                    return

            sprites.update(dt / 1000., self)
            screen.fill((100, 100, 100))
            self.panel.draw(screen)
            self.test_progressbar.draw(screen)
            sprites.draw(screen)
            pygame.display.flip()


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode(Game.RESOLUTION)
    Game().main(screen)

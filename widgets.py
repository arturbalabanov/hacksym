import pygame

from config import Options


class Progressbar(object):
    def __init__(self, width, height, percentage, bgcolor, border_color, label):
        self.rect = pygame.Rect(200, 200, width, height)
        self._border = pygame.Rect(200 - 1, 200 - 1, width + 1, height + 1)
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
        self.rect = pygame.Rect(Options.RESOLUTION[0] - Options.PANEL_WIDTH, 0,
                                Options.PANEL_WIDTH, Options.RESOLUTION[1])
        self.bgcolor = bgcolor

    def draw(self, screen):
        pygame.draw.rect(screen, self.bgcolor, self.rect)

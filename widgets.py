import pygame

from config import Options


class Progressbar(object):
    def __init__(self, x, y, width, height, percentage,
                 bgcolor, border_color, label):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.rect = pygame.Rect(x, y, width, height)
        self.percentage = percentage
        self.bgcolor = bgcolor
        self.border_color = border_color
        self.label = label
        self.font = pygame.font.SysFont('Arial', 15, bold=True)

    def draw(self, screen):
        res = pygame.Rect(self.x, self.y, self.width * self.percentage / 100,
                          self.height)
        pygame.draw.rect(screen, self.bgcolor, res)
        pygame.draw.rect(screen, self.border_color, self.rect, 1)
        text = "%s: %.1f%%" % (self.label, self.percentage)
        screen.blit(
            self.font.render(text, True, (0, 0, 0), (0, 0)), self.rect)

    def update(self, count):
        if self.percentage + count < 0:
            self.percentage = 0
        elif self.percentage + count > 100:
            self.percentage = 100
        else:
            self.percentage += count


class Panel(object):
    ITEM_HEIGTH = 80

    def __init__(self, bgcolor):
        self.rect = pygame.Rect(Options.RESOLUTION[0] - Options.PANEL_WIDTH, 0,
                                Options.PANEL_WIDTH, Options.RESOLUTION[1])
        self.bgcolor = bgcolor

    def draw(self, screen):
        pygame.draw.rect(screen, self.bgcolor, self.rect)


class Popup(object):
    WIDTH = 350
    HEIGHT = 120

    def __init__(self, bgcolor, text):
        self.rect = pygame.Rect((Options.RESOLUTION[0] - self.WIDTH)/2,
                                (Options.RESOLUTION[1] - self.HEIGHT)/2,
                                self.WIDTH, self.HEIGHT)
        self.bgcolor = bgcolor
        self.text = text
        self._font = pygame.font.SysFont('Arial', 18, bold=False)
        self.show = True

    def draw(self, screen):
        if self.show:
            pygame.draw.rect(screen, self.bgcolor, self.rect)
            screen.blit(
                self._font.render(self.text, True, (0, 0, 0), (0, 0)), self.rect)

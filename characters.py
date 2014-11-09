import os

import pygame

# from config import Options


class BaseCharacer(pygame.sprite.Sprite):
    def __init__(self, location, *groups):
        super(BaseCharacer, self).__init__(*groups)
        self.image = pygame.image.load(
            os.path.join('img', '%s.png' % (self.__class__.__name__.lower())))
        self.rect = pygame.rect.Rect(location, self.image.get_size())

    def update(self):
        pass

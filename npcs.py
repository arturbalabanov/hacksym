import os

import pygame


class Mentor(pygame.sprite.Sprite):
    def __init__(self, location, *groups):
        super(Mentor, self).__init__(*groups)
        self.image = pygame.image.load(os.path.join('img', 'mentor.png'))
        self.rect = pygame.rect.Rect(location, self.image.get_size())

    def update(self):
        pass

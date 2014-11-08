import os

import pygame


class Player(pygame.sprite.Sprite):
    SPEED = 500

    def __init__(self, *groups):
        super(Player, self).__init__(*groups)
        self.image = pygame.image.load(os.path.join('img', 'player.png'))
        self.rect = pygame.rect.Rect((320, 240), self.image.get_size())

    def update(self, dt, game):
        last = self.rect.copy()

        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.rect.x -= self.SPEED * dt
        if key[pygame.K_RIGHT]:
            self.rect.x += self.SPEED * dt
        if key[pygame.K_UP]:
            self.rect.y -= self.SPEED * dt
        if key[pygame.K_DOWN]:
            self.rect.y += self.SPEED * dt

        for cell in pygame.sprite.spritecollide(self, game.walls, False):
            self.rect = last

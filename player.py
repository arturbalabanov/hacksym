import os

import pygame


class Player(pygame.sprite.Sprite):
    SPEED = 500

    def __init__(self, location, *groups):
        super(Player, self).__init__(*groups)
        self.image = pygame.image.load(os.path.join('img', 'player.png'))
        self.rect = pygame.rect.Rect(location, self.image.get_size())

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

        new = self.rect
        for cell in game.tilemap.layers['triggers'].collide(new, 'blockers'):
            if last.right <= cell.left and new.right > cell.left:
                new.right = cell.left
            if last.left >= cell.right and new.left < cell.right:
                new.left = cell.right
            if last.bottom <= cell.top and new.bottom > cell.top:
                new.bottom = cell.top
            if last.top >= cell.bottom and new.top < cell.bottom:
                new.top = cell.bottom

        game.tilemap.set_focus(new.x, new.y)

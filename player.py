import random

import pygame

from characters import BaseCharacer


class Player(BaseCharacer):
    SPEED = 500

    def __init__(self, location, programming, design, soft_skills,
                 *groups):
        super(Player, self).__init__(location, *groups)
        self.programming = programming
        self.design = design
        self.soft_skills = soft_skills

    def update(self, dt, game):
        last = self.rect.copy()

        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] or key[pygame.K_h]:
            self.rect.x -= self.SPEED * dt
        if key[pygame.K_RIGHT] or key[pygame.K_l]:
            self.rect.x += self.SPEED * dt
        if key[pygame.K_UP] or key[pygame.K_k]:
            self.rect.y -= self.SPEED * dt
        if key[pygame.K_DOWN] or key[pygame.K_j]:
            self.rect.y += self.SPEED * dt

        new = self.rect
        for cell in game.tilemap.layers['collision'].collide(new, 'blockers'):
            if last.right <= cell.left and new.right > cell.left:
                new.right = cell.left
            if last.left >= cell.right and new.left < cell.right:
                new.left = cell.right
            if last.bottom <= cell.top and new.bottom > cell.top:
                new.bottom = cell.top
            if last.top >= cell.bottom and new.top < cell.bottom:
                new.top = cell.bottom

        game.tilemap.set_focus(new.x, new.y)

    def get_random_bonus(self):
        skill = random.randint(1, 3)
        count = random.randint(1, 5)
        skill_name = None

        if skill == 1:
            self.programming += count
            skill_name = 'programming skills'
        elif skill == 2:
            self.design += count
            skill_name = 'design skills'
        elif skill == 3:
            self.soft_skills += count
            skill_name = 'soft skills'

        return (count, skill_name)

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


class Game(object):
    FPS = 60
    RESOLUTION = (640, 480)

    def main(self, screen):
        clock = pygame.time.Clock()

        sprites = pygame.sprite.Group()
        self.player = Player(sprites)

        self.walls = pygame.sprite.Group()
        block = pygame.image.load(os.path.join('img', 'wall.png'))
        for x in range(0, self.RESOLUTION[0], 32):
            for y in range(0, self.RESOLUTION[1], 32):
                if x in (0, self.RESOLUTION[0]-32) or \
                        y in (0, self.RESOLUTION[1]-32):
                    wall = pygame.sprite.Sprite(self.walls)
                    wall.image = block
                    wall.rect = pygame.rect.Rect((x, y), block.get_size())
        sprites.add(self.walls)

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
            sprites.draw(screen)
            pygame.display.flip()


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode(Game.RESOLUTION)
    Game().main(screen)

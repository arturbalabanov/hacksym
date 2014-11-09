import os

import pygame
import kezmenu

from main import Game


class Team(object):
    running = True

    def main(self, screen):
        clock = pygame.time.Clock()
        background = pygame.image.load(os.path.join('img', 'background.png'))
        teammate = pygame.image.load(os.path.join('img', 'teammate1.png'))
        menu = kezmenu.KezMenu(
            ['Okay!', lambda: Game().main(screen)],
        )
        menu.font = pygame.font.SysFont('Arial', 35, bold=True)
        menu.x = 280
        menu.y = 440
        menu.enableEffect('raise-col-padding-on-focus', enlarge_time=0.1)

        rect1 = pygame.Rect(0, 0, 640, 50)
        rect2 = pygame.Rect(0, 50, 320, 130)
        rect3 = pygame.Rect(0, 180, 320, 130)
        rect4 = pygame.Rect(0, 310, 320, 130)
        rect5 = pygame.Rect(320, 50, 320, 130)
        rect6 = pygame.Rect(320, 180, 320, 130)
        rect7 = pygame.Rect(320, 310, 320, 130)
        rect8 = pygame.Rect(0, 440, 640, 40)
        rect10 = pygame.Rect(130, 50, 190, 43)
        rect11 = pygame.Rect(130, 93, 190, 43)
        rect12 = pygame.Rect(130, 136, 190, 43)
        rect13 = pygame.Rect(130, 180, 190, 43)
        rect14 = pygame.Rect(130, 223, 190, 43)
        rect15 = pygame.Rect(130, 269, 190, 43)
        rect16 = pygame.Rect(130, 310, 190, 43)
        rect17 = pygame.Rect(130, 356, 190, 43)
        rect18 = pygame.Rect(130, 390, 190, 43)
        rect20 = pygame.Rect(450, 50, 190, 43)
        rect21 = pygame.Rect(450, 93, 190, 43)
        rect22 = pygame.Rect(450, 136, 190, 43)
        rect23 = pygame.Rect(450, 180, 190, 43)
        rect24 = pygame.Rect(450, 223, 190, 43)
        rect25 = pygame.Rect(450, 269, 190, 43)
        rect26 = pygame.Rect(450, 310, 190, 43)
        rect27 = pygame.Rect(450, 356, 190, 43)
        rect28 = pygame.Rect(450, 390, 190, 43)

        font = pygame.font.SysFont('Arial', 30, bold=True)
        font_little = pygame.font.SysFont('Arial', 24, bold=True)

        color = (74, 119, 233)
        color_picked = (255, 128, 0)
        current = color

        while self.running:
            # very bad design ahead, take a pokemon with you
            menu.update(pygame.event.get(), clock.tick(30)/1000.)
            screen.blit(background, (0, 0))
            pygame.draw.rect(screen, (255, 0, 0), rect1)
            pygame.draw.rect(screen, (current), rect2)
            pygame.draw.rect(screen, (current), rect3)
            pygame.draw.rect(screen, (current), rect4)
            pygame.draw.rect(screen, (current), rect5)
            pygame.draw.rect(screen, (current), rect6)
            pygame.draw.rect(screen, (current), rect7)
            pygame.draw.rect(screen, (0, 255, 0), rect8)
            screen.blit(font.render("Pick your teammates",
                                    True, (0, 0, 0), (0, 0)), rect1)
            screen.blit(font_little.render("Programming 11",
                        True, (0, 0, 0), (0, 0)), rect10)
            screen.blit(font_little.render("Programming 6",
                        True, (0, 0, 0), (0, 0)), rect13)
            screen.blit(font_little.render("Programming 1",
                        True, (0, 0, 0), (0, 0)), rect16)
            screen.blit(font_little.render("Design 0",
                        True, (0, 0, 0), (0, 0)), rect11)
            screen.blit(font_little.render("Design 6",
                        True, (0, 0, 0), (0, 0)), rect14)
            screen.blit(font_little.render("Design 5",
                        True, (0, 0, 0), (0, 0)), rect17)
            screen.blit(font_little.render("Soft Skills 1",
                        True, (0, 0, 0), (0, 0)), rect12)
            screen.blit(font_little.render("Soft Skills 6",
                        True, (0, 0, 0), (0, 0)), rect15)
            screen.blit(font_little.render("Soft Skills 11",
                        True, (0, 0, 0), (0, 0)), rect18)
            screen.blit(font_little.render("Programming 11",
                        True, (0, 0, 0), (0, 0)), rect20)
            screen.blit(font_little.render("Programming 6",
                        True, (0, 0, 0), (0, 0)), rect23)
            screen.blit(font_little.render("Programming 1",
                        True, (0, 0, 0), (0, 0)), rect26)
            screen.blit(font_little.render("Design 0",
                        True, (0, 0, 0), (0, 0)), rect21)
            screen.blit(font_little.render("Design 6",
                        True, (0, 0, 0), (0, 0)), rect24)
            screen.blit(font_little.render("Design 5",
                        True, (0, 0, 0), (0, 0)), rect27)
            screen.blit(font_little.render("Soft Skills 1",
                        True, (0, 0, 0), (0, 0)), rect22)
            screen.blit(font_little.render("Soft Skills 6",
                        True, (0, 0, 0), (0, 0)), rect25)
            screen.blit(font_little.render("Soft Skills 11",
                        True, (0, 0, 0), (0, 0)), rect28)
            screen.blit(teammate, rect2)
            screen.blit(teammate, rect3)
            screen.blit(teammate, rect4)
            screen.blit(teammate, rect5)
            screen.blit(teammate, rect6)
            screen.blit(teammate, rect7)
            menu.draw(screen)
            pygame.display.flip()

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    Team().main(screen)

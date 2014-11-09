import random

from characters import BaseCharacer
from formulas import mentor_successful_interaction
from widgets import Popup


class Mentor(BaseCharacer):
    MENTORS_COUNT = 4

    def __init__(self, location, locations, *groups):
        super(Mentor, self).__init__(location, *groups)
        self.locations = locations

    def change_place(self, new_x, new_y):
        self.rect.left = new_x
        self.rect.top = new_y

    def change_to_random_place(self):
        place = random.randint(0, self.MENTORS_COUNT-1)
        mc = self.locations[place]

        self.change_place(mc.px, mc.py)

    def visited(self, player):
        chance = mentor_successful_interaction(player.soft_skills)
        if chance > random.randint(1, 100):
            player.soft_skills += 1
            res = player.get_random_bonus()
            text = 'You got %d points in your %s.' % (res[0], res[1])
        else:
            text = 'You asked your mentor a stupid question.'

        self.change_to_random_place()
        popup = Popup((255, 128, 0), text, show=True)
        return popup

    def update(self, dt, game):
        pass


class Member(BaseCharacer):
    def __init__(self, location, programming=0, design=0, soft_skills=0,
                 *groups):
        super(Member, self).__init__(location, *groups)
        self.programming = programming
        self.design = design
        self.soft_skills = soft_skills

    def update(self, dt, game):
        pass

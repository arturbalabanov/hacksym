import random

from characters import BaseCharacer


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
        print 'Visited'
        self.change_to_random_place(self.locations)

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

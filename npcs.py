import random

from characters import BaseCharacer


class Mentor(BaseCharacer):
    MENTORS_COUNT = 4

    def __init__(self, location, *groups):
        super(Mentor, self).__init__(location, *groups)

    def change_place(self, new_x, new_y):
        self.rect.left = new_x
        self.rect.top = new_y

    def change_to_random_place(self, locations):
        place = random.randint(0, self.MENTORS_COUNT-1)
        mc = locations[place]

        self.change_place(mc.px, mc.py)

    def visited(self, player, locations):
        print 'Visited'
        self.change_to_random_place(locations)

    def update(self, dt, game):
        pass

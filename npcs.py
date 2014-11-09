from characters import BaseCharacer


class Mentor(BaseCharacer):
    def __init__(self, location, *groups):
        super(Mentor, self).__init__(location, *groups)

    def change_place(self, new_x, new_y):
        self.rect.left = new_x
        self.rect.top = new_y

    def update(self, dt, game):
        pass

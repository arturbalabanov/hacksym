from characters import BaseCharacer


class Mentor(BaseCharacer):
    def __init__(self, location, *groups):
        super(Mentor, self).__init__(location, *groups)

    def update(self, dt, game):
        pass

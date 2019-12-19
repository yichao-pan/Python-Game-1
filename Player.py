from Entity import *


class Player(Entity):
    def __init__(self, pos, size, speed, color, shape):
        Entity.__init__(
            self,
            (pos[0], pos[1]),
            size-2,
            speed,
            color,
            shape
        )

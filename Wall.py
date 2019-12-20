from MapObject import *


class Wall(MapObject):
    def __init__(self, pos, size, color):
        hitbox = (pos[0], pos[1] , size, size)

        MapObject.__init__(
            self,
            (pos[0] + size / 2, pos[1] + size / 2),
            size,
            hitbox,
            color,
            Shapes.RECT
        )

    def __str__(self):
        return "Wall" + str(MapObject.x_pos) + " " + str(MapObject.y_pos)

    def check_wall_col(self, obj):
        return self.hitbox.colliderect(obj.hitbox)

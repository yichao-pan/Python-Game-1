from MapObject import *


class Entity(MapObject):
    def __init__(self, pos, size, speed, color, shape):
        hitbox = (pos[0]-size/2, pos[1]-size/2, size, size)
        MapObject.__init__(
            self,
            (pos[0], pos[1]),
            size,
            hitbox,
            color,
            Shapes.RECT
        )
        self.speed = speed
        #center
        self.prev_x_pos = pos[0]
        self.prev_y_pos = pos[1]


    #-1 = left, down
    #1 = right, up
    def move(self, direction):
        #unpack the directions
        x_dir = direction[0]
        y_dir = direction[1] * -1
        #save the current positions
        self.prev_x_pos = self.x_pos
        self.prev_y_pos = self.y_pos
        #move to new position
        self.x_pos += x_dir*self.speed
        self.y_pos += y_dir*self.speed
        self.update_hitbox()

    #1 = left
    #2 = up
    #3 = right
    #4 = down
    def oob(self, direction):
        if(direction == 1 or direction == 3):
            self.x_pos = self.prev_x_pos
        if (direction == 2 or direction == 4):
            self.y_pos = self.prev_y_pos
        self.update_hitbox()

    def hit_wall(self, direction):
        pass

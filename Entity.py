class Entity:
    def __init__(self, pos, size, speed, color, shape):

        self.size = size

        #center
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.prev_x_pos = pos[0]
        self.prev_y_pos = pos[1]

        self.speed = speed

        self.color = color
        self.shape_func = shape

    def draw_entity(self, screen):
        self.shape_func(screen,
                        self.color,
                        (self.x_pos - self.size/2, self.y_pos - self.size/2, self.size, self.size))


    #dir:
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

    def oob(self, direction):
        pass
    def hit_wall(self, direction):
        pass

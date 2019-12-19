from Const import *
class MapObject:
    def __init__(self, pos, size, hitbox, color, shape):
        #center position
        self.x_pos = pos[0]
        self.y_pos = pos[1]

        self.size = size

        self.hitbox = pygame.Rect(hitbox)

        self.color = color
        self.shape = shape

        #whether to display the object
        self.disp = True

    def draw(self, screen):
        if (self.shape == Shapes.RECT):
            self.shape(
                screen,
                self.color,
                (self.x_pos - self.size / 2,
                 self.y_pos - self.size / 2,
                 self.size, self.size))
        if (self.shape == Shapes.CIRCLE):
            self.shape(
                screen,
                self.color,
                (self.x_pos, self.y_pos),
                self.size/2)

        self.draw_hitbox(screen)

    def update_hitbox(self):
        self.hitbox.center = (self.x_pos, self.y_pos)
        print(f"obj pos: {self.x_pos} {self.y_pos}")
        print(f"hit pos: {self.hitbox.center}")

    def draw_hitbox(self, screen):
        Shapes.RECT(
            screen,
            Colors.WHITE,
            self.hitbox,
            2
        )
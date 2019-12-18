import pygame


class Wall:
    def __init__(self, pos, size, color):
        self.x_pos = pos[0] + size / 2
        self.y_pos = pos[1] + size / 2
        self.size = size
        self.color = color

    def __str__(self):
        return "Wall" + str(self.x_pos) + " " + str(self.y_pos)

    def draw_wall(self, screen):
        pygame.draw.rect(screen,
                         self.color,
                         (self.x_pos - self.size / 2, self.y_pos - self.size / 2, self.size, self.size))



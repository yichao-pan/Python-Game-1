from Wall import *
from Const import *

class Map:
    def __init__(self, wall_grid, grid_size=20):
        self.wall_grid = wall_grid
        self.x = len(wall_grid[0])
        self.y = len(wall_grid)
        self.grid_size = grid_size

        self.walls = []
        self.set_walls()

    def set_walls(self):
        y = 0
        for vert in self.wall_grid:
            x = 0
            h_wall = []
            for hor in vert:
                if (hor == 1):
                    h_wall.append(Wall((x, y), self.grid_size, Colors().GREEN))
                else:
                    h_wall.append(None)
                x += self.grid_size
            self.walls.append(h_wall)
            y += self.grid_size

    def draw_walls(self, screen):
        for vert in self.walls:
            for w in vert:
                if(w != None):
                    w.draw_wall(screen)

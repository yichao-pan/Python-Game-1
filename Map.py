from Wall import *
from Const import *


class Map:
    def __init__(self, wall_grid, grid_size=20):
        self.wall_grid = wall_grid
        self.grid_width = len(wall_grid[0])
        self.grid_height = len(wall_grid)

        # pixel size of one grid square
        self.grid_size = grid_size

        # pixel size of the map
        self.map_width = self.grid_width * self.grid_size
        self.map_height = self.grid_height * self.grid_size

        # create walls
        self.walls = []
        self.set_walls()

    # create a list of walls
    def set_walls(self):
        # list of walls

        y = 0
        for ver in self.wall_grid:
            x = 0
            h_wall = []
            for hor in ver:
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
                if (w != None):
                    w.draw(screen)

    # convert screen pixel units to grid units
    def pix_to_grid(self, pix):
        return pix / self.grid_size

    # convert grid units to screen pixel units
    def grid_to_pix(self, grid):
        return grid * self.grid_size + self.grid_size / 2

    def check_collision(self, obj1, obj2):
        col = False
        x_dis = abs(obj1.x_pos - obj2.x_pos)
        y_dis = abs(obj1.y_pos - obj2.y_pos)
        if (x_dis < obj1.size / 2 + obj2.size / 2):
            if (y_dis < obj1.size / 2 + obj2.size / 2):
                col = True
        return col

    def check_oob(self, obj):
        # left
        if (obj.x_pos < 0):
            obj.oob(1)
        # right
        if (obj.x_pos > self.map_width):
            obj.oob(3)
        # up
        if (obj.y_pos > self.map_height):
            obj.oob(2)
        # down
        if (obj.y_pos < 0):
            obj.oob(4)

    def check_wall(self, obj):
        # get the grid cords of the object
        grid_x = self.pix_to_grid(obj.x_pos)
        grid_y = self.pix_to_grid(obj.y_pos)
        #print("Check:")

        # check the 9 boxes around the object
        # get the x and y cords for those boxes
        # make sure they dont go out of range near corners
        x_range = (
            int(max(grid_x - 1, 0)),
            int(min(grid_x + 2, self.grid_width))
        )
        y_range = (
            int(max(grid_y - 1, 0)),
            int(min(grid_y + 2, self.grid_height))
        )
        #check each box for a wall
        for i in range(y_range[0], y_range[1]):
            for j in range(x_range[0], x_range[1]):
                #print(f"{j} {i}")
                wall = self.walls[i][j]
                if (wall != None):
                    #if there is a wall, check for overlap
                    if (wall.hitbox.colliderect(obj.hitbox)):
                        #if there is overlap, check if it is above, below, left or right
                        print("c")
                        obj.x_pos = obj.prev_x_pos
                        obj.y_pos = obj.prev_y_pos
                        obj.update_hitbox()


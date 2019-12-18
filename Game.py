import pygame
import sys
from Entity import *
from Map import *
from Const import *


def create_enemy():
    return Entity([player.x_pos, player.y_pos - 100], grid_size, 1, Colors().BLUE, Shapes().RECT)

# convert screen pixel units to grid units
def pix_to_grid(pix):
    return pix / grid_size

# convert grid units to screen pixel units
def grid_to_pix(grid):
    return grid * grid_size + grid_size/2

def check_collision(obj1, obj2):
    col = False
    x_dis = abs(obj1.x_pos - obj2.x_pos)
    y_dis = abs(obj1.y_pos - obj2.y_pos)
    if(x_dis < obj1.size/2 + obj2.size/2):
        if (y_dis < obj1.size / 2 + obj2.size / 2):
            col = True
    return col

def check_oob(obj):
    if (obj.x_pos < 0):
        obj.x_pos = WIDTH
    if (obj.x_pos > WIDTH):
        obj.x_pos = 0
    if (obj.y_pos > HEIGHT):
        obj.y_pos = 0
    if (obj.y_pos < 0):
        obj.y_pos = HEIGHT

def check_wall(obj):
    grid_x = pix_to_grid(obj.x_pos)
    grid_y = pix_to_grid(obj.y_pos)

    #print("Check:")
    for i in range(int(max(0, grid_x-1)), int(min(map.x-1, grid_x+1)+1)):
        for j in range(int(max(0, grid_y-1)), int(min(map.y-1, grid_y+1)+1)):
            #print(f"{(i)} {j}")
            wall = map.walls[j][i]
            if (wall != None):
                if(check_collision(wall, obj)):
                    obj.x_pos = obj.prev_x_pos
                    obj.y_pos = obj.prev_y_pos


pygame.init()

# map
GRID_SIZE = 40
WALLS = [
    [1, 0, 1, 1, 0, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 1, 1, 1]
]
map = Map(WALLS, GRID_SIZE)

# screen
WIDTH = map.x * map.grid_size
HEIGHT = map.y * map.grid_size
screen = pygame.display.set_mode((WIDTH, HEIGHT))

grid_size = map.grid_size
bg_color = Colors().BLACK

# player
player = Entity(
    (grid_to_pix(5), grid_to_pix(5)),
    grid_size, 5,
    Colors().RED, Shapes().RECT)

# enemy
enemies = []
enemy_spawn_timer = 0
ENEMY_SPAWN_TIME = 2
max_enemy = 1

game_over = False

clock = pygame.time.Clock()
FPS = 60

left_press = False
right_press = False
down_press = False
up_press = False

while not game_over:
    # event checker
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            print('quit')
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                left_press = True
            if event.key == pygame.K_RIGHT:
                right_press = True
            if event.key == pygame.K_DOWN:
                down_press = True
            if event.key == pygame.K_UP:
                up_press = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                left_press = False
            if event.key == pygame.K_RIGHT:
                right_press = False
            if event.key == pygame.K_DOWN:
                down_press = False
            if event.key == pygame.K_UP:
                up_press = False

    # moving player
    if left_press:
        player.move((-1, 0))
    if right_press:
        player.move((1, 0))
    if up_press:
        player.move((0, 1))
    if down_press:
        player.move((0, -1))

    check_oob(player)
    check_wall(player)

    screen.fill(bg_color)
    map.draw_walls(screen)

    # draw player
    player.draw_entity(screen)

    # enemy
    for e in enemies:
        check_oob(e)
        e.draw_entity(screen)
        if (check_collision(e, player)):
            game_over = True
        e.move((0,-1))
        check_wall(e)
        # if (e.y_pos > WIDTH):
        #     enemies.remove(e)
            # enemies.append(create_enemy())

    enemy_spawn_timer += 1
    if (enemy_spawn_timer == ENEMY_SPAWN_TIME * FPS):
        enemy_spawn_timer = 0
        if (len(enemies) < max_enemy):
            enemies.append(create_enemy())

    clock.tick(FPS)

    pygame.display.update()

print("Game Over")

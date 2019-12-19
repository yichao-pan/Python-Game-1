import pygame
import sys
from Entity import *
from Map import *
from Const import *


def create_enemy():
    return Entity([player.x_pos, player.y_pos - 100], grid_size, 1, Colors().BLUE, Shapes().RECT)


pygame.init()

# create map
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
game_map = Map(WALLS, GRID_SIZE)

# screen
WIDTH = game_map.map_width
HEIGHT = game_map.map_height
grid_size = game_map.grid_size

screen = pygame.display.set_mode((WIDTH, HEIGHT))
bg_color = Colors().BLACK

# player
player = Entity(
    (game_map.grid_to_pix(5), game_map.grid_to_pix(5)),
    grid_size, 5,
    Colors().RED, Shapes().RECT)

# enemy
enemies = []
enemy_spawn_timer = 0  # counter for enemy spawning
ENEMY_SPAWN_TIME = 2
max_enemy = 0

game_over = False

# clock
clock = pygame.time.Clock()
FPS = 60

# controls
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

        move = False
        if event.type == pygame.KEYUP:
            move = False
            if event.key == pygame.K_LEFT:
                left_press = False
            if event.key == pygame.K_RIGHT:
                right_press = False
            if event.key == pygame.K_DOWN:
                down_press = False
            if event.key == pygame.K_UP:
                up_press = False

        if event.type == pygame.KEYDOWN:
            move = True
            if event.key == pygame.K_LEFT:
                left_press = True
            if event.key == pygame.K_RIGHT:
                right_press = True
            if event.key == pygame.K_DOWN:
                down_press = True
            if event.key == pygame.K_UP:
                up_press = True

    # moving player
    if (move):
        move_x = 0
        move_y = 0
        if left_press:
            move_x = -1
        if right_press:
            move_x = 1
        if up_press:
            move_y = 1
        if down_press:
            move_y = -1
        player.move((move_x, move_y))

    game_map.check_oob(player)
    game_map.check_wall(player)

    screen.fill(bg_color)
    game_map.draw_walls(screen)

    # draw player
    player.draw(screen)

    # enemy
    for e in enemies:
        game_map.check_oob(e)
        e.draw(screen)
        if (game_map.check_collision(e, player)):
            game_over = True
        e.move((0, -1))
        game_map.check_wall(e)
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

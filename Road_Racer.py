import pygame
import random
import math
import time
from pygame import mixer

pygame.init()

screen = pygame.display.set_mode((800, 600))

background = pygame.image.load('road_background.png')

icon = pygame.image.load('car_logo.png')
pygame.display.set_icon(icon)

mixer.music.load('background_music.wav')
mixer.music.play(-1)

car = pygame.image.load('car.png')
carX = 336
carY = 480
carX_change = 0
carY_change = 0

enemy_car_load = pygame.image.load('enemy_car.png')
enemy_car_size = pygame.transform.scale(enemy_car_load, (85, 70))
enemy_car = pygame.transform.rotate(enemy_car_size, 180)
enemy_carX = random.randint(150, 630)
enemy_carY = random.choice([-10, -30, -40])
enemy_carY_change = 5


def print_enemy_car():
    screen.blit(enemy_car, (enemy_carX, enemy_carY))


enemy_car_load1 = pygame.image.load('car_enemy_1.png')
enemy_car_size1 = pygame.transform.scale(enemy_car_load1, (85, 70))
enemy_car1 = pygame.transform.rotate(enemy_car_size1, 180)
enemy_carX1 = random.randint(150, 630)
enemy_carY1 = random.choice([-80, -100, -130])
enemy_carY_change1 = 5


def print_enemy_car1():
    screen.blit(enemy_car1, (enemy_carX1, enemy_carY1))


enemy_car_load2 = pygame.image.load('car_enemy_2.png')
enemy_car_size2 = pygame.transform.scale(enemy_car_load2, (85, 70))
enemy_car2 = pygame.transform.rotate(enemy_car_size2, 180)
enemy_carX2 = random.randint(150, 630)
enemy_carY2 = random.choice([-160, -200, -180])
enemy_carY_change2 = 5


def print_enemy_car2():
    screen.blit(enemy_car2, (enemy_carX2, enemy_carY2))


enemy_car_load3 = pygame.image.load('enemy_car_3.png')
enemy_car_size3 = pygame.transform.scale(enemy_car_load3, (85, 70))
enemy_car3 = pygame.transform.rotate(enemy_car_size3, 180)
enemy_carX3 = random.randint(150, 630)
enemy_carY3 = random.choice([-70, -145, -250])
enemy_carY_change3 = 5


def print_enemy_car3():
    screen.blit(enemy_car3, (enemy_carX3, enemy_carY3))


def print_car():
    screen.blit(car, (carX, carY))


def cheak_collision(carX, carY, enemy_carX, enemy_carY):
    distance = math.sqrt((math.pow(carX - enemy_carX, 2) + (math.pow(carY - enemy_carY, 2))))
    if distance <= 27:
        return True
    else:
        return False


def cheak_collision1(carX, carY, enemy_carX1, enemy_carY1):
    distance = math.sqrt((math.pow(carX - enemy_carX1, 2) + (math.pow(carY - enemy_carY1, 2))))
    if distance <= 27:
        return True
    else:
        return False


def cheak_collision2(carX, carY, enemy_carX2, enemy_carY2):
    distance = math.sqrt((math.pow(carX - enemy_carX2, 2) + (math.pow(carY - enemy_carY2, 2))))
    if distance <= 27:
        return True
    else:
        return False


def cheak_collision3(carX, carY, enemy_carX3, enemy_carY3):
    distance = math.sqrt((math.pow(carX - enemy_carX3, 2) + (math.pow(carY - enemy_carY3, 2))))
    if distance <= 27:
        return True
    else:
        return False


score = 0
score_font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10


def print_score(x, y):
    score_print = score_font.render("Score:" + str(score), True, (0, 0, 0))
    screen.blit(score_print, (x, y))


running = True

while running:
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    mouse_pos = pygame.mouse.get_pos()
    carX = mouse_pos[0]

    collision = cheak_collision(carX, carY, enemy_carX, enemy_carY)
    if collision:
        car_crashed = mixer.Sound('crash.wav')
        car_crashed.play()
        time.sleep(2)
        quit()
    collision1 = cheak_collision1(carX, carY, enemy_carX1, enemy_carY1)
    if collision1:
        car_crashed = mixer.Sound('crash.wav')
        car_crashed.play()
        time.sleep(2)
        quit()
    collision2 = cheak_collision2(carX, carY, enemy_carX2, enemy_carY2)
    if collision2:
        car_crashed = mixer.Sound('crash.wav')
        car_crashed.play()
        time.sleep(2)
        quit()
    collision3 = cheak_collision3(carX, carY, enemy_carX3, enemy_carY3)
    if collision3:
        car_crashed = mixer.Sound('crash.wav')
        car_crashed.play()
        time.sleep(2)
        quit()
    if carX >= 630:
        carX = 630
    if carX <= 150:
        carX = 150
    if enemy_carY >= 536:
        enemy_carX = random.randint(150, 630)
        enemy_carY = random.choice([-10, -30, -50])
        score += 1
    if enemy_carY1 >= 536:
        enemy_carX1 = random.randint(150, 630)
        enemy_carY1 = random.choice([-70, -100, -130])
        score += 1
    enemy_carY1 += enemy_carY_change1
    if enemy_carY2 >= 536:
        enemy_carX2 = random.randint(150, 630)
        enemy_carY2 = random.choice([-160, -200, -180])
        score += 1
    if enemy_carY3 >= 536:
        enemy_carX3 = random.randint(150, 630)
        enemy_carY3 = random.choice([-70, -145, -250])
        score += 1
    enemy_carY3 += enemy_carY_change3
    enemy_carY2 += enemy_carY_change2
    enemy_carY += enemy_carY_change
    carX += carX_change
    print_car()
    print_enemy_car3()
    print_enemy_car()
    print_enemy_car1()
    print_enemy_car2()
    print_score(textX, textY)
    pygame.display.update()

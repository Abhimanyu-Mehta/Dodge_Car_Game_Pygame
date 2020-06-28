import pygame
import random
import math
from pygame import mixer


def game_loop():
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

    with open("Hiscore_Manager.txt", "r") as f:
        hiscore = f.read()

    def cheak_collision3(carX, carY, enemy_carX3, enemy_carY3):
        distance = math.sqrt((math.pow(carX - enemy_carX3, 2) + (math.pow(carY - enemy_carY3, 2))))
        if distance <= 27:
            return True
        else:
            return False

    score = 0
    score_font = pygame.font.Font('font.ttf', 36)
    textX = 10
    textY = 10

    def print_score(x, y):
        score_print = score_font.render("Score:" + str(score), True, (0, 0, 0))
        screen.blit(score_print, (x, y))

    hiscore_font = pygame.font.Font('font.ttf', 36)
    hiscore_textX = 590
    hiscore_textY = 10

    def print_hiscore(x, y):
        hiscore_print = hiscore_font.render("Hiscore:" + str(hiscore), True, (0, 0, 0))
        screen.blit(hiscore_print, (x, y))

    game_over = pygame.font.Font('freesansbold.ttf', 45)
    fontX = 5
    fontY = 270

    def print_game_over():
        game_over_ = game_over.render("GAME OVER! Press Enter to restart", True, (0, 0, 0))
        screen.blit(game_over_, (fontX, fontY))

    running = True
    game_over_ = False

    while running:
        if game_over_:
            with open("Hiscore_Manager.txt", "w") as f:
                f.write(str(hiscore))
            screen.blit(background, (0, 0))
            print_game_over()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        game_loop()
        else:
            screen.blit(background, (0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            mouse_pos = pygame.mouse.get_pos()
            carX = mouse_pos[0]

            if score > float(hiscore):
                hiscore = score

            collision = cheak_collision(carX, carY, enemy_carX, enemy_carY)
            if collision:
                car_crashed = mixer.Sound('crash.wav')
                car_crashed.play()
                enemy_carY_change = 0
                enemy_carY_change1 = 0
                enemy_carY_change2 = 0
                enemy_carY_change3 = 0
                game_over_ = True
            collision1 = cheak_collision1(carX, carY, enemy_carX1, enemy_carY1)
            if collision1:
                car_crashed = mixer.Sound('crash.wav')
                car_crashed.play()
                enemy_carY_change = 0
                enemy_carY_change1 = 0
                enemy_carY_change2 = 0
                enemy_carY_change3 = 0
                game_over_ = True
            collision2 = cheak_collision2(carX, carY, enemy_carX2, enemy_carY2)
            if collision2:
                car_crashed = mixer.Sound('crash.wav')
                car_crashed.play()
                enemy_carY_change = 0
                enemy_carY_change1 = 0
                enemy_carY_change2 = 0
                enemy_carY_change3 = 0
                game_over_ = True
            collision3 = cheak_collision3(carX, carY, enemy_carX3, enemy_carY3)
            if collision3:
                car_crashed = mixer.Sound('crash.wav')
                car_crashed.play()
                enemy_carY_change = 0
                enemy_carY_change1 = 0
                enemy_carY_change2 = 0
                enemy_carY_change3 = 0
                game_over_ = True
            if score == 10:
                enemy_carY_change = 8
                enemy_carY_change1 = 8
                enemy_carY_change2 = 8
                enemy_carY_change3 = 8

            if carX >= 630:
                carX = 630
            if carX <= 150:
                carX = 150
            if enemy_carY >= 536:
                enemy_carX = random.randint(150, 630)
                enemy_carY = random.choice([-10, -30, -50])
                score += .25
            if enemy_carY1 >= 536:
                enemy_carX1 = random.randint(150, 630)
                enemy_carY1 = random.choice([-70, -100, -130])
                score += .25
            enemy_carY1 += enemy_carY_change1
            if enemy_carY2 >= 536:
                enemy_carX2 = random.randint(150, 630)
                enemy_carY2 = random.choice([-160, -200, -180])
                score += .25
            if enemy_carY3 >= 536:
                enemy_carX3 = random.randint(150, 630)
                enemy_carY3 = random.choice([-70, -145, -250])
                score += .25
            enemy_carY3 += enemy_carY_change3
            enemy_carY2 += enemy_carY_change2
            enemy_carY += enemy_carY_change
            carX += carX_change
            print_car()
            print_hiscore(hiscore_textX, hiscore_textY)
            print_enemy_car3()
            print_enemy_car()
            print_enemy_car1()
            print_enemy_car2()
            print_score(textX, textY)
        pygame.display.update()


game_loop()

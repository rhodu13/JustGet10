import pickle
import pygame
from pygame.locals import *
from bases import *
from possibles import *
from merge import *


GRAY = (140, 140, 140)
BLACK = (10,  10,  10)
NAVYBLUE = (60,  60, 100)
WHITE = (245, 245, 245)
OFFWHITE = (230, 230, 230)
OFFWHITE2 = (205, 205, 205)
RED = (255,  35,   0)
ORANGE = (255, 150,   0)
YELLOW = (255, 241,   0)
LIME = (205, 255,   0)
GREEN = (0, 220,  30)
LIGHTBLUE = (4, 214, 211)
BLUE = (18,  37, 219)
PURPLE = (120,  11, 165)
BLEU = (0,  177, 255)


width = 1000
height = 600
margin = 200
celSize = 80


pygame.init()
pygame.display.set_caption('Just get 10 !')
window = pygame.display.set_mode((width, height))
pygame.display.flip()
n = 6
proba = (0.04,0.30,0.6)
progress = True
gameBoard = newBoard(n, proba)
n = 5
k = maxValue(n, gameBoard)
while progress:
    if proba == (0.04, 0.30, 0.6):
        background = pygame.image.load("assets/images/difficulty.png").convert()
        window.blit(background, (0, 0))
        pygame.display.update()
    if proba != (0.04, 0.30, 0.6):
        k = maxValue(n, gameBoard)
        maPolice = pygame.font.SysFont("comicsansms", 20)
        background = pygame.image.load("assets/images/background.png").convert()
        window.blit(background, (0, 0))
        finalScoreValue = maPolice.render(str(k), True, (122, 212, 255))
        finalScoreValueSurface = finalScoreValue.get_rect()
        finalScoreValueSurface.topleft = (374, 32)
        window.blit(finalScoreValue, finalScoreValueSurface)
        display(gameBoard, n, margin, celSize, window)
    for event in pygame.event.get():
        if event.type == QUIT:
            progress = False
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                progress = False
            if event.key == K_4:
                n = 4
            if event.key == K_5:
                n = 5
            if event.key == K_6:
                n = 6
        if event.type == MOUSEBUTTONDOWN:
            x, y = event.pos
            print(gameBoard)
            if 270 < x < 530 and 140 < y < 210 and proba == (0.04, 0.30, 0.6):
                proba = (0.2, 0.60, 0.2)
            if 270 < x < 530 and 260 < y < 330 and proba == (0.04, 0.30, 0.6):
                proba = (0.05, 0.3, 0.6)
            if 270 < x < 530 and 380 < y < 450 and proba == (0.04, 0.30, 0.6):
                proba = (0.01, 0.2, 0.3)
            if 720 < x < 900 and 347 < y < 394 and defeat(n, gameBoard):
                with open('save.txt', 'wb') as save:
                    pickle.dump(gameBoard, save)
                save.close()
            if 720 < x < 900 and 414 < y < 460:
                with open('save.txt', 'rb') as save:
                    gameBoard = pickle.load(save)
                save.close()
                display(gameBoard, n, margin, celSize, window)
                pygame.display.update()
            if 720 < x < 940 and 480 < y < 520:
                progress = False
            if 680 < x < 940 and 250 < y < 320 and not defeat(n, gameBoard) or k == 10:
                background = pygame.image.load("assets/images/background.png").convert()
                window.blit(background, (0, 0))
                gameBoard = newBoard(n, proba)
                proba = (0.04, 0.30, 0.6)
            if maxValue(n, gameBoard) != 10:
                for row in range(n):
                    for cel in range(n):
                        if margin + row * celSize < x < margin + row * celSize + 80 and 100 + cel * celSize < y < 100 + cel * celSize + 80:
                            i, j = cel, row
                            if validCase(n, gameBoard, i, j):
                                az = (i, j)
                                checkList = [(i, j)]
                                stockList = propagation(n, gameBoard, checkList)
                                modification(n, gameBoard, stockList, az)
                                display(gameBoard, n, margin, celSize, window)
                                pygame.display.update()
                                pygame.time.wait(500)
                                gravity(gameBoard, n, proba)
                                display(gameBoard, n, margin, celSize, window)
                                pygame.display.update()
            if maxValue(n, gameBoard) == 10:
                pygame.mixer.music.load('assets/sounds/victory.wav')
                pygame.mixer.music.play()
            if not defeat(n, gameBoard) and maxValue(n, gameBoard) != 10:
                pygame.mixer.music.load('assets/sounds/defeat.wav')
                pygame.mixer.music.play()
    if maxValue(n, gameBoard) == 10:
        k = maxValue(n, gameBoard)
        background = pygame.image.load("assets/images/background2.png").convert()
        window.blit(background, (0, 0))
        finalScoreValue = maPolice.render(str(k), True, (122, 212, 255))
        finalScoreValueSurface = finalScoreValue.get_rect()
        finalScoreValueSurface.topleft = (385, 30)
        window.blit(finalScoreValue, finalScoreValueSurface)
        display(gameBoard, n, margin, celSize, window)
        backgroundVictory = pygame.image.load("assets/images/victory.png").convert_alpha()
        window.blit(backgroundVictory, (170, 260))
        pygame.display.update()
    if not defeat(n, gameBoard) and maxValue(n, gameBoard) != 10:
        k = maxValue(n,gameBoard)
        background = pygame.image.load("assets/images/background2.png").convert()
        window.blit(background, (0, 0))
        finalScoreValue = maPolice.render(str(k), True, (122, 212, 255))
        finalScoreValueSurface = finalScoreValue.get_rect()
        finalScoreValueSurface.topleft = (385, 30)
        window.blit(finalScoreValue, finalScoreValueSurface)
        display(gameBoard, n, margin, celSize, window)
        backgroundDefeat = pygame.image.load("assets/images/defeat.png").convert_alpha()
        window.blit(backgroundDefeat, (200, 260))
        pygame.display.update()
    pygame.display.update()
pygame.quit()
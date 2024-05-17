import random
import sys, pygame


def rand(proba):
    x1,x2,x3 = proba
    randomvalue = random.random()
    if randomvalue < x1:
        return 4
    if x1 <= randomvalue <= x2:
        return 3
    if x2 <= randomvalue <= x3:
        return 2
    else:
        return 1


def newBoard(n, proba):
    board = [[0] * n for _ in range(n)]
    for x in range(n):
        for i in range(n):
            f = rand(proba)
            if x < n:
                board[x][i]=f
    return board


def display(gameBoard, n, margin, celSize, window):
    color = [(178, 239, 87), (68, 187, 248), (255, 192, 94), (255, 104, 80), (0, 149, 126), (106, 96, 243), (247, 82, 184), (230, 43, 63), (255, 243, 77), (44, 62, 80)]
    for row in range(n):
        for cel in range(n):
            i = gameBoard[cel][row]-1
            font = pygame.font.SysFont("comicsansms", 40)
            pygame.draw.rect(window, color[i], ((margin+row*celSize), (100+cel*celSize), celSize, celSize), 0)
            pygame.draw.rect(window, (10,  10,  10), (margin, 100, celSize*n, celSize*n), 2)
            afficher = font.render(str(gameBoard[cel][row]), 1, (10,  10,  10))
            window.blit(afficher, ((margin+25+row*celSize), 100+10+cel*celSize))
    return window
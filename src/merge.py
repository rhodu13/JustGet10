from possibles import *
from bases import *

def check(n, gameBoard, i, j, checkList):
    if 0 <= i < n and 0 <= j - 1 < n and gameBoard[i][j] == gameBoard[i][j - 1]:
        checkList.append((i, j - 1))
    if 0 <= i - 1 < n and 0 <= j < n and gameBoard[i][j] == gameBoard[i - 1][j]:
        checkList.append((i - 1, j))
    if 0 <= i < n and 0 <= j + 1 < n and gameBoard[i][j] == gameBoard[i][j + 1]:
        checkList.append((i, j + 1))
    if 0 <= i + 1 < n and 0 <= j < n and gameBoard[i][j] == gameBoard[i + 1][j]:
        checkList.append((i + 1, j))
    return checkList


def propagation(n, gameBoard, checkList):
    stockList = set()
    while len(checkList) != 0:
        i,j = checkList.pop()
        if (i, j) not in stockList:
            check(n, gameBoard, i, j, checkList)
            stockList.add((i, j))
    return stockList


def modification(n, gameBoard, stockList, az):
    stockList = list(stockList)
    y, x = az
    o = gameBoard[y][x]
    for l in range(len(stockList)):
        i, j = stockList[l]
        gameBoard[i][j] = 0
    gameBoard[y][x] = o+1
    return gameBoard

def gravity(gameBoard,n,proba):
    a = n
    while a != 0:
        for j in range(n):
            for i in range(n):
                if 0 <= j + 1 < n and 0 <= i < n and gameBoard[j + 1][i] == 0:
                    gameBoard[j+1][i], gameBoard[j][i] = gameBoard[j][i], gameBoard[j+1][i]
        a -= 1
    for c in range(n):
        for r in range(n):
            if gameBoard[c][r] == 0:
                gameBoard[c][r] = rand(proba)
    return gameBoard


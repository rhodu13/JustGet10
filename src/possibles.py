def validCase(n, gameBoard, i, j):
    if 0 <= i < n and 0 <= j - 1 < n and gameBoard[i][j] == gameBoard[i][j - 1]:
        return True
    elif 0 <= i-1 < n and 0 <= j < n and gameBoard[i][j] == gameBoard[i - 1][j]:
        return True
    elif 0 <= i < n and 0 <= j + 1 < n and gameBoard[i][j] == gameBoard[i][j + 1]:
        return True
    elif 0 <= i + 1 < n and 0 <= j < n and gameBoard[i][j] == gameBoard[i + 1][j]:
        return True
    else:
        return False


def defeat(n, gameBoard):
    for j in range(n):
        for i in range(n):
            if validCase(n, gameBoard, i, j):
                return True
    return False


def maxValue(n, gameBoard):
    k = 0
    for j in range(n):
        for i in range(n):
            if gameBoard[i][j] > k:
                k = gameBoard[i][j]
    return k
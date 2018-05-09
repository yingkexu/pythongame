import random

def drawBoard(board):
    print(board[7] + '|' + board[8] + '|' +board[9])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[1] + '|' + board[2] + '|' + board[3])


def inputPlayerLetter():
    letter = ' '
    while not(letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = input().upper()
        if letter == 'X':
            return ['X','O']
        else: 
            return['O','X']        
               
def whoGoesForst():
    if random.randint(0,1) == 0:
        return 'computer'
    else:
        return'player'

def makeMove(board, letter, move):
    board[move] = letter



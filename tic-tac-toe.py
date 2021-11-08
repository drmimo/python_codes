import random
def checkWinner(b):
    #It checks the board to find if there is a winner
    global game_over
    for i in range(3):
        if b[0][i] == b[1][i] and b[1][i] == b[2][i] and b[2][i] != '_':
            print("Congrats! {} is the WINNNER!".format(b[0][i]))
            game_over = True
            return
        
    for i in range(3):
        if b[i][0] == b[i][1] and b[i][1] == b[i][2] and b[i][2] != '_':
            print("Congrats! {} is the WINNNER!".format(b[i][0]))
            game_over = True
            return
    
    #Diagonals
    if b[0][0] == b[1][1] and b[1][1] == b[2][2] and b[2][2] != '_':
        print("Congrats! {} is the WINNER!".format(b[1][1]))
        game_over = True
        return

    if b[2][0] == b[1][1] and b[1][1] == b[0][2] and b[0][2] != '_':
            print("Congrats! {} is the WINNNER!".format(b[1][1]))
            game_over = True
            return

    emptyPlacesOnBoard = False
    for row in b:
        for cell in row:
            if cell == '_':
                emptyPlacesOnBoard = True
                break
    
    if not emptyPlacesOnBoard:
        print("DRAW !!!")
        print("Game Over")
        game_over = True


def drawBoard(b):
    #It draws the board of the game
    for row in b:
        print(row)

def askForPlaying(b, mark):
    #Ask for coordinates to put the mark on board
    print("\nIt\'s the role of {}".format(mark))
    while True:
        x = int(input("Line number (0-2): "))
        while x > 2 or x < 0:
            x = int(input("Line number (0-2): "))
        
        y = int(input("Column number (0-2): "))
        while y > 2 or y < 0:
            y = int(input("Column number (0-2): "))
        
        if b[x][y] == '_':
            b[x][y] = mark
            break
        else:
            print("The place at the board is full. Try again!")

def togglePlayer(p):
    return players[(players.index(p)+1) % 2]


#Here is the variable that hold the whole game board
board = [['_','_','_'], ['_', '_', '_'], ['_','_','_']]
#A list of game symbols X and O to choose randomly from them at the game start
players = ['X', 'O']

XO = random.choice(players)
print("The player {} will start playing ...".format(XO))
game_over = False

while not game_over:
    askForPlaying(board, XO)
    drawBoard(board)
    checkWinner(board)

    XO = togglePlayer(XO)


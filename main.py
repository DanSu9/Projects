import random


#  prints the game board
def printboard(boardp):  # prints the board
    # prints the board
    print("Current Game Board:\n")
    for x in range(1, 10):
        if x % 3 != 0 & x != 1:
            print(boardp[x - 1] + "|", end="")
        else:
            print(boardp[x - 1])
            if x < 9:
                print("------------")
    print("\n")


# decides the turn and assigns the choice to the board
def turn(boardg, gamepiece, player):
    if ' - ' in boardg:
        print("Where would you like to place your piece? Choose 1-9 \n")
        printboard(boardg)
        move = int(input())
        if move >= 1 & move <= 9:
            if '-' not in boardg[move -1]:
                print("Position already taken, try again")
                turn(boardg, gamepiece, player)
            else:
                boardg[move - 1] = " " + gamepiece + " "
        else:
            print("Wrong Choice! please enter only numbers between 1-9. \n")
            turn(boardg, gamepiece, player)
    return boardg


#  switches the current player
def nextplayer(currentplayer):
    if currentplayer.upper() == 'X':
        currentplayer = 'O'
        print(" 'O's Turn! ")
    else:
        print(" 'X's Turn! ")
        currentplayer = 'X'
    return currentplayer.upper()


def boardreset(boardx):
    # resets the board
    boardx = [" - ", " - ", " - ",
              " - ", " - ", " - ",
              " - ", " - ", " - "]
    return boardx


def checkwin(boardgame):  # returns win, winner
    # winner is for the winning char
    # win variable determines how the victory was made
    win = 0
    winner = ''
    #                       win in a row
    if ' - ' not in boardgame:
        win = 4
    elif boardgame[0] == boardgame[1] == boardgame[2]:
        if ' - ' not in boardgame[0]:
            win = 1
            winner = boardgame[0]
    elif boardgame[3] == boardgame[4] == boardgame[5]:
        if ' - ' not in boardgame[3]:
            win = 1
            winner = boardgame[3]
    elif boardgame[6] == boardgame[7] == boardgame[8]:
        if ' - ' not in boardgame[6]:
            win = 1
            winner = boardgame[6]
    #                       win in a cross
    elif boardgame[0] == boardgame[4] == boardgame[8]:
        if ' - ' not in boardgame[0]:
            win = 2
            winner = boardgame[0]
    elif boardgame[2] == boardgame[4] == boardgame[6]:
        if ' - ' not in boardgame[2]:
            win = 2
            winner = boardgame[2]
    #                        win in a column
    elif boardgame[0] == boardgame[3] == boardgame[6]:
        if ' - ' not in boardgame[0]:
            win = 3
            winner = boardgame[0]
    elif boardgame[1] == boardgame[4] == boardgame[7]:
        if ' - ' not in boardgame[1]:
            win = 3
            winner = boardgame[1]
    elif boardgame[2] == boardgame[5] == boardgame[8]:
        if ' - ' not in boardgame[2]:
            win = 3
            winner = boardgame[2]
    return win, winner


#  determines the way the victory was made
def determinewinway(win, winner):
    results = ['', '']
    if win == 1:
        print("Victory! the winner is %s , Victory by a row! Nice!" % winner)
        if winner.upper() == 'X':
            results[0] = 'X'
        else:
            results[0] = 'O'
        print("Play again? y/n")
        results[1] = input().upper()
    if win == 2:
        print("Victory! the winner is %s , Victory by a cross! Nice!" % winner)
        if winner.upper() == 'X':
            results[0] = 'X'
        else:
            results[0] = 'O'
        print("Play again? y/n")
        results[1] = input().upper()
    if win == 3:
        print("Victory! the winner is %s , Victory by a column! Nice!" % winner)
        if winner.upper() == 'X':
            results[0] = 'X'
        else:
            results[0] = 'O'
        print("Play again? y/n")
        results[1] = input().upper()
    if win == 4:
        print("its a tie! Play again? y/n")
        results[1] = input().upper()
    return results


#  the turn of the computer, chooses randomly on the board
def computerplay(boardg, piece):
    rand = random.randint(0, 8)
    if boardg[rand] == " - ":
        boardg[rand] = " " + piece + " "
    else:
        computerplay(boardg, piece)
    return boardg


#  Initializing the game, uses functions: drawwhostarts(player, comp) & boardreset(boardx)
def gamestart(boardg):
    arr = ["", "", ""]
    boardg = boardreset(boardg)
    print("------New Game-----\n\n\n")
    gamepiece = input("Choose your game piece: X | O :\n").upper()
    player = gamepiece.upper()
    comp = ''
    if player.upper() == 'X':
        comp = 'O'
    else:
        comp = 'X'
    print("You are %c ." % player)
    gamepiece = drawwhostarts(player, comp)
    arr = [gamepiece, player, comp, boardg]
    return arr


#  chooses randomly who will start
def drawwhostarts(player, comp):
    starter = random.randint(0, 1)
    if starter == 1:
        print("\nYou start! \n")
        return player
    else:
        print("Computer starts! \n")
        return comp


#  determines if the game board is full or there is a winner from the very last move
def isfinishedorwinner(boardg):
    status = False
    if " - " not in boardg:
        status = True
    if checkwin(board)[1] != '':
        status = True
    return status


#                   main code
action = True
board = [" - ", " - ", " - ",
         " - ", " - ", " - ",
         " - ", " - ", " - "]
print("Welcome to the Tic Tac Toe game!")
gamestartarr = gamestart(board)
while action:
    print("\n________________________\n")
    if gamestartarr[0] == gamestartarr[1]:
        # if current player equals to player's game piece - player will play
        # otherwise - computer will randomly place it's game piece on the board
        board = turn(board, gamestartarr[0], gamestartarr[1])
    else:
        # computer move
        board = computerplay(board, gamestartarr[2])
    printboard(board)
    if isfinishedorwinner(board):
        # making sure that the move wasn't the last move of the game
        # and in addition checking if there is a winner for the current board
        if determinewinway(checkwin(board)[0], checkwin(board)[1])[1].upper() == 'N':
            action = False
        else:
            gamestartarr = gamestart(board)
            board = gamestartarr[3]
    else:
        # if there is no current winner and there are still slots available -
        # - the current player will change
        gamestartarr[0] = nextplayer(gamestartarr[0].upper())
print("\n")
print("Goodbye!")

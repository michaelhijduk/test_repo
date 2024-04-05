# CLI python script for playing Battleship

import random

ships = {
    'carrier': 5,
    'battleship': 4,
    'cruiser': 3,
    'submarine': 3,
    'destroyer': 2
}

def boardSetUp(rows, cols):
    gameboard = [[' ' for y in range(cols)] for x in range(rows)]
    return gameboard

def placementLogic(gameboard, ship):
    randNums = createRandomness()
    if gameboard[randNums[0]][randNums[1]] != 0:
        placementLogic(gameboard, ship)

    match randNums[2]:
        case 0:
            if randNums[0] - ships[ship] < 0:
                placementLogic(gameboard, ship)
            for i in range(ships[ship]):
                if gameboard[randNums[0] - i][randNums[1]] != 0:
                    placementLogic(gameboard, ship)
            for i in range(ships[ship]):
                gameboard[randNums[0] - i][randNums[1]] = ships[ship]
        case 1:
            if randNums[1] - ships[ship] < 0:
                placementLogic(gameboard, ship)
            for i in range(ships[ship]):
                if gameboard[randNums[1] - i][randNums[0]] != 0:
                    placementLogic(gameboard, ship)
            for i in range(ships[ship]):
                gameboard[randNums[1] - i][randNums[0]] = ships[ship]
        case 2:
           if randNums[1] - ships[ship] < 0:
                placementLogic(gameboard, ship)
           for i in range(ships[ship]):
                if gameboard[randNums[1] - i][randNums[0]] != 0:
                                placementLogic(gameboard, ship)
                        for i in range(ships[ship]):
                            gameboard[randNums[1] - i][randNums[0]] = ships[ship]
        case 3:

    return gameboard
    

def placeShipsRand(gameboard):
    for ship in ships:
        gameboard = placementLogic
    return  gameboard

def createRandomness():
    y = random.randint(0, 9)
    x = random.randint(0, 9)
    d = random.randint(0, 3)
    return [y, x, d]

def displayBoard(matrix) -> None:
    for row in matrix:
        print()
        for x in row:
            print('[%s]' % (x), end = '')
    print()       
    
def main():

    print('''
    Welcome to CLIBattleship!\n\n
    This is version 0.1, so it has limited functionality.
    For example, your ship placement will be generated randomly.\n\n
    The following symbols will be used:\n
    [ ] - Untouched Tile
    [^] - Missed Guess
    [#] - Hit
    [1] - Carrier Ship
    [2] - Battleship
    [3] - Cruiser
    [4] - Submarine
    [5] - Destroyer\n
    ''')
    # TODO: easy/medium/hard
    gameboard = boardSetUp(10, 10)
    print('Your Board:')
    # TODO: custom ship placement
    # displayBoard(placeShipsRand(gameboard))
    displayBoard(gameboard)
    

if __name__ == "__main__":
    main()

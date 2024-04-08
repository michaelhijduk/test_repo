# CLI python script for playing Connect 4

# TODO: add stats

import random

# def initBoard():

def replay():
    while True:
        ans = input("Do you want to return to the menu? ('y'/'n')\n").lower()
        if ans != 'y' and ans != 'n':
            print("\nPlease enter 'y' (yes) or 'n' (no)\n")
        return ans
    
def playGame():
    print('''
    \\/\\/\\/ Menu \\/\\/\\/\n
    [1] - Stats
    [2] - Standard Game
    [3] - Spectate AI
    [4] - Multiplayer
    ''')
    choice = input("Enter your selection:\n")
    match choice:
        case 1:
            viewStats()
        case 2:
            standardGame()
        case 3:
            spectate()
        case 4:
            multiplayer()
        case _:
            
            
    return replay()

def main():
    print('Welcome to command-line Connect 4!\n')
    while True:
        if playGame() == 'n':
            break
    print('Thanks for playing!')

if __name__ == '__main__':
    main()

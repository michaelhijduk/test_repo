# CLI python script for playing Connect 4

# TODO: store stats persistantly
stats = {
    'Games Played': 0,
    'Games Won': 0,
    'Win-to-Loss Ratio': 0.0,
    'Tokens Dropped': 0,
    'Fewest Token Win': None,
    'Most Token Win': None,
    'Fastest Win': None
}

import random

# def initBoard():

def viewStats():
    print()
    for stat in stats:
        print('%s: %s' % (stat, stats[stat]))

def replay():
    while True:
        ans = input("\nDo you want to return to the menu? ('y'/'n')\n").lower()
        if ans != 'y' and ans != 'n':
            print("\nPlease enter 'y' (yes) or 'n' (no)\n")
        return ans

def mainMenu():
    print('''
    \\/\\/\\/ Menu \\/\\/\\/\n
    [1] - Stats
    [2] - Standard Game
    [3] - Spectate AI
    [4] - Multiplayer
    ''')
    while True:
        choice = input("Enter your selection:\n")
        match choice:
            case '1':
                viewStats()
                break
            case '2':
                break
            case '3':
                break
            case '4':
                break
            case _:
                print("\nPlease enter your selection with a single number ('1', '2', etc.)\n")
    
def playGame():
    mainMenu()
    return replay()

def main():
    print('\nWelcome to command-line Connect 4!')
    while True:
        if playGame() == 'n':
            break
    print('\nThanks for playing!\n')

if __name__ == '__main__':
    main()

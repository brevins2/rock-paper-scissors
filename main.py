import random as rand

print('******* Welcome to RPS Game *******\n')

print(f'Instructions to play:\n'
      f'1. Everyone has 3 chances to play\n'
      f'2. Winner has to get at least two wins\n'
      f'3. If you lose two consecutive games, you can ask to fore-fit the third game\n'
      f'4. You chose (R) for Rock, (P) for Paper or (S) for Scissors\n')
chances = 3
start = 1
choices = ['R', 'P', 'S']

randomChoice = choices

rad = rand.randint(1, 3)

while start <= chances:
    choice = input('Play -> Rock, Paper, Scissors: ')
    if choice == 'R' and start < chances:
        if rad == 1:
            print(f'Rock -> Rock\n'
                  f'You draw, rock and rock')
            break
        elif rad == 2:
            print(f'Rock -> Paper\n'
                  f'You lose, Paper covers Rock')
            break
        elif rad == 3:
            print(f'Rock -> Scissors\n'
                  f'You win, Rock crushes Scissors')
            break

    elif choice == 'P' and start < chances:
        if rad == 1:
            print(f'Paper -> Rock\n'
                f'You win, Paper covers Rock')
            break
        elif rad == 2:
            print(f'Paper -> Paper\n'
                  f'You draw, Paper and Paper')
            break
        elif rad == 3:
            print(f'Paper -> Sciccors\n'
                  f'You lose, Sciccors cut Paper')
            break

    elif choice == 'S' and start < chances:
        if rad == 1:
            print(f'Scissors -> Rock\n'
                  f'You lose, Rock crushes Sciccors')
            break
        elif rad == 2:
            print(f'Sciccors -> Paper\n'
                  f'You win, Sciccors cut Paper')
            break
        elif rad == 3:
            print(f'Sciccors -> Sciccors\n'
                  f'You draw, Sciccors and Sciccors')
            break

    else:
        if choice == 'R' and choice == 'P' and choice == 'S' and start > chances:
            print('Out of moves... change players')
            break
        if choice != 'R' and choice != 'p' and choice != 'S' and start <= chances:
            print('Wrong input play, please insert true characters yo play.')
        else:
            print('Check your input and try again')
            start = start + 1
            continue

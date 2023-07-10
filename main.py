print('******* Welcome to RPS Game *******\n')

print(f'Instructions to play:\n'
      f'1. Everyone has 3 chances to play\n'
      f'2. Winner has to get at least two wins\n'
      f'3. If you lose two consecutive games, you can ask to fore-fit the third game\n'
      f'4. You chose (R) for Rock, (P) for Paper or (S) for Scissors\n')
chances = 4
start = 1
choices = ('R', 'P', 'S')

randomChoice = choices

while start < chances:
    choice = input('Play -> Rock, Paper, Scissors: ')
    if choice == 'R' and start < chances:
        print('Rock')
        break
    elif choice == 'P' and start < chances:
        print('Paper')
        break
    elif choice == 'S' and start < chances:
        print('Scissors')
        break
    else:
        if choice != 'R' and choice != 'P' and choice != 'S' and start >= chances:
            print('Out of moves... change players')
            break
        print('Check your input and try again')
        start = start + 1
        continue

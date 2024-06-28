# Write your code here :-)
import random, sys
print('Rock, Paper, Scissors!')
wins = 0
losses = 0
ties = 0

while True: #Start the Game
    print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
    while True: #Player Input
        print('Enter your move (r)ock (p)aper (s)cissors or (q)uit')
        playerMove = input()
        if playerMove == 'q':
            sys.exit() #Quit
        if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
            break
        print('Type one of r, p, s, or q.')

    if playerMove == 'r':
        print('Rock versus...')
    elif playerMove == 'p':
        print('Paper versus...')
    elif playerMove == 's':
        print('Scissors versus...')
    randomNumber = random.randint(1,3)
    if randomNumber == 1:
        computerMove = 'r'
        print('ROCK')
    elif randomNumber == 2:
        computerMove = 'p'
        print('PAPER')
    elif randomNumber == 3:
        computerMove = 's'
        print('SCISSORS')
    #Calculating Ties
    if playerMove == computerMove:
        print('It\'s a tie')
        ties = ties + 1
    #Calculating wins
    elif playerMove == 'r' and computerMove == 's':
        print('You win!')
        wins = wins + 1
    elif playerMove == 'p' and computerMove == 'r':
        print('You win!')
        wins = wins + 1
    elif playerMove == 's' and computerMove == 'p':
        print('You win!')
        wins = wins + 1
    #Calculating Losses
    elif playerMove == 'r' and computerMove == 'p':
        print('You Lose! :-C')
        losses = losses + 1
    elif playerMove == 'p' and computerMove == 's':
        print('You Lose! :-C')
        losses = losses + 1
    elif playerMove == 's' and computerMove == 'r':
        print('You Lose! :-C')
        losses = losses + 1

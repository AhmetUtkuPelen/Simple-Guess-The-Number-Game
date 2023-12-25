import random

def guess(x):
    random_number = random.randint(1,x)
    guess=0
    while guess!=random_number:
        guess=int(input(f'Guess A Number Between 1 and {x}:'))
        if guess<random_number:
            print('Guess Again Your Guess Is Too Low')
        elif guess>random_number:
            print('Guess Again Your Guess Is Too High')
            
    print(f'You Made It Congratz, {random_number} Was The Number')
    
guess(15)
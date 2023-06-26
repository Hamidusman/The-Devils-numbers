# 97% to completion:


import random
from random import randint

name = str(input("Enter your name: "))


num = [0, 1, 2, 3, 4, 5, 6]






human_ans = 0
bot_ans = 0
rounds = int(input('Number of rounds: '))

while True:
    #misses == 0

            print('')
            player = int(input('Choose a number between 1 and 6 (0 to quit) : ')) #ValueError: invalid literal for int() with base 10
            
            if player not in num:
                continue
            if player == 0:
                break
            random_pick = random.randint(0, 5)
            bot = num[random_pick]
            print(f'bot picked {bot}')


            if player == bot:
                print(f'{name}:{player}, Bot: {bot}. Both numbers are equal ({player} to {bot}), lost this round')
                bot_ans += 1

            elif player%bot == 0 and bot != 1:
                print(f'{name}:{player}, Bot: {bot} your number is divisible ({player}/{bot}) , you lost this round')
                bot_ans += 1
                
            elif bot%player == 0 and player != 1:
                print(f'{name}:{player}, Bot: {bot} Bots number is divisible ({bot}/{player}) , you won this round')
                human_ans += 1

            elif player == 5 and bot == 3:
                print(f'{name}:{player}, Bot: {bot}. A cardinal sin against you! lost this round')
                bot_ans += 1
                
            elif player == 3 and bot == 5:
                print(f'{name}:{player}, Bot: {bot}. A cardinal sin in your favour. You won this round')
                human_ans += 1

            elif player == 1 and bot%2 == 0:
                print(f'{name}:{player}, Bot: {bot}. Bot number is even, and since you picked 1, you lose')
                bot_ans += 1

            #  elif player%2 == 0 and bot == 1:
            #     print(f'{name}:{player}, Bot: {bot}. Your number is even, and since the Bot picked 1, you won this round')
            #    human_ans += 1
                
            elif player == 3 and bot == 1:
                print(f'{name}:{player}, Bot: {bot}. You lost this round')
                bot_ans += 1
                
            elif player == 1 and bot == 3:
                print(f'{name}:{player}, Bot: {bot}. You won this round')
                human_ans += 1


            else:
                print(f'{name}:{player}, Bot: {bot} You won this round')
                human_ans += 1
            if human_ans + bot_ans == rounds:
                break


            

print("")
print(f"Best in {rounds} rounds")
print("")

if player == 0:
    print('You forfeited')
else:
    if  human_ans > bot_ans:
        print("You Won!")
    elif bot_ans > human_ans:
        print('You Lost!')
    else:
        print('Its A Draw')

print(f'You: {human_ans}')
print(f'Bot: {bot_ans}')


print("Game Over")
    
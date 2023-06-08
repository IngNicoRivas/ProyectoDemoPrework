import  random

plays = int(input('How many times do you want to play to win?: '))

def choose_options():
    user_option = int(input('Type 1 = Rock🥌, 2 = Paper📃 or 3 = Scissor ✂: '))
    pc_option = random.randrange(1, 3)

    if user_option == 1:
        print("You choice Rock🥌")
    elif user_option == 2:
        print('You choice Paper📃')
    elif user_option ==3:
        print('You choice Scissor ✂')
    else:
        print('choice a correct option')
        return None, None # two none because functions return two args

    if pc_option == 1:
        print("Pc choice Rock🥌")
    elif pc_option == 2:
        print('Pc choice Paper📃')
    else:
        print('Pc choice Scissor ✂')

    return user_option, pc_option

def versus(user_option, pc_option, user_wins, pc_wins):
    if user_option == pc_option:
        print('It is a Tie!')
    elif user_option == 1  and pc_option == 3 or user_option == 2 and pc_option == 1 or user_option == 3 and pc_option == 2:
            print('You win! 😎')
            user_wins += 1
    else: 
        print('pc win!, you lost😌')
        pc_wins += 1
    return user_wins, pc_wins

def result_game(user_wins, pc_wins):
    if pc_wins == plays:
        print(f'Computer win {pc_wins} times it is the winner!😥')
    elif user_wins == plays:
        print(f'You win {user_wins} times and you are the winner!🤩')
    return user_wins, pc_wins


def run_game():
    pc_wins = 0
    user_wins = 0
    rounds = 1
    while True:
        print('================='.center(20))
        print('ROUND'.center(15), rounds)
        print('================='.center(20))
        rounds += 1
        
        print('pc wins: ',pc_wins)
        print('Tu :', user_wins)

        user_option, pc_option = choose_options()
        user_wins, pc_wins = versus(user_option, pc_option, user_wins, pc_wins)
        user_wins, pc_wins = result_game(user_wins, pc_wins)

        if user_wins == plays or pc_wins == plays:
            return

run_game()
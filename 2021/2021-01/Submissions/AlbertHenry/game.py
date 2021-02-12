from random import choice

opts = dict(R = "Rock", P = "Paper", S = "Scissors")

win_against = dict(R = "S", P = "R", S = "P")

def who_win(opt1, opt2):
    if opt1 == opt2:
        result = None
    elif win_against[opt1] == opt2:
        result = opt1
    else:
        result = opt2
    return result

player = False
cpu = choice(list(opts.keys()))

while player == False:
    player = input("[R]ock, [P]aper, [S]cissors?")
    player = str(player).upper()

    if player in opts:
        print(f"You chose {opts[player]}. CPU chose {opts[cpu]}.")
        result = who_win(player, cpu)
        if result is None:
            print("It's a tie. Try again!")
        elif result == player:
            print("You win!")
        else:
            print("You lose...")
    else:
        print("Invalid input. Please retry.")

    player = False
    cpu = choice(list(opts.keys()))

import random


def game_run():
    print("\n*********************************************** ")
    print("* WELCOME TO ROCK PAPER SCISSORS TERMINAL GAME !!* ")
    print("*************************************************\n")
    while True:
        user = input("Throw 'r' for rock  ,'p' for paper, 's' for scissors:\n")
        cpu = random.choice(['r','p','s'])
        if user == cpu:
            print(cpu)
            print("Its a Draw...!!")

        if winnings(user,cpu):
            print("you won !!")
        elif user != cpu:
          return print("You Lost")


def winnings(play,oppenent):
    if (play == "p" and oppenent == 's') or (play == 's'and oppenent == 'p')\
        or (play == 'd' and oppenent == 'r'):
        return True





if __name__ == '__main__':
    game_run()
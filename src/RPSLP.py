import random
from enum import IntEnum
import pandas as pd
import os

class GameAction(IntEnum):

    Rock = 0
    Paper = 1
    Scissors = 2
    Lizard= 3
    Spock= 4


class GameResult(IntEnum):
    Victory = 0
    Defeat = 1
    Tie = 2


Victories = {
    GameAction.Rock: GameAction.Paper,
    GameAction.Paper: GameAction.Scissors,
    GameAction.Scissors: GameAction.Rock,
    GameAction.Lizard: GameAction.Rock,
    GameAction.Spock: GameAction.Paper,
    GameAction.Lizard: GameAction.Scissors,
    GameAction.Paper: GameAction.Lizard,
    GameAction.Spock: GameAction.Lizard,
    GameAction.Rock: GameAction.Spock,
    GameAction.Scissors: GameAction.Spock
}

def assess_game(user_action, computer_action):

    game_result = None

    if user_action == computer_action:
        print(f"User and computer picked {user_action.name}. Draw game!")
        game_result = GameResult.Tie

    # You picked Rock
    elif user_action == GameAction.Rock:
        if computer_action == GameAction.Scissors:
            print("Rock smashes scissors. You won!")
            game_result = GameResult.Victory
        elif computer_action == GameAction.Lizard:
            print("Rock smashes Lizard. You won!")
            game_result = GameResult.Victory
        elif computer_action == GameAction.Spock:
            print("Spock vaporizes the rock. You lost!")
            game_result = GameResult.Defeat
        else:
            print("Paper covers rock. You lost!")
            game_result = GameResult.Defeat
  
    # You picked Paper
    elif user_action == GameAction.Paper:
        if computer_action == GameAction.Rock:
            print("Paper covers rock. You won!")
            game_result = GameResult.Victory
        elif computer_action == GameAction.Spock :
            print("Paper disapproves Spock. You won!")
            game_result = GameResult.Victory
        elif computer_action == GameAction.Lizard:
            print("Lizard eats Paper. You lost!")
            game_result = GameResult.Defeat
        else:
            print("Scissors cut paper. You lost!")
            game_result = GameResult.Defeat

    # You picked Scissors
    elif user_action == GameAction.Scissors:
        if computer_action == GameAction.Rock:
            print("Rock smashes scissors. You lost!")
            game_result = GameResult.Defeat
        elif computer_action == GameAction.Lizard:
            print("Scissors decapitates the lizard. You won!")
            game_result = GameResult.Victory
        elif computer_action == GameAction.Spock:
            print("Spock smashes scissors. You lost!")
            game_result = GameResult.Defeat
        else:
            print("Scissors cuts paper. You won!")
            game_result = GameResult.Victory

    # You picked Lizard
    elif user_action == GameAction.Lizard:
        if computer_action == GameAction.Paper:
            print("Lizard eats paper. You won!")
            game_result = GameResult.Victory
        elif computer_action == GameAction.Spock:
            print("Lizard poisons Spock. You won!")
            game_result = GameResult.Victory
        elif computer_action == GameAction.Scissors:
            print("Scissors decapitates Lizard. You lost!")
            game_result = GameResult.Defeat
        else:
            print("Rock crushes Lizard. You lost!")
            game_result = GameResult.Defeat

    # You picked Spock
    elif user_action == GameAction.Spock:
        if computer_action == GameAction.Rock:
            print("Spock vaporizes rock. You won!")
            game_result = GameResult.Victory
        elif computer_action == GameAction.Scissors:
            print("Spock smashes scissors. You won!")
            game_result = GameResult.Victory
        elif computer_action == GameAction.Lizard:
            print("Lizard poisons Spock. You lost!")
            game_result = GameResult.Defeat
        else:
            print("Paper disapproves Spock. You lost!")
            game_result = GameResult.Defeat

    return game_result


def get_computer_action(dificulty):
    df=pd.read_csv(r"C:\Users\34658\Desktop\Ejercicios\Python\Tarea-MIA-Piedra-Papel-Tijera\doc\Game results RPSLS.csv")
    User_results = df["User"].value_counts()
    
    if dificulty==2:
        try:
            computer_selection= User_results.idxmax()
            computer_action = GameAction(computer_selection)
            print(f"Computer picked {computer_action.name}.")
        except:
            computer_selection = random.randint(0, len(GameAction) - 1)
            computer_action = GameAction(computer_selection)
            print(f"Computer picked {computer_action.name}.")
    elif dificulty==1:
        computer_selection = random.randint(0, len(GameAction) - 1)
        computer_action = GameAction(computer_selection)
        print(f"Computer picked {computer_action.name}.")
    elif dificulty==0:
        try:
            game_result= User_results.idxmax()
            if game_result==0:
                choices=[1,4]
                computer_action = GameAction(random.choice(choices))
            elif game_result==1:
                choices=[2,3]
                computer_action = GameAction(random.choice(choices))
            elif game_result==2:
                choices=[0,4]
                computer_action = GameAction(random.choice(choices))
            elif game_result==3:
                choices=[2,0]
                computer_action = GameAction(random.choice(choices))
            elif game_result==4:
                choices=[1,3]
                computer_action = GameAction(random.choice(choices))
            print(f"Computer picked {computer_action.name}.")
        except:
            computer_selection = random.randint(0, len(GameAction) - 1)
            computer_action = GameAction(computer_selection)
            print(f"Computer picked {computer_action.name}.")
    return computer_action


def get_user_action():
    # Scalable to more options (beyond rock, paper and scissors...)
    game_choices = [f"{game_action.name}[{game_action.value}]" for game_action in GameAction]
    game_choices_str = ", ".join(game_choices)
    user_selection = int(input(f"\nPick a choice ({game_choices_str}): "))
    user_action = GameAction(user_selection)

    return user_action

def save_to_csv(user_inputs):
    results={user_inputs}
    df=pd.DataFrame(results)
    folder_path= r"C:\Users\34658\Desktop\Ejercicios\Python\Tarea-MIA-Piedra-Papel-Tijera\doc\Game results RPSLS.csv"
    df.reset_index(drop=True,inplace=True)
    df.to_csv(folder_path,index=False,mode="a", header=not os.path.exists(folder_path))
    


def play_another_round():
    another_round = input("\nAnother round? (y/n): ")
    return another_round.lower() == 'y'


def main():
    print("Choose Your Dificulty")
    dificulty=int(input("Hard(0), Normal(1), Easy(2):"))
    while True:
        try:
            user_action = get_user_action()
            user_inputs=user_action
        except ValueError:
            range_str = f"[0, {len(GameAction) - 1}]"
            print(f"Invalid selection. Pick a choice in range {range_str}!")
            continue
        computer_action = get_computer_action(dificulty)
        computer_inputs=computer_action
        assess_game(user_action, computer_action)

        save_to_csv(user_inputs)
        if not play_another_round():
            break


if __name__ == "__main__":
    main()

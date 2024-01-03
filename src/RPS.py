import random
from enum import IntEnum
import pandas as pd
import os

class GameAction(IntEnum):

    Rock = 0
    Paper = 1
    Scissors = 2


class GameResult(IntEnum):
    Victory = 0
    Defeat = 1
    Tie = 2


Victories = {
    GameAction.Rock: GameAction.Paper,
    GameAction.Paper: GameAction.Scissors,
    GameAction.Scissors: GameAction.Rock
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
        else:
            print("Paper covers rock. You lost!")
            game_result = GameResult.Defeat

    # You picked Paper
    elif user_action == GameAction.Paper:
        if computer_action == GameAction.Rock:
            print("Paper covers rock. You won!")
            game_result = GameResult.Victory
        else:
            print("Scissors cuts paper. You lost!")
            game_result = GameResult.Defeat

    # You picked Scissors
    elif user_action == GameAction.Scissors:
        if computer_action == GameAction.Rock:
            print("Rock smashes scissors. You lost!")
            game_result = GameResult.Defeat
        else:
            print("Scissors cuts paper. You won!")
            game_result = GameResult.Victory

    return game_result


def get_computer_action(user_inputs,dificulty):
    df=pd.read_csv(r"C:\Users\34658\Desktop\Ejercicios\Python\Tarea-MIA-Piedra-Papel-Tijera\doc\Game results.csv")
    User_results = df["User"].value_counts()
    
    if dificulty==2:
        computer_selection= User_results.idxmax()
        computer_action = GameAction(computer_selection)
        print(f"Computer picked {computer_action.name}.")
    elif dificulty==1:
        computer_selection = random.randint(0, len(GameAction) - 1)
        computer_action = GameAction(computer_selection)
        print(f"Computer picked {computer_action.name}.")
    elif dificulty==0:
        game_result= User_results.idxmax()
        if game_result==0:
            computer_action = GameAction(1)
        elif game_result==1:
            computer_action = GameAction(2)
        elif game_result==2:
            computer_action = GameAction(0)
        print(f"Computer picked {computer_action.name}.")
    return computer_action


def get_user_action():
    # Scalable to more options (beyond rock, paper and scissors...)
    game_choices = [f"{game_action.name}[{game_action.value}]" for game_action in GameAction]
    game_choices_str = ", ".join(game_choices)
    user_selection = int(input(f"\nPick a choice ({game_choices_str}): "))
    user_action = GameAction(user_selection)

    return user_action

def save_to_csv(user_inputs,computer_inputs):
    results={user_inputs}
    df=pd.DataFrame(results)
    folder_path= r"C:\Users\34658\Desktop\Ejercicios\Python\Tarea-MIA-Piedra-Papel-Tijera\doc\Game results.csv"
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
        computer_action = get_computer_action(user_inputs,dificulty)
        computer_inputs=computer_action
        assess_game(user_action, computer_action)

        save_to_csv(user_inputs,computer_inputs)
        if not play_another_round():
            break


if __name__ == "__main__":
    main()

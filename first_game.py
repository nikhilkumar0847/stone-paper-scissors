import random


CHOICES = ["stone", "paper", "scissors"]


def get_computer_choice():
    return random.choice(CHOICES)


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "draw"

    if (
        (user_choice == "stone" and computer_choice == "scissors")
        or
        (user_choice == "paper" and computer_choice == "stone")
        or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        return "user"

    return "computer"


def display_result(user_choice, computer_choice, result):
    print()
    print(f"You chose: {user_choice.capitalize()}")
    print(f"Computer chose: {computer_choice.capitalize()}")
    print()

    if result == "user":
        print("You win!")
    elif result == "computer":
        print("Computer wins!")
    else:
        print("It's a draw!")


def display_score(score):
    print()
    print("--------------------------------")
    print("             SCORE")
    print("--------------------------------")
    print(f"You      : {score['user']}")
    print(f"Computer : {score['computer']}")
    print(f"Draws    : {score['draw']}")
    print("--------------------------------")


def get_user_choice():
    print()
    print("1. Stone")
    print("2. Paper")
    print("3. Scissors")
    print("q. Quit")

    choice = input("Enter your choice: ").strip().lower()

    choice_mapping = {
        "1": "stone",
        "2": "paper",
        "3": "scissors"
    }

    if choice == "q":
        return "quit"

    if choice not in choice_mapping:
        print("Invalid choice. Please select 1, 2, 3, or q.")
        return None

    return choice_mapping[choice]


def main():
    score = {
        "user": 0,
        "computer": 0,
        "draw": 0
    }

    print("================================")
    print("     STONE PAPER SCISSORS")
    print("================================")

    while True:

        user_choice = get_user_choice()

        if user_choice == "quit":
            break

        if user_choice is None:
            continue

        computer_choice = get_computer_choice()

        result = determine_winner(
            user_choice,
            computer_choice
        )

        score[result] += 1

        display_result(
            user_choice,
            computer_choice,
            result
        )

        display_score(score)

    print()
    print("Thanks for playing!")
    print("Final Score:")
    display_score(score)


if __name__ == "__main__":
    main()
import random

# Rock
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

game_images = [rock, paper, scissors]

def decide_choice(player_choice: int, computer_choice: int) -> str:
    if player_choice == computer_choice:
        return "draw"
    elif player_choice == 0 and computer_choice == 2:
        return "win"
    elif computer_choice == 0 and player_choice == 2:
        return "lose"
    elif computer_choice > player_choice:
        return "lose"
    return "win"

def main():
    print('''Welcome to Rock–Paper–Scissors!
            Type 0 for Rock
            Type 1 for Paper
            Type 2 for Scissors
            ''')
    while True:
        try:
            choice = int(input("What's your choice? "))
            if 0 <= choice <= 2:
                break
            else:
                print("Invalid choice. Please enter 0, 1, or 2.")
        except ValueError:
            print("Invalid choice. Please enter 0, 1, or 2.")

    print("You chose: ")
    print(game_images[choice])

    computer_choice = random.randint(0,2)
    print("Computer chose: ")
    print(game_images[computer_choice])

    result = decide_choice(choice, computer_choice)
    if result == "win":
        print("You win!")
    elif result == "lose":
        print("You lose!")
    else:
        print("It's a draw!")


if __name__ == '__main__':
    main()

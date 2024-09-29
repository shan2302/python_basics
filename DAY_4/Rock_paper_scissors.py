import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [rock,paper,scissors]
print("What do you choose? Type 0 for Rock,1 for Paper or 2 for Scissors.")
option = int(input())
if option>=3 or option <0:
    print("You tyoed an invalid number,you lose!")
else:
    print(game_images[option])
    computer_choice = random.randint(0,2)
    print("Computer choice:")
    print(game_images[computer_choice])
    if option == computer_choice:
        print("Draw")
    elif option < computer_choice:
        print("You lose")
    elif option > computer_choice:
        print("You win")
    elif option==0 and computer_choice==2:
        print("You win")
    elif option==2 and computer_choice==0:
        print("You Lose")

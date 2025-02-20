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

player1 = int(input("What do you choose? Type 0 for Rock, type 1 for paper, type 2 for scissors: "))
if player1 >= 0 and player1 <= 2:
 print(game_images[player1])
player2 = random.randint(a=0,b=2)
print(f"Computer chose{player2}")
print(game_images[player2])

if player1 >= 3 or player1 < 0:
    print("You win!")
elif player2 == 0 and player1 == 2:
    print("Computer wins!")
elif player2 > player1:
    print("Computer wins!")
elif player1 > player2:
    print("You win!")
elif player1 == player2:
    print("It is a draw!")
else:
    print("you typed an invalid character. You lose!")

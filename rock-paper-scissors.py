# Go to https://replit.com/@appbrewery/rock-paper-scissors-start?v=1
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

#Write your code below this line 👇
import random
computer = str(random.randint(0, 2))
hand = input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. ')

if hand == '0': print(rock) 
elif hand == '1' : print(paper) 
elif hand == '2': print(scissors)
# print(f'Computer chose: {computer}')
print(f'Computer chose: ')
if computer == '0': print(rock) 
elif computer == '1' : print(paper) 
elif computer == '2': print(scissors)

if hand == computer: print('Draw')
elif int(computer) == int(hand) + 1 or hand == '2' and computer == '0': print('You lose')
else : print('You won')

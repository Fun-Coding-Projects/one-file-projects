# Import the random module here

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

# Example list ...
Angela, Ben, Jenny, Michael, Chloe

#Write your code below this line 👇
import random

print(names[random.randint(0, len(names))])
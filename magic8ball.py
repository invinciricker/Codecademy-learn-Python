#magic8ball.py

import random
#Greetings
name = "User"
name = str(input("Hi there, What's your name? "))

#Question
question = str(input(f"Hi {name} What would you like to ask today? "))
print (f"{name} asks: {question}")

# Answer
random_number = random.randint(1, 9)
if random_number == 1:
    answer = "Yes, definitely."
elif random_number == 2:
    answer = "It is decidedly so."
elif random_number == 3:
    answer = "Without a doubt."
elif random_number == 4:
    answer = "Reply hazy, try again."
elif random_number == 5:
    answer = "Ask again later."
elif random_number == 6:
    answer = "Better not tell you now."
elif random_number == 7:   
    answer = "My sources say no."
elif random_number == 8:
    answer = "Outlook not so good."
elif random_number == 9:
    answer = "Very doubtful."
else: answer = "Error: Invalid response."
# Output
print(f"{name}, the Magic 8-Ball says: {answer}")
# End of magic8ball.py


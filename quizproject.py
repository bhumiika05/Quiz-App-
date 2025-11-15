print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
  quit()

print("Okay! Let's play :)")
score = 0

answer = input("What is the capital of India? ")
if answer == "New Delhi":
 print('Correct!')
 score += 1
else:
  print("Incorrect!")

answer = input("Which planet is known as Red Planet?")
if answer == "Mars":
 print('Correct!')
 score += 1
else:
 print("Incorrect!")

answer = input("How many days are there in a leap year? ")
if answer == "366":
 print('Correct!')
 score += 1
else:
 print("Incorrect!")

answer = input("Which is the largest ocean on Earth?")
if answer == "Pacific Ocean":
  print('Correct!')
  score += 1
else:
 print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4) * 100) + "%.")
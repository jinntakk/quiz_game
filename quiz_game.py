print("Welcome to QUIZ GAME!")

play = input("Would you like to play? Y/N: ").upper()
score = 0


if play != "Y":
    print("Have a great day!")
    quit()

print("Let's Play!")

answer = int(input("What is 2 + 2? "))
if answer == 4:
    score += 1
    print("Correct!")
else:
    print("That is not the correct answer.")

answer = int(input("What is 2 + 3? "))
if answer == 5:
    score += 1
    print("Correct!")
else:
    print("That is not the correct answer.")

answer = int(input("What is 2 + 5? "))
if answer == 7:
    score += 1
    print("Correct!")
else:
    print("That is not the correct answer.")

print(f"You got {score} questions correct!")
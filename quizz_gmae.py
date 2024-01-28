print("Welcome to my computer")

playing = input("Do you want to play? ").lower()

# .lower() is to make valid user's input even if they are in upper case

if playing != "yes":
    quit()

# != stands for 'other than'

print("Okey! Let's play :)")
score = 0

answer = input("What does CPU stand for? ").lower()
if answer == "central processing unit":
    print("Correct!")
    score +=1

# score +=1 is equal to score = score+1
     
else:
    print("Wrong answer")

answer = input("What does RAM stand for? ").lower()
if answer == "random acess memory":
    print("Correct!")
    score +=1
else:
    print("Wrong answer")

answer = input("What does PSU stand for? ").lower()
if answer == "power supply unit":
    print("Correct!")
    score +=1
else:
    print("Wrong answer")

answer = input("What does ROM stand for? ").lower()
if answer == "read only memory":
    print("Correct!")
    score +=1
else:
    print("Wrong answer")

answer = input("Who made this code? ").lower()
if answer == "prabhakar":
    print("Correct!")
    score +=1
else:
    print("Wrong answer")

print("You got " + str(score) + " questions correct!")
print("Or you got " + str((score/4)*100) + "%.")

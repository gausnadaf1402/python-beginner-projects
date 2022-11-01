print('welcome to my computer quiz!')

playing=input("do you want to play? ")

if playing.lower() !="yes":
    quit()

print("okay! Lets play:)")
score=0


answer=input("what does ML stnds for? ")
if answer.lower()=="machine learning":
    print("correct!")
    score=score+1
else:
    print("incorrect")

answer=input("what does AI stnds for? ")
if answer.lower()=="artificial intelligence":
    print("correct!")
    score=score+1
else:
    print("incorrect")

answer=input("what is the full form of GUI? ")
if answer.lower()=="graphical user interface":
    print("correct!")
    score=score+1
else:
    print("incorrect")

answer=input("what is the state of pune? ")
if answer.lower()=="maharashtra":
    print("correct!")
    score=score+1
else:
    print("incorrect")

answer=input("where are you from? ")
if answer.lower()=="pune":
    print("correct!")
    score=score+1
else:
    print("incorrect")

print("you got " + str(score) + " questions correct!")
print("you got " + str((score/4)*100) + "%.")
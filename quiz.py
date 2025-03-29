print("Welcome to Quiz-O-maina")
playing=input("Do you want to play? ")

if playing.lower() !="yes":
    quit()

print("Okay!,Lets play the game")

score=0
print("You will get 1 point for each correct answer")

answer=input("What is the capital of India? ")
if answer.upper()=="DELHI":
    print ("Correct :)")
    score+=1
else:
    print('Incorrect!!')
print("**************************************************************************************************************")

answer1=input("Which animal is the king of the jungle? ")
if answer1.upper()=="LION":
    print ("Correct :)")
    score+=1
else:
    print('Incorrect!!')

print("**************************************************************************************************************")

answer2=input("What is the name of the big river in India where people pray? ")
if answer2.upper()=="GANGA":
    print ("Correct :)")
    score+=1
else:
    print('Incorrect!!')

print("**************************************************************************************************************")

answer3=input("Which animal is special in India and has a long trunk? ")
if answer3.upper()=="ELEPHANT":
    print ("Correct :)")
    score+=1
else:
    print('Incorrect!!')

print("**************************************************************************************************************")

answer4=input("Which is the national bird of India? ")
if answer4.upper()=="PEACOCK":
    print ("Correct :)")
    score+=1
else:
    print('Incorrect!!')

print("**************************************************************************************************************")

answer5=input("What festival in India is called the Festival of Colors where people throw colorful powders? ")
if answer5.upper()=="HOLI":
    print ("Correct :)")
    score+=1
else:
    print('Incorrect!!')

print("**************************************************************************************************************")

print("You have completed the quiz!")
print("You got "+ str(score) +" question corrects:) ")
print("You got "+ str((score / 6) * 100) + " % ")

print("**************************************************************************************************************")

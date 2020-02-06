print("Well come to the KenKen game V1!")
username = input("Please enter your username: ")

print()
print('----------------------------------------')
print('---------------Puzzle 1-----------------')
print('----------------------------------------')
print()
print("Hello " + username + "! Try solving this puzzle 1*2 with rule  <\" 3+ \">")

answer = input("Enter your answer 1: ")  # "1"
num1 = int(answer)
answer = input("Enter your answer 2: ")
num2 = int(answer)
if(num1+num2 == 3):
    print("Yeah!You win!")
else:
    print("Wrong answer :(")

print()
print('----------------------------------------')
print('---------------Puzzle 2-----------------')
print('----------------------------------------')
print()

correctAnswer = False
print("Now lets try solving the second puzzle 1*2 with rule  <\" 1- \">")
while(correctAnswer == False):
    answer = input("Enter your answer 1: ")  # "1"
    num1 = int(answer)
    answer = input("Enter your answer 2: ")
    num2 = int(answer)
    if(abs(num1-num2) == 1):
        print("Yeah!You win!")
        correctAnswer = True
    else:
        print("Wrong answer :( Please try again!")

print()
print('----------------------------------------')
print('---------------Puzzle 3-----------------')
print('----------------------------------------')
print()

import random as r

num = r.randint(0, 3)

rulePool = ["1-", "3+", "2*", "2/"]
rule = rulePool[num]
operater = rule[1]
expectedAnswer = int(rule[0])

print("Now lets try solving the second puzzle 1*2 with rule  <\" " + rule + " \">")

correctAnswer = False
while(correctAnswer == False):
    answer = input("Enter your answer seperated by space: ")
    num1 = int(answer[0])
    num2 = int(answer[-1])
    if(operater == '+'):
        correctAnswer = num1+num2 == expectedAnswer
    elif(operater == '-'):
        correctAnswer = abs(num1-num2) == expectedAnswer
    elif(operater == '*'):
        correctAnswer = num1*num2 == expectedAnswer
    elif(operater == '/'):
        if(num1/num2 == expectedAnswer or num2/num1 == expectedAnswer):
            correctAnswer = True
    if(correctAnswer):
        print("Yeah!You win!")
    else:
        print("Wrong answer :( Press try again!")

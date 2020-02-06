import KenKenGameV2UI as ui

# ui.loadEntryMessage()
# ui.loadLevelUI(45787458)

def playLevel(level):
    # call UI function to display UI
    ui.loadLevelUI(level)

    rule = levelPool[level]
    operater = rule[1]
    expectedAnswer = int(rule[0])
    answerCorrect = False

    print("Try solving this puzzle 1*2 with rule  \"" + rule+"\"")

    while(answerCorrect == False):

        answer = input("Enter your answer seperated by space: ")
        num1 = int(answer[0])
        num2 = int(answer[-1])

        if(operater == '+'):
            answerCorrect = num1+num2 == expectedAnswer
        elif(operater == '-'):
            answerCorrect = abs(num1-num2) == expectedAnswer
        elif(operater == '*'):
            answerCorrect = num1*num2 == expectedAnswer
        elif(operater == '/'):
            if(num1/num2 == expectedAnswer or num2/num1 == expectedAnswer):
                answerCorrect = True
        else:
            print("unsupported type of operater")

        if(answerCorrect):
            print("Yeah!You win!")
        else:
            input("Wrong answer :( Press Enter to retry!")

username = ui.loadEntryMessage()
levelPool = [None,"1-", "3+", "2*", "2/"]
for level in range(1,5):
    playLevel(level)



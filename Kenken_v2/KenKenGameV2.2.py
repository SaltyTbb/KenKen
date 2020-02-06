import KenKenGameV2UI as ui

def validateAnswer(answer, rule):
    # answer: list of string of user input|| rule: string of rule
    operater = rule[-1]
    expectedAnswer = int(rule[:-1])
    if(operater == '+'):
        total = 0
        for num in answer:
            total += int(num)
        return total == expectedAnswer

        """
        the for-loop can be replaced by
        return sum(list(map(lambda x: int(x), answer))) == expectedAnswer
        """

    elif(operater == '-'):
        num1 = int(answer[0])
        num2 = int(answer[1])
        return abs(num1-num2) == expectedAnswer

    elif(operater == '*'):
        total = 1
        for num in answer:
            total *= int(num)
        return total == expectedAnswer

    elif(operater == '/'):
        num1 = int(answer[0])
        num2 = int(answer[1])
        if(num1/num2 == expectedAnswer or num2/num1 == expectedAnswer):
            return True
        return False  # using else does the same thing here
    return False # this line should never be reached


def playLevel(level):
    # call UI function to display UI
    ui.loadLevelUI(level)

    rule = levelPool[level]

    print("Try solving this puzzle with rule  \"" + rule+"\"")

    answerCorrect = False
    while(answerCorrect == False):

        # type(answer):string
        answer = input("Enter your answer seperated by space: ")
        # type(answer):list of str
        answer = answer.split(' ')

        answerCorrect = validateAnswer(answer, rule)

        if(answerCorrect):
            print("Yeah!You win!")
        else:
            input("Wrong answer :( Press Enter to retry!")

username = ui.loadEntryMessage()
levelPool = [None,"2-", "16+", "24*", "4/"]
for level in range(1,5):
    playLevel(level)

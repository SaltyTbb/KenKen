import KenKenGameV2UI as ui
from KenKenGameV2Validator import Validator

def playLevel(level):
    # call UI function to display UI
    ui.loadLevelUI(level)
    validator=Validator()
    rule = levelPool[level]

    print("Try solving this puzzle with rule  \"" + rule+"\"")

    answerCorrect = False
    while(answerCorrect == False):

        # type(answer):string
        answer = input("Enter your answer seperated by space: ")
        # type(answer):list of str
        answer = answer.split(' ')

        answerCorrect = validator.validateAnswer(answer, rule)

        if(answerCorrect):
            print("Yeah!You win!")
        else:
            input("Wrong answer :( Press Enter to retry!")

username = ui.loadEntryMessage()
levelPool = [None,"2-", "16+", "24*", "4/"]
for level in range(1,5):
    playLevel(level)

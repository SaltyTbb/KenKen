def loadEntryMessage():
    print("Welcome to the KenKen game V2!")
    username = input("Please enter your username: ")
    print("Hello " + username + "!Hope you have fun and enjoy Kenken!")
    return username


def loadLevelUI(level):
    print()
    print('----------------------------------------')
    print('---------------Puzzle '+str(level) + '-----------------')
    print('----------------------------------------')
    print()

#loadEntryMessage()
#loadLevelUI(45787458)
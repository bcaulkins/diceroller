import random

dice = ['d4','d6','d8','d10','d12','d20',"d100"]

diceDict = {
    "d4":4,
    "d6":6,
    "d8":8,
    "d10":10,
    "d12":12,
    "d20":20,
    "d100":100
}

#syntax will be like /r 1d6k +4
print("Let's Roll")

while True:
    syntax_list = []
    section_loc = []
    player_roll=input()

#places each part of the command into a list. used to help parse user input
    for i in player_roll.split(' '):
        syntax_list.append(i)
    
#indexes the lengths of the different sections of the commands. used to parse user input.
    for i in syntax_list:
        section_loc.append(len(syntax_list[syntax_list.index(i)]))
    

    pos1 = syntax_list[0]
    if pos1 == 'q':
        break
    elif IndexError ==True:
        print("Error. Please try again.")
    elif pos1=='/r':
        dpos = int(player_roll.rfind('d'))
        spacepos = player_roll.rfind(' ')
        rollstring = ""
        endofstring = 0
        numofdicetoroll = 0
        typeofdicetoroll = 0
        try:
            rollstring = str(syntax_list[1])
        except IndexError:
            print("There was an error, please try again.")
        else:
            rollstring = str(syntax_list[1])
        dpos1= int(rollstring.rfind('d'))

        try:
            endofstring = int(section_loc[1])
        except IndexError:
            print("There was an error, please try again.")
        else:
            endofstring = int(section_loc[1])

        try:
            numofdicetoroll = int(rollstring[0:dpos1])
        except ValueError:
            print("There was an error, please try again.")
        else:
            numofdicetoroll = int(rollstring[0:dpos1])

        try:
            typeofdicetoroll = int(rollstring[dpos1+1:endofstring])
        except ValueError:
            print("There was an error, please try again.")
        else:
            typeofdicetoroll = int(rollstring[dpos1+1:endofstring])
        

        rolls = numofdicetoroll
        results = []
        while rolls != 0:
            results.append(random.randint(1,typeofdicetoroll))
            rolls = rolls-1
        print(*results)
        print(player_roll)
    elif pos1 !='/r':
        print("Please enter a valid command.")
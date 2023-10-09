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
print("type --help or --h for a list of commands.")

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
    elif pos1 == 'c' or pos1 == 'commands' or pos1 == '--help' or pos1 == '--h':
        #Prints commands to use.
        print("Here are some helpful commands on how to use DiceRoller.")
        print("/R, /ROLL      - Every roll needs to start with either /R or /ROLL.")
        print("A              - Adding an 'A' to the end of the dice and roll will roll with Advantage, meaning it will roll 2 dice of the type you specify and take the higest of those 2 dice.")
        print("D              - Adding a 'D' to the end of the dice and roll will roll with Disadvantage, meaning it will roll 2 dice of the type you specified and take the lowest of those 2 dice.")
        print("KH, KH(number) - Adding KH(number) to the end of the dice roll command will keep the higest (number) of dice. Example: /r 6d6kh(5) will keep the 5 higest rolls. The default is 1.")
        print("KL, KL(number) - Adding KL(number) to the end of the dice roll command will keep the lowest (number) of dice. Example: /r 6d6kh(5) will keep the 5 lowest rolls. The default is 1.")
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
#clean up error handling - should only print error once.
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
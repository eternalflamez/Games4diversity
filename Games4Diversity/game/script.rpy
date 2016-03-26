﻿# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
define m = Character('Me', color="#c8ffc8")
define n = Character('Nicholas')

# The game starts here.
label start:
    $ day = 1
    $ health = 100;
    $ happiness = 100;
    $ piety = 100;
    $ love = 100;

    m "Welcome to ...ENTER_GAMENAME_HERE..."

    jump pickReligion


label pickReligion:
    
    $ religion = renpy.input("What is the name of your religion?")
    $ religion = religion.strip()

    if not religion:
        jump pickReligion

    "And so [religion] was created."
    
    jump pickTitle

label pickTitle:
    $ playertitle = renpy.input("What is your title in this religion?")
    $ playertitle = playertitle.strip()

    if not playertitle:
        jump pickTitle

    jump pickName

label pickName:
    $ playername = renpy.input("What is your name?")
    $ playername = playername.strip();
    $ playertitlename = playertitle + " " + playername

    if not playername:
        jump pickName

    # $ renpy.show_screen("confirm", message="For the religion [religion] you are [playertitlename]?", yes_action=Jump("dayStart"), no_action=Jump("pickReligion"))

    menu:
        "Are you [playertitlename] from [religion]?"
        "Yes":
            jump dayStart

        "No":
            jump pickReligion
    

label dayStart:
    
    n 'Today is day [day].'

    $ day += 1
    $ date = "day" + str(day)
    jump expression date
# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
define m = Character('Me', color="#c8ffc8")
define n = Character('Nicholas')

# The game starts here.
label start:
    $ day = 0

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

    jump dayStart


label dayStart:

    n 'Today is day [day].'

    $ day += 1
    $ date = "day" + str(day)
    jump expression date

    return


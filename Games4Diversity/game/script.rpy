# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

image bg normal = "ui/background_01.png"
image monk = "ui/monk2.png"
image booth = "ui/booth.png"

# Declare characters used by this game.
define m = Character('Me', color="#c8ffc8")

# Define images to be used with dilemmas
image cradle = "ui/circles/cradle.png"
image heart = "ui/circles/heart.png"
image scales = "ui/circles/scales.png"

# The game starts here.
label start:
    scene bg normal
    show monk

    $ day = 0
    $ health = 100;
    $ happiness = 100;
    $ piety = 100;
    $ love = 100;

    m "Welcome to Confession."

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

    call screen dilemma(("Yes", "No"), None, "Are you [playertitlename] from [religion]?")

    if _return == 0:
        "You are [playertitlename], one of the founders of [religion]."
        "You have been tasked with helping to grow a small community that has adopted religion happily"
        "The choices you make will shape the founding tenements of [religion] and how the community develops."
        $ m = Character(playertitlename, color="#c8ffc8")
        hide monk
        jump dayStart 

    if _return == 1:
        jump pickReligion

label dayStart:
    show booth with fade
    # todo: fadeout and in
    $ day += 1
    $ date = "day" + str(day)

    'Today is day [day].'
    hide booth with dissolve
    jump expression date
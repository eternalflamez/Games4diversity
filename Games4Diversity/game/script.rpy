# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
define m = Character('Me', color="#c8ffc8")
define n = Character('Nicholas', color="#FFFFFF")

# The game starts here.
label start:
    $ day = 0

    m "[day]You've created a new Ren'Py game."

    m "Once you add a story, pictures, and music, you can release it to the world!"

    jump pickReligion

label pickReligion:
    $ religionname = renpy.input("What is the name of your religion?")
    $ religionname = religionname.strip()

    if not religionname:
        jump pickReligion

    "And so [religionname] was created."
    
    jump dayStart

label dayStart:

    n 'Today is day [day].'

    $ day += 1
    jump dayStart

    return


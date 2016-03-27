label day5:
    "You had a calm day, nothing serious was going on, until John approached you. He looked confused, as if struggling with a complex issue."
    "Person" "\"Dear [playertitlename] I have returned for I need guidance.\""
    "Person" "\"My AI needs to know what it is allowed to do if it needs to avoid a high speed frontal collision.\""    

    call screen dilemma(("Take one life to save the many", "You cannot interfere", "Pray it will never occur", "Randomize the outcome"), scales, "Person" "\"Is it allowed to make the choice to drive the car into a ravine to save a group of people from an unavoidable crash?\"", "Person")

    if _return == 0:
        m "Let the AI take one life to save many."
        $ day5resp = 1;
        jump dayStart
    elif _return == 1:
        m "You cannot interfere with the fate of others."
        $ day5resp = 2;
        jump dayStart
    elif _return == 2:
        m "Pray that this situation will never occur."
        $ day5resp = 3;
        jump dayStart
    elif _return == 3:
        m "Randomize the outcome, we can never make such a choice."
        $ day5resp = 4;
        jump dayStart

label day2:
    
    "Person" "Dear [playertitle] I am visiting you for I need guidance."
    "Person" "I work as an artificial intelligence programmer, and I need to know what to do."
    "Person" "I am working on a self-driving car, however I do not know if I can give an AI the autonomy to make a choice about human safety. "

    call screen dilemma(("Allow", "Do not allow"), "Does an AI have the right to crash a car to potentially avoid a larger accident from happening?", "Person")

    if _return == 0:
        m "Allow such a choice to be made by an AI."
        $ day2response = 1
        jump dayStart
    if _return == 1:
        m "An AI is never allowed to make such a choice."
        $ day2response = 2
        jump dayStart
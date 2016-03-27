label day10:

    show scales

    "Your day has been hectic, news of a car crash has shocked the community. Many people have come to talk to you in their grief. "

    "A man enters the confession booth. You recognise his trembling voice:"

    "John" "\"Dear [playertitlename] I have returned for I fear that I have sinned.\""
    "John" "\"My AI has killed people in the crash.\""
    "John" "\"It was an unavoidable situation and the car had to divert its course.\"" 

    call screen dilemma(("Bear the burden", "The driver is responsible", "The AI is responsible"), "\"Am… am I responsible for these deaths...?\"", "John")

    if _return == 0:
        m "You must bear this burden with you."
        jump endgame
    elif _return == 1:
        m "The driver is responsible for their car."
        $ day7resp = 2;
        jump endgame
    elif _return == 2:
        m "The AI is responsible, you are not to be blamed."
        $ day7resp = 3;
        jump endgame
label day1:
    
    "As you're working in your house of [religion], a woman comes up to you."
    "woman" "[playertitle], I need your help."
    "It's Laura, she and her husband work a nearby farm."

    jump day1question

label day1question:
    m "Hey Laura, what can I help you with today?"
    "laura" "I feel like my husband is cheating on me."
    "laura" "He doesn't pay much attention to me anymore these days, he just seems so absent. I've had this feeling for months now and I just don't know what to do."
    
    $ day1options = ("Kind Response", "Harsh Response", "Sarcasm", "Flirt")

    call screen dilemma(day1options)

    if _return == 0:
        jump day1kind
    elif _return == 1:
        jump day1harsh
    elif _return == 2:
        jump day1sarcasm
    elif _return == 4:
        jump day1flirt

label day1kind:
    m "Just have faith in your husband, my child."
    $ responsetype = 1
    $ love += 1;
    $ happiness -= 1;
    jump dayStart

label day1harsh:
    m "Confront your husband, tell him what you're thinking. It could just be that there's something else going on."
    $ responsetype = 2
    jump dayStart

label day1sarcasm:
    m "*laughs*"
    m "Good luck with that."
    $ responsetype = 3
    jump dayStart

label day1flirt:
    m "So do you want to get back at him?"
    $ responsetype = 4
    jump dayStart
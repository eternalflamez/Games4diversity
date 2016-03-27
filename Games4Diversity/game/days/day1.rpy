define laura = Character('Laura')

label day1:

    show heart
    
    "It is a Spring morning, and you are familiarising yourself with the layout of the church, when a woman enters through the doors. She is clutching her arms to herself and looks slightly sad. She approaches you."
    "She introduces herself as Laura, a secretary for a nearby business. After introducing yourself as a new [playertitle] of [religion], she nervously begins to talk."
    laura "\"I…this is kind of hard to talk about… but I really don’t know who else to ask… you see, I feel a bit… out of touch with my husband…\""
    laura "\"I’m not sure how to describe it really, he feels distant all the time… we’ve never had a problem talking to each other except…\""
    laura "\"Is…is he cheating on me do you think?\""
    laura "\"Oh gods that’s a horrible thing to say, he can’t be…I mean, I don’t… I don’t know what to do…\""

    jump day1question

label day1question:

    $ day1options = ("Trust in your husband",
                     "Rekindle your love",
                     "Hire a private investigator",
                     "Encourage him to confess")

    call screen dilemma(day1options)

    if _return == 0:
        jump day1option1
    elif _return == 1:
        jump day1option2
    elif _return == 2:
        jump day1option3
    elif _return == 3:
        jump day1option4

label day1option1:
    m "\"Trust in your husband, a marriage has struggles and hardships which you will trial through.\""
    $ day1response = 1
    jump day1end

label day1option2:
    m "\"Rekindle your love together by some form of romantic gesture.\""
    $ day1response = 2
    jump day1end

label day1option3:
    m "\"Hire a private investigator to watch your husband.\""
    $ day1response = 3
    jump day1end

label day1option4:
    m "\"Encourage him to attend confession.\""
    $ day1response = 4
    jump day1end

label day1end:
    laura "\"You…you really think so?\""
    laura "\"Alright… I… I’ll do that… Thank you [playertitlename]…\""
    "She slowly leaves, staring at the floor, holding herself steady."
    hide heart
    jump dayStart

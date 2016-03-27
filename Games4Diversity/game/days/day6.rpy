define unknownMan = Character("Man's Voice")
label day6:
    show heart
    if day1response == 1 or day1response == 2:
        hide cradle
        hide heart
        hide scales
        show monk
        "It is a quiet day today."

        jump dayStart

    elif day1response == 3:
        if day3resp3 == 1:
            "You see Laura enter the church. She stops upon passing the threshold, allowing the doors to close behind her. She is staring at the ground, both her hands loosely holding her elbows."
            laura "\"I… I had to… didn’t I? He’d broken our promise…\""
            "You console her as she weeps softly."

            jump dayStart

        elif day3resp3 == 2:
            "You are on confessional duty today. It is a slow day, and only a single person comes to confess today. A man's voice starts to pass through the dividing lattice."
            unknownMan "\"Forgive me [playertitle], for I have sinned.\""
            unknownMan "\"I have been tempted and have cheated on my wife. I think she might know, but I can’t be sure. I… I feel so guilty\""

            call screen dilemma(("Tell your wife, ask for forgiveness", "Pray for forgiveness", "It is not a sin in the eyes of [religion]"), "\"What should I do?\"", "Man's Voice")

            if _return == 0:
                m "Tell your wife, ask for forgiveness."
                jump day6resp2resp1
            elif _return == 1:
                m "Pray for forgiveness from God."
                jump day6resp2resp2
            elif _return == 2:
                m "It is not a sin in the eyes of [religion]."
                jump day6resp2resp3

        elif day3resp3 == 3:
            "You see Laura enter the church. She stops upon passing the threshold, allowing the doors to close behind her. She is staring at the ground, both her hands loosely holding her elbows."
            "You begin to approach her when she clenches her fists and shoots her head up towards you with gritted teeth, rage in her eyes."
            laura "\"How could you try and make do such a thing!? What kind of church is this, where you make people cheat on people they love?!\""
            "She is panting heavily, her chest rising up and down, tiny arms shaking at her sides, but she stays in place."
            laura "\"Did you make my husband cheat on me?! Did you give him that same sick advice?!\""
            "Tears are beginning to well up in her eyes."
            laura "\"I can’t believe I came here in the first place! I renounce this bloody faith, you… you… animals!\""
            "Her voice begins to crack. With a great sob she spins and storms out the double doors."

            jump dayStart

        elif day3resp3 == 4:
            "You are on confessional duty today. It is a slow day, and only a single person comes to confess today. A man's voice starts to pass through the dividing lattice."
            unknownMan "\"Forgive me [playertitle], for I have sinned.\""
            unknownMan "\"I have been tempted and have cheated on my wife. She discovered me. I can’t believe I hurt her so much…\""

            call screen dilemma(("Tell your wife, ask for forgiveness", "Pray for forgiveness", "It is not a sin in the eyes of [religion]"), "\"What should I do?\"", "Man's Voice" )

            if _return == 0:
                m "Tell your wife, ask for forgiveness."
                jump day6resp4resp1
            elif _return == 1:
                m "Pray for forgiveness from God."
                jump day6resp4resp2
            elif _return == 2:
                m "It is not a sin in the eyes of [religion]."
                jump day6resp4resp3

    elif day1response == 4:
        hide cradle
        hide heart
        hide scales
        show monk
        "It is a quiet day today."

        jump dayStart

label day6resp2resp1:
    unknownMan "I… Maybe you’re right… she’s the one I should be apologising to… I don’t want to hide this from her…"
    unknownMan "But she’ll be so hurt I just know it… God why did I do this?"

    "The man leaves the confessional booth"

    "~Later that day~"

    "Laura and her husband arrive in the church, clinging onto each other’s arms. They approach you slowly. The husband’s head is hanging slightly."
    laura "\"Hello [playertitlename], we… we wanted to come here to thank you…\""
    laura "\"We’ve been through a hard few days but… I think… we can get past it… a relationship has to be worked for after all…\""
    laura "\"Once again… thank you for helping us…\""

    jump dayStart

label day6resp2resp2:
    unknownMan "\"Alright… I… If that’s enough… I can’t stand seeing her get hurt… I’ll promise to be a better husband for her.\""
    "The man leaves the confessional booth."
    "Throughout the rest of the day you see him burying his head in his hands in prayer."

    jump dayStart

label day6resp2resp3:
    unknownMan "\"I... But… I… Well… If I don’t tell her… I guess she won’t be hurt…\""
    "The man leaves the confessional booth."

    jump dayStart


label day6resp4resp1:
    unknownMan "\"I… Maybe you’re right… she’s the one I should be apologising to… I shouldn’t have hidden this from her…\""
    unknownMan "\"She’s hurt, I need to go back… God why did I do this?\""

    "The man leaves the confessional booth"

    "~Later that day~"

    "Laura and her husband arrive in the church, clinging onto each other’s arms. They approach you slowly. The husband’s head is hanging slightly."
    laura "\"Hello [playertitlename], we… we wanted to come here to thank you…\""
    laura "\"We’ve been through a hard few days but… I think… we can get past it… a relationship has to be worked for after all…\""
    laura "\"Once again… thank you for helping us…\""

    jump dayStart

label day6resp4resp2:
    unknownMan "\"Alright… I… If that’s enough… I can’t stand seeing her get hurt… I’ll promise to be a better husband for her.\""
    "The man leaves the confessional booth."
    "Throughout the rest of the day you see him burying his head in his hands in prayer."

    jump dayStart

label day6resp4resp3:
    unknownMan "\"I… But… I… She… She won’t accept that…\""
    "The man leaves the confessional booth."

    jump dayStart

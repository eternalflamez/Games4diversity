label day3:
    if day1response == 1 or day1response == 2:
        "You are tending to your duties in the church when Laura enters through the doors and appreaches you, a soft smile on her lips."
        laura "\"Hello again, thank you for your guidance [playertitlename]. I think it's worked out. Releationships have to be worked at, don't they? I'm sure we'll continue to find happiness. This has just been the first real time we've drifted apart... I suppose it's to be expected as we get older, he?\""
        
        jump dayStart

    elif day1response == 3:
        "You are tending to your duties in the church when Laura bursts through the doors, tears streaming down her face."
        laura "\"I... [playername]... he's cheating on me... he was with another woman... *sob* I don't... *sob*\""
        "She sniffles."
        
        call screen dilemma(("Divorce him", "Tell him to confess", "Eye for an eye", "Do nothing"), heart, "\"Please I don't know what to do! I threw away so much for him! I don't... please...\"", "Laura")

        if _return == 0:
            m "Divorce him. Cut him entirely out of your life."
            $ day3resp3 = 1;
            jump day3resp3end
        elif _return == 1:
            m "Tell him to attend confession."
            $ day3resp3 = 2;
            jump day3resp3end
        elif _return == 2:
            m "Eye for an eye. Cheat on him."
            $ day3resp3 = 3;
            jump day3resp3end
        elif _return == 3:
            m "Do nothing. He can do what he wants."
            $ day3resp3 = 4;
            jump day3resp3end

    elif day1response == 4:
        "You are on confessional duty today. It is a slow day, and only a single person comes to confess today."
        "A man's voice starts to pass through the dividing lattice:"
        "Man" "\"Forgive me [playertitle], for I have sinned.\""
        
        call screen dilemma(("Ask wife for forgiveness", "Pray for forgiveness", "This is no sin to me"), "\"I have been tempted and have cheated on my wife. I think she might know, but I can't be for sure. I... I feel so guilty...\"", "Laura")

        if _return == 0:
            m "Tell your wife, ask for her forgiveness."
            jump day3resp41end
        elif _return == 1:
            m "Pray for forgiveness from God."
            jump day3resp42end
        elif _return == 2:
            m "It is not a sin in the eyes of [religion]."
            jump day3resp43end


label day3resp3end:
    "Laura is still in tears as you tell her what she should do. She initially rejects what you say but gradually you convince her that it is in her best interests to follow your advice."
    "She leaves the cloister sullenly"
    jump dayStart

label day3resp41end:
    "Man" "\"I... Maybe you're right... she's the one I should be apologising to... I don't want to hide this from her...\""
    "Man" "\"But she'll be so hurt I just know it... God why did I do this?\""
    "The man leaves the confession booth."

    "Later that day..."
    "Laura and her husband arrive in the church, clinging onto each other's arms. They approach you slowly. The husband's head is hanging slightly."
    laura "\"Hello [playertitlename], we… we wanted to come here to thank you…\""
    laura "\"We've been through a hard few days but… I think… we can get past it… a relationship has to be worked at after all…\""
    laura "\"Once again… thank you for helping us…\""

    jump dayStart

label day3resp42end:
    "Man" "\"Alright... I... If that's enough... I can't stand seeing her get hurt... I'll promise to be a better husband for her.\""
    "The man leaves the confession booth."
    "Throughout the rest of the day you see him burying his head in his hands in prayer."
    
    jump dayStart

label day3resp43end:
    "Man" "I... But… I… Well… If I don't tell her… I guess she won't be hurt… but…"
    "The man leaves the confessional booth."

    jump dayStart
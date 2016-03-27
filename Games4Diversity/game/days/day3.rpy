label day3:
    if day1response == 1 or day1response == 2:
        "You are tending to your duties in the church when Laura enters through the doors and appreaches you, a soft smile on her lips."
        "Laura" "Hello again, thank you for your guidance [playertitlename]. I think it's worked out. Releationships have to be worked at, don't they? I'm sure we'll continue to find happiness. This has just been the first real time we've drifted apart... I suppose it's to be expected as we get older, he?"
        # TODO: Fadeout
    elif day1response == 3:
        "You are tending to your duties in the church when Laura bursts through the doors, tears streaming down her face."
        "Laura" "I... [playername]... he's cheating on me... he was with another woman... *sob* I don't... *sob*"
        "She sniffles."
        "Laura" "Please I don't know what to do! I threw away so much for him! I don't... please..."
        
        menu:
            "Divorce him":
                m "Divorce him. Cut him entirely out of your life."
                jump day3resp3end
            "Tell him to confess":
                m "Tell him to attend confession."
                jump day3resp3end
            "Eye for an eye":
                m "Eye for an eye. Cheat on him."
                jump day3resp3end
            "Do nothing":
                m "Do nothing. He can do what he wants."
                jump day3resp3end

    elif day1response == 4:
        "asd"


label day3resp3end:
    "Laura is still in tears as you tell her what she should do. She initially rejects what you say but gradually you convince her that it is in her best interests to follow your advice."
    "She leaves the cloister sullenly"
    jump dayStart
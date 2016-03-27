label day8:
    show cradle

    if day4response == 1:
        hide cradle
        hide heart
        hide scales
        show monk
        "It is a quiet day today."
        jump dayStart

    elif day7resp > 1:
        "You receive a letter. The handwriting seems to have been hurried."
        "Hurried letter" "\"Dear [playertitlename], I am writing to you again as the situation has changed.\""
        "Hurried letter" "\"My wife is still pregnant with our baby, who will be disabled and unable to ever walk. It might even turn out worse than that.\""
        "Hurried letter" "\"And the deadline to abort is approaching in a week, after which we will have no choice left but to have the child.\""

        call screen dilemma(("Convince your wife to abort", "Do not abort", "Discuss this with your wife"), "\"What should I do? I'm not sure if I can keep my job. I really don't know what should be done. Yours in haste, Gary Sinclair\"", "Hurried letter")

        if _return == 0:
            m "Convince your wife to abort."
            $ day8resp = 1;
            jump dayStart
        elif _return == 1:
            m "Do not abort, keep the baby."
            $ day8resp = 2;
            jump dayStart
        elif _return == 2:
            m "Talk with your husband, and then decide."
            $ day8resp = 3;
            jump dayStart

    elif day7resp == 1:
        "News is carried to you from the local hospital. The abortion was performed."
        jump dayStart

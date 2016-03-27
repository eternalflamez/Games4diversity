label day7:
    show cradle
    if day4response == 1:
        "News is carried to you from the local hospital. The abortion was performed."
        jump dayStart

    "A small woman enters the church. She seems to be showing the early signs of pregnancy. "
    "She spies you across the chapel and approaches you. "
    "Unidentified woman" "\"Hello there, might you be [playertitlename]? You're the new [playertitle] here, right?\""
    "Unidentified woman" "\"My name is Hannah Sinclair. \""
    "Hannah Sinclair" "\"I was wondering if you could help me with something... As you probably noticed, I'm pregnant and I want to keep the child... we just found out that it's a girl, someting I've always wanted, but my husband does not think we can support it. \""
    "Hannah Sinclair" "\"To make matters worse, after a recent doctor visit it turns out the child will be born disabled with Spina Bifida, and may never be able to walk. \""
    "Hannah Sinclair" "\"What should I do? Does the church have any views on abortion?\""

    call screen dilemma(("Abort it", "Keep the baby", "Talk with your husband", "Do nothing"), "\"Please I don't know what to do! I threw away so much for him! I don't... please...\"", "Laura")

    if _return == 0:
        m "Keep the child from misery, abort it."
        $ day7resp = 1;
        jump dayStart
    elif _return == 1:
        m "Do not abort, keep the baby."
        $ day7resp = 2;
        jump dayStart
    elif _return == 2:
        m "Talk with your husband, and then decide."
        $ day7resp = 3;
        jump dayStart

define letter = Character('Mysterious letter')

label day4:

    letter "\"You receive a letter addressed to you. \""
    letter "\"Dear [playertitlename], I am writing to you for guidance on a delicate situation.\""
    letter "\"My wife is pregnant with another child. We already have three children and we do not have the funds to support another mouth to feed.\""
    letter "\"I want her to have an abortion but she wants to keep it. What should I do?\""
    letter "\"Yours sincerely, Gary Sinclair.\""

    jump day4question

label day4question:

    $ day4options = ("Convince her to abort",
                     "Don't abort, keep the child",
                     "Discuss this with your wife")
    call screen dilemma(day4options, "\"Tell me [playertitle], What should I do?\"", "Letter from Gary Sinclair")

    if _return == 0:
        jump day4option1
    elif _return == 1:
        jump day4option2
    elif _return == 2:
        jump day4option3

label day4option1:
    m "\"If you cannot support the child, you should convince your wife to abort the child.\""
    $ day4response = 1
    jump day4end

label day4option2:
    m "\"You should not abort this child. Keep the child instead and raise them well.\""
    $ day4response = 2
    jump day4end

label day4option3:
    m "\"Discuss these thoughts with your wife, so that you are certain in your decision.\""
    $ day4response = 3
    jump day4end

label day4end:
    "You pen your response and send it to the address provided."
    jump dayStart

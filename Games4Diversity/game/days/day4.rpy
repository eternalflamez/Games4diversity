define john = Character('John')

label day4:

    john "\"Dear [playertitle], I am visiting you for I need guidance.\""
    john "\"My wife is pregnant with another child.\""
    john "\"We already have three children and we do not have the funds to support another mouth to feed.\""
    john "\"I want her to have an abortion but she wants to keep it.\""
    john "\"Tell me [playertitle], what should I do?\""

    jump day4question

label day4question:

    $ day4options = ("Convince her to abort",
                     "Don't abort, keep the child",
                     "Discuss this with your wife")
    call screen dilemma(day4options)

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
    john "\"Thank you for your guidance [playertitlename]\""
    jump dayStart

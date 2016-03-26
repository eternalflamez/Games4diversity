define woman = Character("Woman")
define laura = Character("Laura")

label day1:
    
    "As you're working in your house of [religion], a woman comes up to you."
    woman "[playertitle], I need your help."
    "It's Laura, she and her husband work a nearby farm."

    jump day1question

label day1question:
    m "Hey Laura, what can I help you with today?"
    laura "I feel like my husband is cheating on me."
    laura "He doesn't pay much attention to me anymore these days, he just seems so absent. I've had this feeling for months now and I just don't know what to do."

    menu: 
        "kind response":
            jump day1kind

        "harsh response":
            jump day1harsh

        "sarcasm":
            jump day1sarcasm

        "flirt":
            jump day1flirt

        "Repeat the question":
            jump day1question

label day1kind:
    m "Just have faith in your husband, my child."
    jump dayStart

label day1harsh:
    m "Confront your husband, tell him what you're thinking. It could just be that there's something else going on."
    jump dayStart

label day1sarcasm:
    m "*laughs*"
    m "Good luck with that."
    jump dayStart

label day1flirt:
    m "So do you want to get back at him?"
    jump dayStart
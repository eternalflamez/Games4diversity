label day9:
    show cradle

    if day4response == 1:
        "It is a quiet day today."

    elif day7resp == 2 or day7resp == 3:
        "News is carried to you by local gossip. The baby has been kept."

    elif day8resp == 1:
        "News is carried to you from the local hospital. The abortion was performed."

    elif day8resp > 1:
        "It is a quiet day today."

    jump dayStart

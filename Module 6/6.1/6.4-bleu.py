def substitue(message, abreviation):
    """Substitue the abreviation with the full word"""
    # Split the message into words
    message = message.split()
    # Loop through the words in the message
    for i in range(len(message)):
        # If the word matches the abreviation
        if message[i] in abreviation:
            # Replace the word with the full word
            message[i] = abreviation[message[i]]
    # Join the words back into a message and return it
    return " ".join(message)
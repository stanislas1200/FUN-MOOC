def construction_dict_amis(couples):
    """Build a dictionary of friends from a list of couples"""
    # Initialize the dictionary
    amis = {}
    # Loop through the list of couples
    for couple in couples:
        # Add the friend to the dictionary with his friends
        amis[couple[0]] = amis.get(couple[0], set('')).union({couple[1]})
        if (couple[1] not in amis):
            # Add the friend to the dictionary with an empty set
            amis[couple[1]] = set('')
    # Return the dictionary
    return amis
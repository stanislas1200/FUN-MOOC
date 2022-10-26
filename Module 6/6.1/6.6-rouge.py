def symetrise_amis(d, englobe):
    """Symetrize the dictionary of friends"""
    # Loop through the dictionary
    for ami in d:
        # Loop through the friends of the friend
        for ami_ami in d[ami]:
            # If the friend is not in the friends of the friend
            if ami not in d[ami_ami]:
                if englobe:
                    # Add the friend
                    d[ami_ami].add(ami)
                else:
                    # Remove the friend
                    d[ami].remove(ami_ami)
                    break

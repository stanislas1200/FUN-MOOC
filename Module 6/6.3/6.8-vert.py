def store_email(liste_mails):
    """Returne a dictionary with the domaine and the user"""
    # Create a dictionary
    dico = {}
    # Loop on the list
    for email in liste_mails:
        # We split the email in two parts
        nom, domaine = email.split('@')
        # We add the domaine and the user in the dictionary
        if domaine in dico:
            dico[domaine].append(nom)
        else:
            dico[domaine] = [nom]
    # We return the dictionary
    return {domaine: sorted(dico[domaine]) for domaine in dico}
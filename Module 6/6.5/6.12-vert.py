def belongs_to_file(word, filename):
    """Returns True if word is in filename, False otherwise."""
    with open(filename, 'r') as file:
        for line in file:
            if word == line.replace("\n", ''):
                return True
    return False
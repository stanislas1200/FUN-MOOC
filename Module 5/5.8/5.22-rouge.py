import string

def wc(file):
    """Retourne un tuple qui contient le nombre de mots, de caractères et de lignes du fichier"""
    nbr_word = 0
    nbr_char = 0
    nbr_line = 0
    lst = []
    with open(file, encoding="utf-8") as f:
        for line in f:
            nbr_line += 1
            for i in range(len(line)):
                if not line[i].isalnum() and line[i] not in lst:
                    lst += line[i]
                if line[i].isalnum:
                    nbr_char += 1
                if not line[i].isalnum() and line[i-1].isalnum():
                    nbr_word += 1
    print(lst)
    return (nbr_char, nbr_word, nbr_line)

print(wc('Apollinaire2.txt'))
## Line good, but not word and char
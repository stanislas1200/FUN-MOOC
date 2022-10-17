def acrostiche(file):
    ret = ''
    with open(file, encoding="utf-8") as f:
        for line in f:
            ret += line[0]
        return ret

print(acrostiche('Apollinaire.txt'))
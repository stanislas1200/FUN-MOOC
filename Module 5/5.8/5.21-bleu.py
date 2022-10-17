def liste_des_mots(file):
    """Retourne une liste de tous les mots du fichier"""
    ret = []
    with open(file, encoding="utf-8") as f:
        for line in f:
            for i in range(len(" -\"'?!:;.,*=()1234567890")):
                line = line.replace(" -\"'?!:;.,*=()1234567890"[i], ' ')
            for word in line.split():
                word = word.lower()
                if word not in ret:
                    ret.append(word)
    ret.sort()
    return ret

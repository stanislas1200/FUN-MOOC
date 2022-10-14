def transcription_clavier(texte):
    """Fonction qui permet de corriger un texte"""
    str = ""
    for i in texte:
        if i == '%':
            i = 'M'
        str += i
    return str
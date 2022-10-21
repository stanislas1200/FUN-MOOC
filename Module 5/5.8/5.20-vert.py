def nouveaux_heros(file, dest):
    with open(file, encoding="utf-8") as f:
        with open(dest, 'w', encoding="utf-8") as f2:
            for line in f:
                line = line.replace(',', ' ')
                line = line.replace('Paul', 'Tom')
                line = line.replace('Pierre', 'Paul')
                line = line.replace('Jacqueline', 'Mathilde')
                line = line.replace('  ', ', ')
                f2.write(line)

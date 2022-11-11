def ft_read_file(filename):
    """Reads a file and returns the content as a dict"""
    with open(filename, "r") as file:
        lines = file.readlines()
        # Stock in var
        dict = {}
        for i in range(0, len(lines[1:]) + 1):
            lines[i] = lines[i].replace("\n", '').split(";")
            dict[i] = lines[i]
    return dict


rpf = input()  # rpf.csv
rc = input()  # rc.csv

# read csv files and save in dict
f1 = ft_read_file(rpf)
f2 = ft_read_file(rc)

# dict ex names
dex = {}
for ex in f1[0]:
    dex[ex] = 0

# Increment dex if count less than 10
nfia = []
for i in range(1, len(f1)):
    for j in range(len(f2[i])):
        if f2[i][j] and int(f2[i][j]) > 10:
            nfia.append(i)
for i in range(1, len(f1)):
    if i not in nfia:
        for j in range(len(f1[i])):
            if f1[i][j] == "VRAI":
                dex[f1[0][j]] += 1

dex = {val[0]: val[1] for val in sorted(dex.items(), key=lambda x: (x[1], x[0]))}
while len(dex) > 0:
    print(dex.popitem()[0])

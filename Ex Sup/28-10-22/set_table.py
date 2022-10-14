table = [(0, 't1'), (3, 't4'), (1, 't2'), (4, 't6'), (2, 't5')]

def regen(src):
    if len(table) < len(src):
        for i in range(len(src) - len(table)):
            table.append(None)
    for i in range(len(table)):
        table[i] = src[i]
    return

def set_table(arr, id, no_de_telephone):
    if id >= len(arr):
        table_2 = []
        for i in range(len(table)+5):
            table_2.append(None)
        arr.append((id, no_de_telephone))
        for i in range(len(arr)):1<
            set_table(table_2, arr[i][0], arr[i][1])
        print(table_2)
        regen(table_2)
        return None
    taille = len(arr)
    position = id * 97 % taille
    if (arr[position] is None) or (arr[position][0] == id):
        arr[position] = (id, no_de_telephone)
    else:
        pass#set_table(table, id + 1, no_de_telephone)
    regen(arr)
    return None

set_table([(0, 't1'), (3, 't4'), (1, 't2'), (4, 't6'), (2, 't5')], 5, 't7')
print("fini : " + table.__str__())


def get_table(table, id):
    taille = len(table)
    position = id * 97 % taille
    return table[position]

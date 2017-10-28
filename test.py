def combo(incoming1, incoming2):
    list_of_tuples = []
    a = 0
    while a < len(incoming1):
        temp = incoming1[a], incoming2[a]
        list_of_tuples.append(temp)
        a += 1
    return list_of_tuples


combo([1, 2, 3], 'abc')

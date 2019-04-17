#my_list = [1, 2, 3, [4, 5, [6, 7]]]
my_list = input('Введите список')
my_list = eval(my_list)

def superfunc228(spis,bol):
    if bol == 0:
        for i in range(len(spis)):
            if type(spis[i]) == list:
                spis[i] = superfunc228(spis[i],1)
        print(spis)
        return spis
    else:
        for i in range(len(spis)):
            if type(spis[i]) == list:
                spis[i] = superfunc228(spis[i], 1)
        return sum(spis)

superfunc228(my_list,0)
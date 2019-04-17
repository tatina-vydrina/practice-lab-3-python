first_list = input('Введите список')
first_list = eval(first_list)

def prod_list(alist):
    i = 0
    out_list = []
    while i < len(alist):
        out_list.append(list_prod(alist))
        alist.pop(0)
    return out_list


def list_prod(blist):
    i = 0
    tmp = 1
    while i < len(blist):
        tmp *= blist[i]
        i += 1
    return tmp


#first_list = [1, 2, 3, 4, 5, 6]

print(prod_list(first_list))

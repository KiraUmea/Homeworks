list_it = (2, 4, 6, 7, 1)

def sum(list_it):
    sum_l = 0
    for i in list_it:
        while i != len(list_it):
            sum_l = sum_l + i
    print(sum_l)

sum(list_it)

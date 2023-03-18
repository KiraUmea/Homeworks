def spam(number):
    return "bulochka" * number


def my_sum(list_of_numbers):
    nsum = 0
    for i in numbers:
        nsum += i
    return nsum


def shortener(string):
   x = string.split()
   st_new = []
   for i in x:
       if len(i) > 6:
        st_new.append(i[:6] + "*")
       else:
        st_new.append(i)
   string = ' '.join(st_new)
   return string


def compare_ends(words):
    y = 0
    for i in words:
    if len(i) >= 2 and i[0] == i[-1]:
        y += 1
    return y


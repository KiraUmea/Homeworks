floors = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
entrance = 1
fl_on_fl = 5
flats = 5 * (len(floors))
list(flats)

for i in flats():
    n = i % 5 == 0


#flats_on_fl = {floors[i]: flats(5 items)}

def find_numd(num):
    numb_flats = 4
    avgfloors = 4

    H_search = num // (numb_flats * avgfloors)
    F_search = (num - (numb_flats*avgfloors)*(H_search)) // avgfloors

    return f" під'їзд: {H_search + 1}, поверх: {F_search + 1}, квартира: {num}"

search = 12

print(find_numd(search))
___________
f = int(input('ввести номер квартиры'))
v = int(input('ввести номер подьезда'))
b = int(input('ввести номер этажей'))
n = int(input('ввести кол-во квартир на этаже'))

A = b * n #количество квартир в подьезде
B = f // A
D = (B +1) #в каком подьезде квартира
E = f % A
G = E // n
J = (G + 1) #узнаем на каком этаже
print(str(D) + 'подьезд')
print(str(J) + 'этаж')

file = open('strings of numbers.txt', 'r')


def fizz_buzz(f: int, b: int, l: int):
    numb = ''
    for i in range(1, l + 1):
        if i % f == 0 and i % b == 0:
           numb +=  'FB' + ' '
        elif i % F == 0:
           numb +=  'F' + ' '
        elif i % B == 0:
            numb +=  'B' + ' '
        else:
            numb += str(i) + ' '
    return numb


file2 = open('strings of numbers2.txt', 'w')


f = int(f)
b = int(b)
i = int(i)
l = int(l)
for i in f:
    f, b, l = i.split(" ")
print(f,b,l)


file2.write(fizz_buzz(int(f), int(b), int(l)))
file2.write("\n")

file.close()
file2.close()
print(fizz_buzz(f, b, l))

# f2 = open('strings2 of numbers.txt', 'w')

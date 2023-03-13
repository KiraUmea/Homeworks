import math
x = int(input())


def square(x):
    d = x*x
    print(d)


square(x)


is_simple = any(not x%i for i in range(2, round(x**0.5)+1))

print("число просте") if is_simple is False else print("число не просте")


list_of_simple = list(filter(is_simple, range(51)))
print(list_of_simple)
print(list(map(square, list_of_simple)))



for i in range(1,19):
    if ((i % 2 == 0) and (i % 5 == 0)) in range(1,19):
        print("F" + "B")
    elif i % 2 == 0:
        print("F")
    elif i % 5 == 0:
        print("B")
    else:
        print(i)

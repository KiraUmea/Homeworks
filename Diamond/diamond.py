n=int(input("enter the no of rows :"))
k = n//2
for i in range(k+1):
    if i == 0:
        print(" "*(k-i), '*', sep='', end='\n')
    else:
        j = list(range(1,n-1,2))[i-1]
        print(" "*(k-i), '*', "*"*j, '*', sep='', end='\n')
for i in range(k-1,-1,-1):
    if i > 0:
        j = list(range(n-k+(n-9)//2,-1,-2))[k-i-1]
        print(" "*(k-i), '*', "*"*j, '*', sep='', end='\n')
    else:
        print(" "*(k-i), '*', sep='', end='\n')

n = numb -2
w = n*2-1
ar  = [ ]

for y in range(w):
   ar.append([])
   for x in range(w):
       d = n - abs(x+1-n) - abs(y+1-n)
       ar[y].append( "*" if d > 0 else " ")

for l in ar:
    print(*l,sep='')

from random import randint 
l = [randint(10,80) for x in range(10)]
print (l)
for el in range(0,len(l)):
    if el % 2 == 1:
        print(l[el])


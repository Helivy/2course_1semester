l = 'xxhhhhhhhhhhhhhhhhxxxxxhhx'
a = l[:l.find('h') + 1] 
b = l[l.find('h') + 1:l.rfind('h')]
c = l[l.rfind('h'):]
l = a + b.replace('h', 'H') + c
print(l)

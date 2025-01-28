list=[12,23,75,14,7,3,734]
a=list[0]
for i in range(0,len(list)):
    if list[i]<a:
        a=list[i]
print(a)
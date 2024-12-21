a=int(input("choose a number"))
sum=0 
for i in range (a):
    if i % 2 == 0:
        sum = i + sum
    

print(sum)


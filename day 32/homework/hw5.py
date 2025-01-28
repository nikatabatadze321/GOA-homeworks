#5) გააკეთეთ Sum Of Even Numbers. მიზანი: შეკრიბეთ ყველა ლუწი რიცხვი და შეინახეთ სიაში შემდეგ ეგ სია დაპრინტეთ 10 ჯერ
list=[]

for i in range (0,100,2):
    list.append(i)
sum=0

for i in range(0,len(list)):
    sum= sum + int(list[i])
print (sum)
#3) გააკეთეთ Filter Even Numbers. მიზანი: გაფილტრეთ ყველრა ლუწი რიცხვი და ჩაამატეთ ახალ სიაში და შემდეგ ეგ სია დაპრინტეთ 

import random
list=[]
for i in range(0,10):
    a=random.randint(0,100)
    list.append(a)

print(list)
for i in range (0,10):
    if list[i] %2==0:
        list.remove(list[i])
# print(list)
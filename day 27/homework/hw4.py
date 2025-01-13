import random
num = list(range(1, 31))
a=random.randint(0,30)
print(a)
user_num = int(input("enter number: "))
while user_num != num[a]:
    print("incorrect!!!")
    user_num = int(input("enter number: "))
    
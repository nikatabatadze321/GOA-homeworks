#7) დაიწყეთ რიცხვების სიით, გამოიყენეთ while loop რომ წაშალოთ ყველა რიცხვი ამ სიიდან და გამოიყენეთ pop რო
#  დაპრინტოთ ეს ყველა ელემენტი სანამ ლისტი არ დაცარიელდება 
list=[11,2,3,41,17,6]

i=-3
while i < len(list):
    a=int(input("choose wich number to pop 0-5"))
    new_list=[list.pop(a)]
    print(list)
    i=i+1
    print(i)
        






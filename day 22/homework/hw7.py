#     4) მომხმარებელს შემოატანინეთ რიცხვი შემდეგ კი ერთიდან ამ რიცხვამდე დაბეჭდეთ ყველა რიცხვის ორზე ნამრავლების ჯამი
a = int(input("number?:"))
sum = 0

for i in range (a):
    sum = sum + (i*2)
    
    print(sum)
#     2) მომხმარებელს შემოატანინეთ რიცხვი შემდეგ კი ერთიდან ამ რიცხვამდე დაბეჭდეთ რიცხვების საშუალო არითმეტიკული
a = int(input("number?:"))
sum = 0
for i in range (a):
    sum = sum + i
    print(sum/(a-1))

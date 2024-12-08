#2)  მომხმარბელს შემოატანინეთ რიცხვი შემდეგ კი მომხმარებლის შემოტანილ რიცხვამდე დაბეჭდეთ რიცხვები და გვერძე მიუწერეთ ლუწია თუ კენტი
a=int(input("choose a number"))
for i in range (a):
    if i % 2 ==0:
        print(str(i)+" "+"even")
    else:
        print(str(i)+" "+"odd")
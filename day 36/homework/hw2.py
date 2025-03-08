#10) შექმენით ფუნქცია რომელიც მომხმარებელს შეეკითხება რიცხვს შემდეგ კი ერთიდან იმ რიცხვამდე დაბეჭდავს
#  ყველა რიცხვს
def numbers ():
    a = int(input("choose a number"))
    for i in range (0,a):
        print(i+1)
numbers()

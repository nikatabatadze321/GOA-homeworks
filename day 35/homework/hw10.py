#11) შექმენით ფუნქცია რომელიც მომხმარებელს შეეკითხება რიცხვს შემდეგ კი ერთიდან იმ რიცხვამდე დაბეჭდავს ყველა ლუწ რიცხვს
def nums ( ):
    a=int(input("choose a numm : "))
    for i in range (0,a,2):
        print(i+2)
nums()
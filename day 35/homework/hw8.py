# 8) შექმენით ფუნქცია რომელიც მომხმარებელს შეეკითხება რიღხვს შემდეგ კი დაბეჭდავს დადებითია თუ უარყოფითი
def wich ():
    a=int(input("number ?"))
    if a > 0 :
        print("positive")
    elif a < 0 :
        print("negative")
    else:
        print("none")
wich ()
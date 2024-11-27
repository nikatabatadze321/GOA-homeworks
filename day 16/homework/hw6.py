#თქვენ დაგპატიჟეს პატარა ბავშვის დაბადების დღეზე გასართობ ცენტრში, 
# თქვენთან ერთად ამ გასართობ ცენტრში დაპატიჟეს 10 ადამიანი და ამ 10 ადამიანიდან ერთ ერთი ნიკოლოზია. 
# ნიკოლოზს უთხრეს რომ მას შეუძლია ბავშებთან ერთად გაერთოს თუ ის ფეხსაცმელებს გაიხდის და ქურთუკს საკიდზე ჩამოკიდებს (True და False-ს გამოყენება დაგჭირდებათ). 
# თქვენი მიზანია გაარკვიოთ ნიკოლოზმა შეასრულა ეს წესები თუ არა, ანუ შეუძლია თუ არა მას ბავშებთან ერთად გართობა.

nika=input("did you take off your shoes")
while nika not in ["yes", "no"]:
    print("please answer with yes or no ")
    nika=input("did you take off your shoes")   
while nika in ["no"] :
    nika=print("you did not follow the rules thus you cant have fun with others")
    
    
while nika in ["yes"] :
        a=input("did you hang your coat")
        while a not in ["yes","no"]:
                print("please answer with yes or no ")
                a=input("did you hang your coat")
        while a in ["no"]:
                a=print("you did not follow the rules thus you cant have fun with others")
        
        while a in ["yes"]:
         a=print ("congrats now you can have fun with kids")

        

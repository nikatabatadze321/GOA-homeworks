# შექმენით shopping სია სადაც მომხმარებელს შეეძლება რამე ნებისმიერი პროუქტის დამატება და წაშლა, 
# როდესაც მორჩებიან შოპინგს დაუპრინტეთ საბოლოოდ რა შეიძინეს 
shop = ["phone","laptop","TV",]

a=(input("remove whichever product you want by naming it:  "))
while a not in shop:
    a=(input("please type product that is in the list: "))
shop.remove(a)
print(shop)
remove_more=input("do you want to remove more product ? yes/no: ")
while remove_more == "yes":
    b=input("name the product you want to remove: ")
    shop.remove(b)
    print("congrats you have bought" +str(shop))
    break

while remove_more == "no":
    c=input("which product do you want to add: ")
    shop.append(c)
    print("congrats you have bought"+str(shop))
#5) შექმენით ლისტი სადაც გექნებათ 1-10 ჩათვლით რიცხვები, შეამოწმეთ რიცხვი ლუწია თუ კენტი და თუ კენტია დაამატეთ ახალ ლისტში 
my_list=[1,2,3,4,5,6,7,8,9,10]
new_list=[]
for i in range (len(my_list)):
    if my_list[i] % 2 !=0:
        new_list.append(my_list[i])
print(new_list)

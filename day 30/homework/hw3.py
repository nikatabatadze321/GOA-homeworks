#3) შექმენით ლისტი სადაც გექნებათ 1-10 ჩათვლით რიცხვები,
#  დაპრინტეთ ყველა რიცხვი მაგრამ მიუწერეთ რომელია კენტი და რომელია ლუწი
my_list=[ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]
for i in range (len(my_list)):
    if my_list[i] % 2 ==0:
        print (str(my_list[i]) + "odd")
    else:
        print(str(my_list[i])+"even")
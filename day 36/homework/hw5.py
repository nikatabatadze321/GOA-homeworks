#13) შექმენით ფუნქცია რომელშიც იქნება რიცხვებით სავსე სია შემდეგ კი დაბეჭდავს ამ სიაში არსებული
#  რიცხვების ჯამს
def num():
    my_list=[1,11,23,17,22]
    sum = 0 
    for i in range (len(my_list)):
        sum=sum+my_list[i]
        print(sum)
num()

#13) შექმენით ფუნქცია რომელშიც იქნება რიცხვებით სავსე სია შემდეგ კი დაბეჭდავს ამ სიაში არსებული რიცხვების ჯამს
def summation ():
    my_list=[28,17,19,22,34]
    sum=0
    for i in range (len(my_list)):
        sum = my_list[i] + sum
        print(sum)
summation()
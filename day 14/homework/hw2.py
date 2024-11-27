#გამოიყენეთ or ოპერატორი,
#  რათა შეამოწმოთ, თუ მოცემული ციფრები არიან 10-ზე ნაკლები ან 50-ზე მეტი.
a= int(input("number:"))

if a<10 or a>50:
    print("your number is either lower than 10 or higher than 50")
else:
    print("your number is between 10(including 10) and 50(including 50)")
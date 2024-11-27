#შეამოწმეთ, თუ ერთ-ერთი ციფრი უფრო დიდია 10-ზე ან მეორე ციფრი ნაკლებია 50-ზე.

a = int(input("num1:"))

b = int(input("num2:"))

if a>10 or b<50:
    print("either num1 is greater than 10 or num2 is less than 50, maybe both")
else:
    print("num1 is less than 10 and num2 is greater than 50")
#1) თუ ასაკი არის 18 ის 
# ზემოთ ან 50 წლის ქვემოთ  ან თუ  ასაკი  ნაკლებია 18 ზე და მეტია 50 ზე გამოტანეთ
#  ის უნდა იყოს ან მოხუცი ან ახალგაზრდა
a= int(input("your age:"))

if a<18:
    print("sorry your underaged")
if a>=18 and a<50:
    print("your middle aged")
if a>=50:
    print("your old")
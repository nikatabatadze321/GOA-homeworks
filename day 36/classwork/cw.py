 #1) შექმენით ფუნქცია რომელსაც ექნება ორი პარამეტრი ხოლო ამ ფუნქციამ უნდა 
 # გადაამრავლოს ეს ორი რიცხვი ერთმანეთზე შემდეგ კი დაიბეჭდოს მიღებული ნარმავლი ლუწია თუ კენტი
 #  ნამრავლთან ერთად, გამოიძახეთ ეს ფუნქცია რამდენჯერმე და გადაეცით არგუმენტები(სვადასვა რიცხვები)
def multiply (num1,num2):
    a = num1 * num2
    if a % 2 == 0:
        print(str(a)+"odd")
    else:
        print(str(a)+"even")
multiply(9,11)

#1) შექმენით ფუნქცია რომელსაც ექნება ორი პარამეტრი ხოლო ამ ფუნქციამ უნდა გადაამრავლოს ეს ორი რიცხვი ერთმანეთზე შემდეგ კი დაიბეჭდოს
#  მიღებული ნარმავლი ლუწია თუ კენტი ნამრავლთან ერთად, გამოიძახეთ ეს ფუნქცია რამდენჯერმე და გადაეცით არგუმენტები(სვადასვა რიცხვები)
def multiply (a,b):
    if (a * b) % 2 ==0:
        print( str(a*b)+"odd")
    else:
        print (str(a*b)+"even")
    
num1=int(input("num :"))
num2=int(input("num :"))
multiply(num1,num2)
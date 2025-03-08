def calculator (text):
    a = int(input("choose first number : "))
    b = int(input("choose second number : "))
    first_num = a * text
    second_num = b * text 
    sum = a * text + b * text
    print("addition:") 
    print(first_num + " "+"+")
    print(second_num + " "+ "=")
    print(sum)
    print("==================================================================")
    minus= a - b 
    next = minus * text
    first = a * text
    second = b * text 
    print("deduction:")
    print(first + " "+ "-")
    print(second + " "+ "=")
    print(next) 
    print("==================================================================")  
    multiply = a * b
    so1= a * text
    so2=b * text 
    end=multiply * text
    print("multiplication :")
    print(so1 + " " +"*")
    print(so2 + " " + "=")
    print(end)
    print("==================================================================")
    int_division= a // b
    firstly = a * text
    secondly = b * text
    at_end = int_division * text
    print("division :")
    print(firstly + " "+ "/")
    print(secondly + " "+ "=")
    print(at_end)
    print("==================================================================")


calculator(".")
# 1)a = 5
#   b = "10"
#   result = a + b
#   print("Result:", result)

#   კოდი გამოიტანს ერორს დაწერეთ რატომ და ასევე ცალკე დაწერეთ სწორი ფორმა

# problem is in 3rd line because variables a and b cant be added,pyton doesnt define( int + str )


a = 5
b = "10"
result = a + int(b)
print("Result:", result)
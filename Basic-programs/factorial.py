# to print factorial of given no

a = int(input("Enter the number: "))

fact = 1

for i in range (1 , a+1):
    fact *= i
    
print(fact)


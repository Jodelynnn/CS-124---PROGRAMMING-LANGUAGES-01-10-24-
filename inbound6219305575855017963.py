print ("Choose an Operator")
print ("1. Multiplication")
print ("2. Division")
print ("3. Addition")
print ("4. Subraction")

op = input()

if op == "1":
    num1 = input ("Enter first num:")
    num2= input ("Enter second num:")
    print ("The product is " + str(int(num1) * int(num2)))
    
elif op == "2":
    num1 = input ("Enter first num:")
    num2= input ("Enter second num:")
    print ("The quotient is " + str(int(num1) / int(num2)))
    
elif op == "3":
    num1 = input ("Enter first num:")
    num2= input ("Enter second num:")
    print ("The sum is " + str(int(num1) + int(num2)))
    
elif op == "4":
    num1 = input ("Enter first num:")
    num2= input ("Enter second num:")
    print ("The difference is " + str(int(num1) - int(num2)))
   
else:
     print("Invalid Input")   

print("select an operation: ")
print( "1. add(+)")
print( "2. subtract(-)")
print( "3. multiply(*)")
print( "4. Division(/)")

#operator = input("Enter the operator (+, -, *, /): ")

choice = input("Enter your choice (1,2,3,4): ")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
if choice == "1":
    results = num1 + num2
    print(results)
elif choice == "2":
    results = num1 - num2
    print(results)
elif choice == "3":
    results = num1 * num2
    print(results)
elif choice == "4":
    if num2 == 0:
       print("cannot divide by zero")
    else:
        results = num1 / num2
        print(results)

else:
    print("Please enter a valid choice")








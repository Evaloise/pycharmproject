#Largest among 3 numbers
a = float(input("Enter a number: "))
b = float(input("Enter another number: "))
c = float(input("Enter third number: "))

#method 1
if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else :
    largest = c
    print("The largest number is ", largest)
    print(largest)


    #method 2
    #largest = max (a,b,c)
   # print(f"The largest number is ": {largest})

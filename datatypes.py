#whole numbers are called integers
age = 67
#float - decimal values
height = 1.75
#string - in terms of text written in double quotes
greeting = "Hello"
#boolean written in capitals true or false or yes or no
isPythonInteresting = True

#Data Structures A single variable storing multiple values

cars = {"Toyota", "Ford", "Mustang", "Mercedez", "Cadillac escallade"} #List - ordered and changeable

fruits = ("Banana", "Cherry", "Mango", "Orange") #Taple ordered but unchangeable
Countries = { "China", "Italy", "France", "Germany"}#Set - unordered and unchangeable
#Dictionary

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict.get("model"))

## creating an array of cars
cars = ["Ford", "Volvo", "BMW"]

# adding a new car
cars.append("Honda")

# displaying the cars
print(cars)

print(Countries)
print(fruits)
print(height)
print(cars)
print(greeting)
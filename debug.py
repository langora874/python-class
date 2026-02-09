# Debug this code
name = "kabelo"
age = "23"
print("My name is " + name + " and I am " + age + " years old")

age = 17
if age >= 18:
    print("Adult")
else: 
    print("Minor")
greeting = "hello CodeTribers"
print(greeting.swapcase())

fruits = ["Apple", "Orange", "Banana"]
fruits.append("Mango")
print(fruits)

for i in range(1,5):
  print(i)

num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")

file = open("data.txt", "w")
file.write("Python is fun")
file.close()
age = int(input("Enter your age: "))
if age >= 18:
    print("You can vote")
else:
    print("You cannot vote yet")

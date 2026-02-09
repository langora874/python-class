#A function is a block of code that performs a specific task.
#It only runs when you call it
 
def greet():   #def- Keyword used to define a function
    print("Hello, welcome to Python!")
    
# Call the function
def greetings(name):#definging a fuction
 
    #print("Hello " ,name)

    print(f'Hello{name}')#A parameter is a placeholder inside the function definition.

def addnumbers(a, b):
    z=a+b
    return z
total=addnumbers(30,70)
print(total)

#Subtraction 
def subtract(x, y):
    a = x - y      # subtract y from x
    return a

total = subtract(10, 3)  # pass two numbers
print("Total:", total)



greetings(" Oratile") #calling a function// # "Oratile" → argument (the actual value you pass in)
#An argument is the actual value you pass when you call the function.
greet()








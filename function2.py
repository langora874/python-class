#x + y → adds the two numbers
#x * y → multiplies them
#return add, multiply → sends back both results
#You can store both results in two variables:

def calculate(x, y):
    add = x + y
    multiply = x * y
    return add, multiply
sum_result, product_result = calculate(5, 3)
print("Sum:", sum_result)
print("Product:", product_result)

# Divide
# x / y → divides x by y.

# Return result → sends the answer back to where the function was called.

# The result is often a float (like 5.0 instead of 5).

def divide(x, y):
    result = x / y
    return result
# Call the function
answer = divide(10, 2)
print("The result is:", answer)


def calculate(a, b):
    print("Addition:", a + b)
    print("Subtraction:", a - b)
    print("Multiplication:", a * b)
    if b != 0:
        print("Division:", a / b)
    else:
        print("Division: Cannot divide by zero")

calculate(10, 5)





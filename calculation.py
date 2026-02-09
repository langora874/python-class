# float are you used when you need to present decimal numbers (5.0 instead of 5)
# if and elif are used when you have multiply condition 
num1=int(input ("Enter first number :"))
num2=int(input("Enter second number :"))
op=input("Enter operation(+,-,*,/):")
if op=='+':
    print(num1+num2)

elif op=='-':
    print(num1-num2)
    if op=='*':
       print(num1*num2)
elif op=='/':
    print(num1/num2)
else:
   print("Invaild operation")
    
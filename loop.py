#Loops-To repeat a set of instructions or automate repetitive tasks.

#While Loop control flow statement that repeatedly executes a block of code as long as a specified Boolean condition remains True. 
#while loop example 
x=0                
y=0

days=["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]

while(x<5):
    print(x)
    x=x+1 #(increment by 1)

#for loop is a control flow statement used to iterate over the items of any sequence
for y in range(0,11):
    print(y)

for d in days:
    if d=="Fri":
        print("heyyyy its Friday")
        break #means Stop
    print(d)

for d in days:
    if d =="Tue":
        continue # means skip and go too the next
    print(d)




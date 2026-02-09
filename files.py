# create a file
myfile=open('myfile.txt','w')
# printing file name
print('Name :', myfile.name)
#checking if file is closed
print('Is closed' , myfile.closed)
#Checking the mode of the file
print('Mode' , myfile.mode)
#Writing to file
myfile.write('Its Monday its going to be a hectic day\n')  #\n -i want to add a second line
# Closing file
myfile.write('Monday motivation :Dont stress Friday is tomorrow')
myfile.close()
print('Is closed' , myfile.closed)#check if file is closed

# Reopen the file and edit(a)
myfile=open('myfile.txt','a')
myfile.write('\n Keep going KB')
myfile.close()

# Read from file
myfile=open('myfile.txt','r+')
text=myfile.read(200)
print('File content\n' , text)
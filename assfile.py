file=open('hobbies.txt','w')
# printing file name
print('Name :', file.name)
file.write("My hobbies:\n")
file.write("1.reading\n")
file.write("2.Playing soccer\n")
file.write("3.Going for a walk\n")
file.write("4.Watching movies\n")
file.write("5.Chilling with mike\n")
file.close


file= open("hobbies.txt" , "a")
file.write("\n A sentence about me:\n")
file.write("I am a creative person and I love to think")
file.close()


file = open("hobbies.txt" , "r")
content=file.read(300)
print("Reading from file:\n")
print(content)
file.close()
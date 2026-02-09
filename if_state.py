mark = (input("Enter your mark"))
mark=int(mark)

if mark < 50:
  print("you have failed")

elif 50<= mark<=59:
  print("you have passed")
else:
  print("invalid or higher range mark")
  print(mark)
  